from retrieval_module_service import execute_retrieval_step
from argumentation_module_service import  execute_argumentation_step
from generation_module_service import execute_generation_step


def execute_rag_app(question):
    documents_stored = execute_retrieval_step("llama3", "promptior_presentation.pdf", "https://www.promtior.ai/service")
    chain = execute_argumentation_step("llama3",documents_stored)
    return execute_generation_step(chain, question)
