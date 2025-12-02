import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def read_source_code(file_path: str) -> str:
    """Reads and returns the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"\nERROR: The file '{file_path}' was not found.")
        print("Please ensure 'functions.py' is in the same directory as 'agent.py'.")
        exit(1)

def save_tests(file_name: str, content: str):
    """Saves the test content to a new file."""
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nTests successfully generated and saved to: {file_name}")

AZURE_DEPLOYMENT = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_API_VERSION = os.environ.get("AZURE_OPENAI_API_VERSION")

if not AZURE_API_VERSION:
    print("ERROR: AZURE_OPENAI_API_VERSION not found. Please check your .env file.")
    exit(1)

llm = AzureChatOpenAI(
    # Arguments required by the Azure/LangChain integration
    azure_deployment=AZURE_DEPLOYMENT,
    api_version=AZURE_API_VERSION,
    
    temperature=0.0
)

prompt_template = """
You are an experienced Test Engineer. Your task is to analyze the provided Python code
and generate comprehensive unit tests using the pytest library.

Output Instructions:
1. Start with 'import pytest' followed by the necessary import statement 'from functions import *' 
   to import all functions from the source code.
2. Use the prefix 'def test_' for all test functions.
3. Include tests for success cases (valid inputs) and failure/exception cases 
   (e.g., division by zero, invalid inputs) using 'pytest.raises'.
4. The output must be ONLY the Python code, with no surrounding text, 
   markdown fences (e.g., ```python), or explanatory prose.

PYTHON CODE TO BE TESTED:
{source_code}
"""
prompt = ChatPromptTemplate.from_template(prompt_template)

test_generator_chain = prompt | llm 


if __name__ == "__main__":
    source_file = "functions.py"
    output_file = "test_functions.py"

    print(f"Fetching source code from: {source_file}")

    source_code = read_source_code(source_file)

    print("-" * 50)
    print("Source Code Read:")
    print(source_code)
    print("-" * 50)
    print("Generating tests with the AI Agent (LangChain + Azure OpenAI)...")

    try:
        generated_tests = test_generator_chain.invoke(
            {"source_code": source_code}
        ).content.strip()

        save_tests(output_file, generated_tests)

        print("\nNext Step: Run 'pytest' in your terminal to validate the generated tests!")
    except Exception as e:
        print(f"\nERROR running the Agent: {e}")
        print("Please verify your environment variables and the Azure OpenAI deployment name are correct.")