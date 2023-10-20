import json

with open('tt100k2016_part/annotations.json', 'rb') as fp:
    data = json.load(fp)

print(type(data))
print(data.keys())

# re_store json file with
with open('./annotations_tt100k2016_formated.json', 'w') as fp:
    json.dump(data, fp, indent=4, sort_keys=True, ensure_ascii=False)

