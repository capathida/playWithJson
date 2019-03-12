import json


with open('data/SWE2019.json', errors='ignore', encoding='utf-8') as json_file:  
    data = json.load(json_file)

print(data)