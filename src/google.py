# src\google.py

import logging
import google.generativeai as genai
from src.base import LLM


class GoogleLLM(LLM):

    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.model_name = model_name
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def generate_content(self, prompt: str) -> str:
        """Generates text using the LLM."""

        try:
            response = self.model.generate_content(prompt)
            return response.text.strip() if response.text else None
        except Exception as e:
            logging.error(f"Error generating text: {e}")
            return None