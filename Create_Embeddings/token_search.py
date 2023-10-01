import os
import re

# Define the folder path and the token you want to search for
folder_path = "../pages"
token_to_search = "CEO of moveworks"

# Define a regular expression pattern to match the token (case insensitive)
pattern = re.compile(fr'(.{{0,25}}\b{re.escape(token_to_search)}\b.{{0,25}})', re.IGNORECASE)

# Function to search for tokens in a file and return the surrounding text
def search_tokens_in_file(file_path, token):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(token, content)
        return matches

match_list = []

# Iterate through files in the folder
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.md'):
            file_path = os.path.join(root, file_name)
            matches = search_tokens_in_file(file_path, pattern)

            if matches:
                print(f"Found {len(matches)} occurrences of '{token_to_search}' in {file_path}:")
                match_list.append(file_name)
                for match in matches:
                    print(f"  - {match}")

print(match_list)
