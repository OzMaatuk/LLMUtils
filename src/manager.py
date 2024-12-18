# src/manager.py

from typing import Optional
from src.google import GoogleLLM
from src.huggingface import HuggingfaceLLM
from src.openai import OpenAILLM

class LLMManager:
    """Manages interactions with Language Models (LLMs)."""

    def __init__(self, model_name: str = "gemini-1.5-flash"):
        if "gemini" in model_name:
            self.model = GoogleLLM(model_name)
        elif "gpt" in model_name:
            self.model = OpenAILLM(model_name)
        else:
            self.model = HuggingfaceLLM(model_name)

    def generate_text(self, prompt: str) -> Optional[str]:
        return self.model.generate_content(prompt)