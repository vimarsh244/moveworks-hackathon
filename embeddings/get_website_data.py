import xmltodict
import requests

r = requests.get("https://moveworks.com/sitemap.xml")
xml = r.text
raw = xmltodict.parse(xml)

from bs4 import BeautifulSoup

def extract_text_from(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="html.parser")
    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    return '\n'.join(line for line in lines if line)

pages = []
for info in raw['urlset']['url']:
    # info example: {'loc': 'https://www.paepper.com/...', 'lastmod': '2021-12-28'}
    url = info['loc']
    if 'https://www.moveworks.com/' in url:
        pages.append({'text': extract_text_from(url), 'source': url})



# from langchain.text_splitter import CharacterTextSplitter

# text_splitter = CharacterTextSplitter(chunk_size=1500, separator="\n")
# docs, metadatas = [], []
# for page in pages:
#     splits = text_splitter.split_text(page['text'])
#     docs.extend(splits)
#     metadatas.extend([{"source": page['source']}] * len(splits))
#     print(f"Split {page['source']} into {len(splits)} chunks")


# import faiss
# from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
# import pickle

# store = FAISS.from_texts(docs, OpenAIEmbeddings(), metadatas=metadatas)
# with open("faiss_store.pkl", "wb") as f:
#     pickle.dump(store, f)


# import faiss
# from langchain import OpenAI
# from langchain.chains import VectorDBQAWithSourcesChain
# import pickle
# import argparse

# parser = argparse.ArgumentParser(description='Paepper.com Q&A')
# parser.add_argument('question', type=str, help='Your question for Paepper.com')
# args = parser.parse_args()

# with open("faiss_store.pkl", "rb") as f:
#     store = pickle.load(f)

# chain = VectorDBQAWithSourcesChain.from_llm(
#             llm=OpenAI(temperature=0), vectorstore=store)
# result = chain({"question": args.question})

# print(f"Answer: {result['answer']}")
# print(f"Sources: {result['sources']}")
