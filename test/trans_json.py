import json
with open('test/test_file.json', 'rb') as f:
    d = json.load(f)
print(d)