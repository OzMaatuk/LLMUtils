# LLM Utils Library

This library provides a unified interface for interacting with language models (LLMs) such as Google Generative AI, Hugging Face models, and OpenAI GPT models. It includes dynamic backend selection and easy-to-use methods for generating text.

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```
Or
```bash
conda install --use-local llm-manager
```

## Features
- Unified interface for LLMs (`LLM` base class).
- Dynamic backend selection using `LLMManager`.
- Implementations for Google Generative AI (`GoogleLLM`), Hugging Face (`HuggingfaceLLM`), and OpenAI (`OpenAILLM`).

## Usage

### Environment Variables

Set the following environment variables before running:
- `GOOGLE_API_KEY`: API key for Google Generative AI.
- `HF_TOKEN`: Authentication token for Hugging Face.
- `OPENAI_API_KEY`: API key for OpenAI.

### Example

```python
from llm_manager import LLMManager

# Initialize the manager with a specific model
llm = LLMManager(model_name="gpt-4")

# Generate text
prompt = "What is the capital of France?"
generated_text = llm_manager.generate_text(prompt)
print(f"Generated Text: {generated_text}")
```