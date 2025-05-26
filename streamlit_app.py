# streamlit_app.py
import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import matplotlib.pyplot as plt

# CONFIG
API_URL = "http://127.0.0.1:8000"  # FastAPI backend
MODEL_NAME = "llama3"

st.set_page_config(page_title="SerenityGPT", page_icon="🧘‍♂️", layout="centered")
st.title("🧘‍♂️ SerenityGPT: Your AI Mental Wellness Coach")

# USER INPUT
prompt = st.text_input("What's on your mind today?", placeholder="I'm feeling anxious about an exam tomorrow...")

if st.button("Ask Coach"):
    if prompt:
        with st.spinner("Thinking..."):
            response = requests.post(API_URL, json={"model": MODEL_NAME, "prompt": prompt})
            if response.status_code == 200:
                reply = response.json()["response"]
                st.success("🧠 Coach Says:")
                st.write(reply)

                # Save to journal
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                journal_entry = pd.DataFrame([[timestamp, prompt, reply]], columns=["Timestamp", "User", "Coach"])
                journal_entry.to_csv("journal.csv", mode='a', index=False, header=not pd.io.common.file_exists("journal.csv"))
            else:
                st.error("Failed to connect to AI Navigator API. Make sure it's running.")
    else:
        st.warning("Please enter your thoughts first.")

# MOOD TRACKER
st.subheader("🧭 Mood Tracker")
mood = st.selectbox("How do you feel right now?", ["😊 Happy", "😐 Neutral", "😢 Sad", "😰 Anxious", "😡 Angry"])
if st.button("Log Mood"):
    mood_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d %H:%M:%S"), mood]], columns=["Timestamp", "Mood"])
    mood_entry.to_csv("mood.csv", mode='a', index=False, header=not pd.io.common.file_exists("mood.csv"))
    st.success("Mood logged!")

# MOOD CHART
if st.checkbox("📊 Show Mood Trends"):
    if pd.io.common.file_exists("mood.csv"):
        df = pd.read_csv("mood.csv")
        df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
        mood_counts = df.groupby(['Date', 'Mood']).size().unstack(fill_value=0)
        mood_counts.plot(kind='bar', stacked=True, figsize=(10, 4))
        st.pyplot(plt)
    else:
        st.info("No mood data available yet.")

# BREATHING EXERCISE
st.subheader("🫁 Guided Breathing Exercise")
if st.button("Show Exercise"):
    st.markdown("""
    ### 🌬️ Try this:
    1. **Inhale** slowly for 4 seconds  
    2. **Hold** for 4 seconds  
    3. **Exhale** slowly for 4 seconds  
    4. **Hold** for 4 seconds  
    🌀 Repeat 4 times to feel the calm.
    """)
    st.image("assets/meditation1.png", use_column_width=True, caption="Relax and Breathe")

# JOURNAL VIEWER
if st.checkbox("📖 View Journal Entries"):
    if pd.io.common.file_exists("journal.csv"):
        df = pd.read_csv("journal.csv")
        st.dataframe(df[::-1])  # Show latest first
    else:
        st.info("No journal entries yet.")
