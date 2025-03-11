import os
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_ollama import OllamaLLM

def set_api_key():
    load_dotenv(".env")
    apikey_model = os.getenv("OPENAI_API_KEY")
    print(apikey_model)

#"llama3"
def initialize_model(model_name):
    return OllamaLLM(model=model_name)


def get_prompt_template():
    return ChatPromptTemplate.from_template(
        """Please answer the question using only the information from the context below:
        Context: {context} Question: {input}"""
    )

def chain(model, storage):
    stuff_document_chain = create_stuff_documents_chain(model, get_prompt_template())
    chain = create_retrieval_chain(storage.as_retriever(), stuff_document_chain)
    return chain

def execute_argumentation_step(model_name, storage):
    return chain( initialize_model(model_name), storage )