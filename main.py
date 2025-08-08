import os
from smolagents import Tool, CodeAgent, DuckDuckGoSearchTool, InferenceClientModel
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

class WebScraperTool(Tool):
    name = "web_scraper"
    description = "Scrape and return the visible text from a webpage URL."
    inputs = {"url": {"type": "string", "description": "URL to scrape"}}
    output_type = "string"

    def forward(self, url: str):
        try:
            html = requests.get(url, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            for script in soup(["script", "style"]):
                script.extract()
            return " ".join(soup.stripped_strings)
        except Exception as e:
            return f"Error scraping {url}: {e}"

model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    api_key=os.getenv("HF_API_KEY")
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), WebScraperTool()],
    model=model,
    add_base_tools=True,
    max_steps=8
)

def research_topic(query: str) -> str:
    prompt = f"""
    Step 1: Use DuckDuckGoSearchTool to find 3–5 relevant web pages for '{query}'.
    Step 2: For each page, use WebScraperTool to extract the full text.
    Step 3: Combine the extracted texts and write:
      - A short summary (max 200 words)
      - 5 bullet-point key takeaways
      - A list of reference URLs used
    """
    return agent.run(prompt)

if __name__ == "__main__":
    query = input("Enter your research topic: ")
    print("\n--- RESEARCH SUMMARY ---\n")
    print(research_topic(query))
