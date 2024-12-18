from setuptools import setup, find_packages

setup(
    name="llm_manager",
    version="0.1.0",
    description="A unified interface for managing LLMs like Google Generative AI, Hugging Face and OpenAI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="OzLevi",
    author_email="ozmaatuk@gmail.com",
    url="https://github.com/OzMaatuk/llm_manager",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-generativeai>=0.8.3",
        "openai>=1.57.4",
        "requests>=2.32.3",
        "python-dotenv>=1.0.1",
        "fastapi>=0.115.6",
        "pydantic>=2.10.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
