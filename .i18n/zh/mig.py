import json

source_file = '.i18n/en/Game.json'
lang_file = '.i18n/zh/Game.json'
# Load the current lang.json
with open(lang_file, 'r', encoding='utf-8') as file:
    lang_data = json.load(file)


lang_data =  {key: lang_data[key] for key in sorted(lang_data.keys(), reverse=True)}

# Save the updated lang.json
with open(lang_file, 'w', encoding='utf-8') as file:
    json.dump(lang_data, file, ensure_ascii=False, indent=4)
