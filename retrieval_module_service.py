from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from source_data_service import get_data_by_web, get_data_by_documents



#"ollama3"
def initialize_embeddings(model_name):
    return OllamaEmbeddings(model=model_name)

def get_vector_store(embeddings):
    return Chroma(embedding_function=embeddings)

def get_method_chucking():
    return RecursiveCharacterTextSplitter()

def get_web_data_chucked(url):
    return get_method_chucking().split_documents( get_data_by_web( url ) )

def get_document_chucked( document_name ):
    return get_data_by_documents( document_name )

def get_documents_stored(model_name, documents):
    embeddings = initialize_embeddings( model_name )
    store = get_vector_store( embeddings )
    store.add_documents(documents=documents)
    return store

def execute_retrieval_step(model_name, document_name, url):
    documents = get_web_data_chucked( url )
    # A esto le sumamos el documento (es solo una page no es necesario trozarlo)
    documents.append( get_document_chucked(document_name) )
    return get_documents_stored(model_name, documents)