import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import time
import re
import json
from urllib.request import urlopen
import json


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

model = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")


main = FAISS.load_local("faiss_main", model)


def get_answer(query):
    print(query)
    response = {}
    # query = "Open career positions at moveworks"
    # docs = main.similarity_search(query)
    docs = main.similarity_search_with_score(query)
    
    for doc in docs:
        file = str(doc[0].metadata['source'])
        with open(file, "r") as f:
            url = f.readline().strip().split()[-1]
        response[url] = doc[0].page_content
        print(doc[0].page_content)
        
    return response
