# 🧠 SmolAgents Research & Summarizer

An AI-powered research assistant built with [smolagents](https://huggingface.co/docs/smolagents/index), capable of searching the web, scraping full-page content, and producing concise research summaries with bullet points and optional reference URLs.
Runs in both **CLI mode** and **Gradio Web UI** with live configuration options.

---

## ✨ Features

* 🔍 **Web Search + Scraping** — Uses DuckDuckGo and BeautifulSoup to pull full-page content, not just snippets.
* 🧠 **Multiple Hugging Face Models** — Choose from free/open-source models like Qwen, Mistral, and Llama.
* ⚙️ **Live Configurable Parameters**:

  * Model selector
  * Number of search results
  * Summary length (word target)
  * Max agent steps
  * Include/exclude references toggle
* 💻 **Two Modes**:

  * **CLI**: Quick research from the terminal
  * **Gradio UI**: Interactive web interface

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
pip install -r requirements.txt
```

Also, create a `.env` file in the project root with your Hugging Face API key:

```
HF_API_KEY=your_api_key_here
```

Get a free API key here: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## 🚀 Usage

### **CLI Mode**

```bash
python main.py
```

Follow the prompts to enter a topic and get your research summary.

---

### **Gradio Web UI**

```bash
python app.py
```

Then open the provided `localhost` link in your browser.

In the UI, you can:

* Select your preferred model
* Adjust summary length, search results, and steps
* Toggle whether to include reference URLs

---

## 🛠 Example

**Topic:** *Advances in solar panel technology*
**Model:** Qwen/Qwen2.5-Coder-32B-Instruct
**Summary Length:** 200 words
**Results:** *(truncated)*

```
--- Research Summary ---

Recent advancements in solar panel technology focus on higher efficiency rates, improved durability, and reduced manufacturing costs...
...
References:
1. https://example.com/article1
2. https://example.com/article2
```

---

## 📚 Tech Stack

* **[smolagents](https://huggingface.co/docs/smolagents)** — Agent framework
* **DuckDuckGo Search API** — Web search
* **BeautifulSoup** — HTML parsing & scraping
* **Gradio** — UI
* **Python 3.10+**

