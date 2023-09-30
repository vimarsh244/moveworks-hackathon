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
main = FAISS.load_local("faiss_main", embeddings)

query = ""
docs = main.similarity_search_with_score(query)
comic_list = list()
for doc in docs:
    print(doc)
    file = str(doc[0].metadata['source'])
    with open(file, "r") as f:
        url = f.readline().strip().split()[-1]
    print(url)