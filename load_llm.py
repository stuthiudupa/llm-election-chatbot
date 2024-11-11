"""
This module loads the LLM from the local file system
Modify this file if you need to download some other model from Hugging Face or OpenAI/ChatGPT
"""

from langchain.llms import CTransformers
from langchain_openai import OpenAI

# Step 1: Initialize the model
model_name = r'C:\Users\ananth\.cache\lm-studio\models\MaziyarPanahi\Mistral-7B-Instruct-v0.3-GGUF'
model_file = model_name + r"\Mistral-7B-Instruct-v0.3.Q4_K_M.gguf"


# def load_llm():
#     """
#     Load the LLM from local file system. You can also load it from Hugging Face or use Open AI models
#     In our case we use locally set up Mistral model
#
#     :return: loaded llm
#     """
#     llm_config = {
#         "temperature": 0,
#         'max_new_tokens': 8192,
#         "context_length": 8192,
#         'gpu_layers': 50,
#     }
#
#     llm = CTransformers(
#                         model=model_name,
#                         model_file=model_file,
#                         config=llm_config)
#
#     return llm

def load_llm():
    llm = OpenAI(
        base_url="http://localhost:1234/v1",
        api_key="llama",
        max_tokens=2048,
    )
    return llm


if __name__ == '__main__':
    llm = load_llm()
    result = llm.invoke("Provide a short answer: What is machine learning?")
    print(result)
