import unittest
from src.google import GoogleLLM
from src.huggingface import HuggingfaceLLM
from src.openai import OpenAILLM
from dotenv import load_dotenv
load_dotenv()

class TestLLMUtils(unittest.TestCase):
    def test_google_llm_generate(self):
        llm = GoogleLLM(model_name="gemini-1.5-flash")
        response = llm.generate_content("What is the capital of France?")
        self.assertIsNotNone(response)

    def test_huggingface_llm_generate(self):
        llm = HuggingfaceLLM(model_name="microsoft/Phi-3-mini-128k-instruct")
        response = llm.generate_content("What is the capital of France?")
        self.assertIsNotNone(response)

    def test_openai_llm_generate(self):
        llm = OpenAILLM(model_name="gpt-4")
        response = llm.generate_content("What is the capital of France?")
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
