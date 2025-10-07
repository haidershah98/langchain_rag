from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from constants import *

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

vectordb = Chroma(
    persist_directory=DB_NAME,
    embedding_function=embeddings
)
