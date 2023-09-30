import os
import requests
from bs4 import BeautifulSoup
# from sentence_transformers import SentenceTransformer, util
# import faiss
import markdown
import urllib.parse
import hashlib

# Function to extract URLs from a sitemap.xml file
def extract_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = [loc.text for loc in soup.find_all('loc')]
    return urls

# Function to generate a unique filename from a URL
def generate_filename(url):
    # Hash the URL path and use it as the filename (truncated for brevity)
    url_path = urllib.parse.urlparse(url).path
    url_hash = hashlib.sha1(url_path.encode()).hexdigest()[:8]
    return f"{url_hash}_{os.path.basename(url_path)}.md"

# Function to scrape text and images from a webpage and save as Markdown with inline images
def scrape_and_save_as_markdown(url, output_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text
    text = ""
    for paragraph in soup.find_all('p'):
        text += f"{paragraph.get_text()}\n\n"

    # Generate a unique filename based on the URL
    filename = generate_filename(url)
    output_path = os.path.join(output_dir, filename)

    # Save as Markdown with inline images
    markdown_content = f"# {url}\n\n{text}\n\n"

    for img_tag in soup.find_all('img'):
        alt_text = img_tag.get('alt', 'Image')
        img_url = img_tag.get('src', '')

        if img_url.startswith('http'):
            markdown_content += f"![{alt_text}]({img_url})\n"

    with open(output_path, 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(markdown_content)


"""
# Function to create sentence embeddings using sentence-transformers and faiss
def create_embeddings(data_dir, model_name, output_file):
    model = SentenceTransformer(model_name)
    embeddings = []
    filenames = []

    for filename in os.listdir(data_dir):
        if filename.endswith('.md'):
            with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as markdown_file:
                text = markdown_file.read()
                embeddings.append(model.encode(text))
                filenames.append(filename)

    embeddings = util.normalize_embeddings(embeddings)
    embeddings = faiss.IndexFlatL2(embeddings[0].shape[0])
    embeddings.add(np.array(embeddings))

    faiss.write_index(embeddings, output_file)
"""
if __name__ == "__main__":
    sitemap_url = "https://moveworks.com/sitemap.xml"
    output_dir = "pages"
    model_name = "paraphrase-MiniLM-L6-v2"
    embeddings_output_file = "embeddings.index"

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract URLs from sitemap.xml
    urls = extract_sitemap_urls(sitemap_url)

    # Scrape and save as Markdown
    for url in urls:
        scrape_and_save_as_markdown(url, output_dir)

    # Create embeddings
    # create_embeddings(output_dir, model_name, embeddings_output_file)
