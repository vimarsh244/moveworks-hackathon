import os
import re

# Define the folder path and the token you want to search for
folder_path = "../pages"
<<<<<<< HEAD
token_to_search = "CEO of Moveworks"
=======
token_to_search = "CEO of moveworks"
>>>>>>> e12cb0e7d0e21e0ae88b34e4cf822bbf09b834a2

# Define a regular expression pattern to match the token (case insensitive)
pattern = re.compile(fr'(.{{0,25}}\b{re.escape(token_to_search)}\b.{{0,25}})', re.IGNORECASE)

<<<<<<< HEAD
context_length = 200
# Function to search for tokens in a file and get context
=======
# Function to search for tokens in a file and return the surrounding text
>>>>>>> e12cb0e7d0e21e0ae88b34e4cf822bbf09b834a2
def search_tokens_in_file(file_path, token):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.finditer(token, content)
        for match in matches:
            start_index = max(0, match.start() - context_length)
            end_index = min(len(content), match.end() + context_length)
            context = content[start_index:end_index]
            yield context

# Iterate through files in the folder
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.md'):
            file_path = os.path.join(root, file_name)
            for context in search_tokens_in_file(file_path, pattern):
                print(f"Context for '{token_to_search}' in {file_path}:")
                print(context)
                print("-" * 50)
