# SerenityGPT 💬✨  
An intelligent local chatbot powered by Meta’s **LLaMA 3-8B-Instruct** model, designed to run privately on your machine using **Anaconda AI** with a modern UI built with **Streamlit** and a **FastAPI** backend.

---

## 🚀 Features

- 🔐 **Private & Local AI**: Entirely local setup using LLaMA 3-8B Instruct model.
- 🎨 **Interactive UI**: Simple, beautiful frontend with Streamlit.
- ⚙️ **Robust Backend**: FastAPI handles requests, model logic, and completions.
- 🔄 **Anaconda AI Integration**: Uses Anaconda’s built-in local `llamafile` model serving.
- 🔁 **Chat History**: Session-based chat memory (extendable to database).

---

## 🧠 Model Used

### 🔸 Meta-LLaMA 3-8B-Instruct (Quantized)
- **Model File**: `Meta-Llama-3-8B-Instruct_Q4_K_M.gguf`
- **Provider**: Anaconda AI Navigator
- **Running as API**: Via `llamafile` inside Anaconda
- **Endpoint**: `http://127.0.0.1:8080/completion`
- **API Key**: `llamakey` (as per Anaconda AI default)
- **Supports**: JSON-based completions similar to OpenAI's style APIs.

---

## 🗂️ Project Structure

```plaintext
SerenityGPT/
│
├── app.py                  # FastAPI backend server
├── streamlit_app.py        # Frontend UI using Streamlit
├── llama_client.py         # API client to query Anaconda AI LLaMA model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
│
├── serenity_env/           # Virtual environment (not in repo)
│
└── assets/                 # (Optional) for custom logos, CSS, etc.



## 🛠️ Setup Instructions (For Windows)

### 🔹 1. Clone the Project
```bash
git clone https://github.com/your-username/SerenityGPT.git
cd SerenityGPT
```

### 🔹 2. Create and Activate a Virtual Environment
```powershell
python -m venv serenity_env
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  # if you face script execution issues
.\serenity_env\Scripts\Activate.ps1
```

### 🔹 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 🔹 4. Start the LLaMA Model in Anaconda AI
- Open **Anaconda Navigator > AI Tab**
- Select the model: `Meta-LLaMA-3-8B-Instruct_Q4_K_M.gguf`
- Click **Start API Server**
- Confirm the server is running at: `http://127.0.0.1:8080` with API Key: `llamakey`

---

## ⚙️ Running the Application

### 🔸 Start FastAPI Backend
```powershell
uvicorn app:app --reload
```
Runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 🔸 Start Streamlit Frontend
Open **another terminal**, activate the environment again, then run:
```powershell
streamlit run streamlit_app.py
```
Visit: [http://localhost:8501](http://localhost:8501)

---

## 🔌 Component Overview

| Component         | Description |
|------------------|-------------|
| `llama_client.py` | Connects to Anaconda AI's running LLaMA model using the `/completion` endpoint |
| `app.py`         | FastAPI backend that acts as a bridge between the frontend and the model |
| `streamlit_app.py` | Frontend UI to send user queries and display model responses |
| Anaconda AI      | Provides the model server with API access locally — no internet or OpenAI needed |

---

## 📤 Sharing with Others

To share with others:

- Run on a **LAN** and let others access your local IP (adjust `uvicorn` and `streamlit` host to `0.0.0.0`).
- Use **Ngrok** or **Cloudflare Tunnel** to expose your local `localhost` to the internet.

Example:
```bash
ngrok http 8501
```
> Note: Sharing externally may require port forwarding or tunneling due to local-only deployment.

---

## 🧼 Shutting Down

- Press `Ctrl + C` in each terminal (backend/frontend)
- Deactivate the virtual environment:
```powershell
deactivate
```

---

## 📚 Detailed Description of the Model Used

### 🧠 Meta-LLaMA-3-8B-Instruct_Q4_K_M

The `Meta-LLaMA-3-8B-Instruct_Q4_K_M` is a locally deployable, instruction-tuned large language model (LLM) developed by **Meta AI**. It is optimized for efficient resource use and conversational AI tasks, making it ideal for local chatbot applications like **SerenityGPT**.

---

### 🔍 General Overview

| Property              | Value                                              |
|-----------------------|----------------------------------------------------|
| **Model Family**       | LLaMA (Large Language Model Meta AI)               |
| **Model Name**         | Meta-LLaMA-3-8B-Instruct                           |
| **Quantization**       | Q4_K_M (4-bit quantization for efficiency)         |
| **Parameters**         | 8 Billion                                          |
| **Architecture**       | Decoder-only Transformer                           |
| **Context Length**     | 8,192 tokens                                       |
| **Training Data**      | 15 Trillion tokens (public sources)                |
| **Release Date**       | April 18, 2024                                    |
| **API Endpoint Used**  | `http://127.0.0.1:8080/completion`                 |

---

### 📦 Quantization Details: Q4_K_M

Quantization reduces the model’s size and computational needs by converting weights to a lower-bit format. The `Q4_K_M` quantization provides:

- ✅ Significant memory footprint reduction  
- 🚀 Faster inference speeds  
- 🎯 Minimal quality loss in model output  
- 🧠 Perplexity score around 8.52 (close to full precision)

---

### ⚡ Capabilities of the Model

- 💬 Natural language conversations  
- 📄 Text summarization and rewriting  
- 📊 Basic reasoning and problem solving  
- 🧑‍💻 Code generation and explanation  
- 🌐 Multilingual text understanding  
- 🧾 Instruction following and tool use

---

### 📈 Performance Benchmarks

| Task / Benchmark    | Score / Accuracy       |
|---------------------|------------------------|
| **MMLU (5-shot)**   | 69.4%                  |
| **GSM8K (Math)**    | 84.5% (with chain-of-thought prompting) |
| **HumanEval**       | 72.6% pass@1           |

These benchmarks position the model competitively among open-source LLMs in the 7B–13B parameter range.

---

### 🧩 Role in SerenityGPT

This model acts as the **core AI engine** behind SerenityGPT, integrated as follows:

| Component           | Description                                              |
|---------------------|----------------------------------------------------------|
| `llama_client.py`   | Connects to Anaconda AI’s local LLaMA API for inference  |
| `app.py`            | FastAPI backend handling client requests and responses   |
| `streamlit_app.py`  | Streamlit frontend providing the user interface          |
| **Anaconda AI**     | Hosts the model locally and exposes it via REST API      |

---

### 🛡️ Why Use This Model?

- 📍 **Fully Local Inference**: Ensures user data privacy with no external calls.  
- 🛠️ **Efficient & Lightweight**: Runs on consumer hardware with moderate RAM.  
- ⚡ **Instruction-Tuned**: Provides natural and coherent conversational responses.  
- 💬 **Versatile**: Suitable for a variety of NLP tasks beyond chat.

---

### 🙏 Acknowledgements

- Meta AI for the LLaMA 3 model family.  
- Anaconda AI for enabling local model serving.  
- The open-source community for tooling and benchmarking resources.


## 🛠️ Future Improvements

- Add persistent chat history using SQLite or MongoDB
- Add voice input/output
- Implement authentication for shared access
- Extend to multi-model switch (e.g., Mistral, Gemma)

## 👋 HellO There! Let's Dive Into the World of Ideas 🚀

Hey, folks! I'm **Himanshu Rajak**, your friendly neighborhood tech enthusiast. When I'm not busy solving DSA problems or training models that make computers *a tad bit smarter*, you’ll find me diving deep into the realms of **Data Science**, **Machine Learning**, and **Artificial Intelligence**.  

Here’s the fun part: I’m totally obsessed with exploring **Large Language Models (LLMs)**, **Generative AI** (yes, those mind-blowing AI that can create art, text, and maybe even jokes one day 🤖), and **Quantum Computing** (because who doesn’t love qubits doing magical things?).  

But wait, there's more! I’m also super passionate about publishing research papers and sharing my nerdy findings with the world. If you’re a fellow explorer or just someone who loves discussing tech, memes, or AI breakthroughs, let’s connect!

- **LinkedIn**: [Himanshu Rajak](https://www.linkedin.com/in/himanshu-rajak-22b98221b/) (Professional vibes only 😉)
- **Medium**: [Himanshu Rajak](https://himanshusurendrarajak.medium.com/) (Where I pen my thoughts and experiments 🖋️)

Let’s team up and create something epic. Whether it’s about **generative algorithms** or **quantum wizardry**, I’m all ears—and ideas!  
🎯 Ping me, let’s innovate, and maybe grab some virtual coffee. ☕✨
