# main.py

import os
import logging
from dotenv import load_dotenv
from src.google import GoogleLLM
from src.huggingface import HuggingfaceLLM
from src.openai import OpenAILLM


def test_google_llm():
    if not os.environ.get("GOOGLE_API_KEY"):
        logging.error("GOOGLE_API_KEY environment variable is not set.")
        return

    llm = GoogleLLM()

    prompt = "What is the capital of France?"
    generated_content = llm.generate_content(prompt)
    if generated_content:
        print(f"Generated Content: {generated_content}")
    else:
        print("Failed to generate content.")


def test_openai_llm():
    if not os.environ.get("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set.")
        return

    llm = OpenAILLM()

    prompt = "What is the capital of France?"
    generated_content = llm.generate_content(prompt)
    if generated_content:
        print(f"Generated Content: {generated_content}")
    else:
        print("Failed to generate content.")


def test_huggingface_llm():
    if not os.environ.get("HF_TOKEN"):
        logging.error("HF_TOKEN environment variable is not set.")
        return

    llm = HuggingfaceLLM()

    prompt = "What is the capital of France?"
    generated_content = llm.generate_content(prompt)
    if generated_content:
        print(f"Generated Content: {generated_content}")
    else:
        print("Failed to generate content.")


def main():
    load_dotenv()
    test_google_llm()
    # test_openai_llm()
    test_huggingface_llm()


if __name__ == "__main__":
    main()