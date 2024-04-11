import json
from fuzzywuzzy import fuzz, process

source_file = '.i18n/en/Game.json'
lang_file = '.i18n/zh/Game.json'

# Load the JSON files
with open(source_file, 'r', encoding='utf-8') as file:
    en_data = json.load(file)

with open(lang_file, 'r', encoding='utf-8') as file:
    zh_data = json.load(file)

# Copy of the old zh.json to mark outdated keys
zh_old = zh_data.copy()

# Threshold for considering a fuzzy match
FUZZY_THRESHOLD = 80

zh_updated = {}

for en_key, en_value in en_data.items():
    # If there's an exact match, we use it directly
    if en_key in zh_data:
        zh_updated[en_key] = zh_data[en_key]
        zh_old.pop(en_key, None)  # Remove the matched key from zh_old
    else:
        # Find the best fuzzy match for the key
        best_match, score = process.extractOne(en_key, zh_data.keys(), scorer=fuzz.ratio)
        if score >= FUZZY_THRESHOLD:
            # Marking the value with *FUZZY*
            zh_updated[en_key] = "*FUZZY*" + zh_data[best_match]
            zh_old.pop(best_match, None)  # Remove the matched key from zh_old
        else:
            # If no match is found, leave it empty
            zh_updated[en_key] = ""

# Marking outdated keys in zh_old with *outdated*
for key in zh_old:
    zh_updated[key] = "*outdated*" + zh_old[key]

# Write the updated translations to a new file
with open(lang_file, 'w', encoding='utf-8') as file:
    json.dump(zh_updated, file, ensure_ascii=False, indent=4)
