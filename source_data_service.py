import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader


def get_data_by_web(url):
    return WebBaseLoader(url).load()

#"promptior_presentation.pdf"
def get_data_by_documents(file_name):
    title_target = "About Promtior"
    absolut_path = os.path.dirname(os.path.abspath(__file__))
    document_path = os.path.join(absolut_path, file_name)
    for document in PyPDFLoader(document_path).load_and_split():
        if document.page_content.startswith(title_target) or  document.page_content.endswith(title_target):
            return document