import os
import gradio as gr
from main import research_topic, agent
from smolagents import InferenceClientModel

# Available models (free/open-source on Hugging Face):
MODEL_OPTIONS = {
    "Qwen-2.5 Coder (32B)": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "Qwen3 Coder (30B A3B)": "Qwen/Qwen3-Coder-30B-A3B-Instruct",  # [ref]
    "Qwen3 Thinking (4B)": "Qwen/Qwen3-4B-Thinking-2507",  # [ref]
    "Mistral Instruct (7B)": "mistralai/Mistral-7B-Instruct-v0.3",  # [ref]
    "Llama 3.1 (8B)": "meta-llama/Llama-3.1-8B-Instruct",  # [ref]
}

def run_agent(query, model_id, num_results, summary_len, max_steps, include_refs):
    if not query.strip():
        return "⚠️ Please enter a topic."

    # Optionally override the agent's model dynamically
    agent.model = InferenceClientModel(model_id=model_id, api_key=os.getenv("HF_API_KEY"))
    agent.max_steps = int(max_steps)
    
    prompt = f"""
    Step 1: Use DuckDuckGoSearchTool to find {num_results} relevant web pages for '{query}'.
    Step 2: Use WebScraperTool to fetch the full page text.
    Step 3: Generate:
      - A short summary (target ~{summary_len} words)
      - 5 bullet points
    """
    if include_refs:
        prompt += "\n  - Include reference URLs used\n"

    result = agent.run(prompt)
    return result

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 SmolAgents Research & Summarizer")

    topic = gr.Textbox(label="Research Topic", placeholder="e.g. Advances in solar panel tech")
    model = gr.Dropdown(list(MODEL_OPTIONS.keys()), label="Model", value=list(MODEL_OPTIONS.keys())[0])
    num_results = gr.Slider(1, 10, value=5, step=1, label="Number of Search Results")
    summary_len = gr.Slider(50, 500, value=200, step=50, label="Summary Length (words)")
    max_steps = gr.Slider(2, 20, value=8, step=1, label="Max Agent Steps")
    include_refs = gr.Checkbox(label="Include References", value=True)
    output = gr.Textbox(label="Research Summary", lines=20)
    btn = gr.Button("Run Research")

    btn.click(
        fn=lambda q, m, nr, sl, ms, ir: run_agent(q, MODEL_OPTIONS[m], nr, sl, ms, ir),
        inputs=[topic, model, num_results, summary_len, max_steps, include_refs],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()
