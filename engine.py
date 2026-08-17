import google.generativeai as genai
from config import SYSTEM_INSTRUCTION

class GenerationEngine:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_component(self, prompt: str) -> str:
        """Sends the structured engineering instructions and cleans response markdown."""
        full_query = f"{SYSTEM_INSTRUCTION}\n\nUser Component Request: {prompt}"
        response = self.model.generate_content(full_query)
        
        # Clean potential markdown wrapping anomalies from LLM output
        clean_text = response.text.strip()
        if clean_text.startswith("```html"):
            clean_text = clean_text[7:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
            
        return clean_text.strip()
