import json

file_name = "authors.json"
with open(file_name, "r") as fh:
    unpacked = json.load(fh)
for el in unpacked:
    print(el["description"])
