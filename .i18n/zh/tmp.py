import json
from fuzzywuzzy import fuzz, process

lang_file = '.i18n/zh/Game.json'

def process_json_contents(contents):
    modified_contents = {}
    for key, value in contents.items():
        # Check if the key does not end with '\n'
        if not key.endswith('\n'):
            # Remove the newline from the end of the value, if it exists
            modified_contents[key] = value.rstrip('\n')
        else:
            modified_contents[key] = value
    return modified_contents

# Read the original JSON file
with open(lang_file, 'r', encoding='utf-8') as file:
    contents = json.load(file)

# Process the contents
modified_contents = process_json_contents(contents)

# Write the modified contents back to the file
with open(lang_file, 'w', encoding='utf-8') as file:
    json.dump(modified_contents, file, ensure_ascii=False, indent=4)
