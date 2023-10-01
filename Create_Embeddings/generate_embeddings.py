from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from pathlib import Path
import glob
import os

model = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
##Its descriptions says:
# This model was tuned for semantic search: Given a query/question, if can find relevant passages. It was trained on a large and diverse set of (question, answer) pairs.


path_to_dir = "../pages"

markdown_files = glob.glob(os.path.join(path_to_dir, "*.md"))

for file in markdown_files:
    with open(file, "r") as f:
        url = str((f.readline().strip()).split()[1]).replace("/", "_")

    loader = UnstructuredMarkdownLoader(file)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")

    db = FAISS.from_documents(docs, embeddings)
    print(Path(file).stem)
    db.save_local(f"raw_embeddings/{Path(file).stem}/")

