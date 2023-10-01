# use langchain version 0.0.300
import langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import time
import os


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
loader = TextLoader('blank.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
main = FAISS.from_documents(docs, embeddings)

files = os.listdir("raw_embeddings")

count = 0
for f in files:
    add = FAISS.load_local(f"raw_embeddings/{f}", embeddings)
    main.merge_from(add)
    print("File "+str(count)+" complete")
    count += 1

main.save_local("faiss_main")

# print(main.docstore._dict)