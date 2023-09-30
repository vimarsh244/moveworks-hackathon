# from sentence_transformers import SentenceTransformer, util
# import faiss
import os
import re
import requests
import hashlib
import urllib.parse
from bs4 import BeautifulSoup
from PIL import Image
import PIL
import pytesseract
import markdown
import io


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



# Function to prune the width part from image URLs
def prune_image_width(image_url):
    # Remove the width parameter from the URL
    return re.sub(r'\?width=\d+', '?', image_url)



def prune_image_url(image_url):
    return image_url.split('?')[0]


# Function to exclude header and footer elements from the parsed HTML
def exclude_header_footer(soup):
    # Specify CSS selectors or attributes to identify header and footer elements
    header_selectors = ['header', '.header', '#header']
    footer_selectors = ['footer', '.footer', '#footer']

    # Remove header elements
    for selector in header_selectors:
        header_elements = soup.select(selector)
        for element in header_elements:
            element.extract()

    # Remove footer elements
    for selector in footer_selectors:
        footer_elements = soup.select(selector)
        for element in footer_elements:
            element.extract()

    return soup

# Function to scrape text and images from a webpage and save as Markdown with inline images
def scrape_and_save_as_markdown(url, output_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = exclude_header_footer(soup)

    # Generate a unique filename based on the URL
    filename = generate_filename(url)
    output_path = os.path.join(output_dir, filename)

    # Open the Markdown file for writing
    with open(output_path, 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(f"# {url}\n\n")

        # Extract text and images while keeping them inline
        for element in soup.find_all(['p', 'img']):
            if element.name == 'p':
                text = element.get_text()
                markdown_file.write(f"{text}\n\n")
            elif element.name == 'img':
                alt_text = element.get('alt', 'Image')
                img_url = element.get('src', '')
                img_url = prune_image_width(img_url)

                if img_url.startswith('http'):
                    markdown_file.write(f"![{alt_text}]({img_url})\n\n")


# Function to perform OCR on an image and return the extracted text (only for supported formats)
# Function to perform OCR on an image and return the extracted text (only for supported formats)
def perform_ocr(image_url):
    response = requests.get(image_url)
    image_bytes = response.content

    # Check if the image is in a supported format (e.g., PNG)
    if image_url.lower().endswith(('.png', '.jpeg', '.jpg', '.bmp', '.tiff')):
        try:
            image = Image.open(io.BytesIO(image_bytes))
            extracted_text = pytesseract.image_to_string(image)
            return extracted_text
        except PIL.UnidentifiedImageError:
            return None
    else:
        return None

# Function to update alt-text in Markdown files with OCR results
def update_alt_text_with_ocr(markdown_dir):
    for filename in os.listdir(markdown_dir):
        if filename.endswith('.md'):
            with open(os.path.join(markdown_dir, filename), 'r+', encoding='utf-8') as markdown_file:
                markdown_content = markdown_file.read()

                # Find image URLs and perform OCR (for supported formats)
                for match in re.finditer(r'!\[([^\]]*)\]\(([^)]*)\)', markdown_content):
                    alt_text = match.group(1)
                    img_url = match.group(2)

                    # Prune image width if necessary
                    img_url = prune_image_url(img_url)

                    # Perform OCR (only for supported formats) and update alt-text
                    print("doing OCR for : " + img_url)
                    extracted_text = perform_ocr(img_url)
                    if extracted_text:
                        print("Got text: " + extracted_text)
                    if extracted_text:
                        # Sanitize extracted text and alt text
                        extracted_text = ' '.join(extracted_text.split())  # Replace consecutive spaces with single space
                        extracted_text = extracted_text.strip()  # Remove leading and trailing whitespace
                        extracted_text = extracted_text.replace('\n', '\\n')  # Replace new lines with "\\n"
                        
                        alt_text = ' '.join(alt_text.split())  # Replace consecutive spaces with single space
                        alt_text = alt_text.strip()  # Remove leading and trailing whitespace
                        alt_text = alt_text.replace('\n', '\\n')  # Replace new lines with "\\n"

                        markdown_content = markdown_content.replace(match.group(0), f"![{alt_text} | {extracted_text}]({img_url})")

                        # markdown_content = markdown_content.replace(match.group(0), f"![{alt_text} | {extracted_text.strip()}]({img_url})")

                # Rewind the file and write updated content
                markdown_file.seek(0)
                markdown_file.write(markdown_content)
                markdown_file.truncate()




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

    print("getting sitemap...")
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract URLs from sitemap.xml
    urls = extract_sitemap_urls(sitemap_url)

    print("downloading pages...")
    # Scrape and save as Markdown
    for url in urls:
        scrape_and_save_as_markdown(url, output_dir)

    markdown_dir = output_dir
    
    print("doing OCR")

    update_alt_text_with_ocr(markdown_dir)

    # Create embeddings
    # create_embeddings(output_dir, model_name, embeddings_output_file)
