import csv
import json
from pprint import pprint

with open("data/input.csv") as file:
    reader = csv.DictReader(file)
    data = list(reader)          # Convert to a list of dicts


with open("data/output.json", "w") as file:
    json.dump(data, file)        # Write data directly to a file


with open("data/output.json") as file:
    data = json.load(file)       # Read data directly from a file
    pprint(data)                 # pprint (pretty-print) adds newlines and indentation


with open("data/output.json", "w") as file:
    json_str = json.dumps(data)  # Convert data to str
    print(json_str)
    file.write(json_str)         # Write str to file


with open("data/output.json") as file:
    contents = file.read()       # Read data as str
    data = json.loads(contents)  # Convert str to objects
    pprint(data)                 # Pretty print data
