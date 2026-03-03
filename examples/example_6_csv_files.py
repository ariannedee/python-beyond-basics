import csv

with open("data/input.csv", "r") as file:
    reader = csv.DictReader(file)

    for country in reader:
        print(f'The capital of {country["Country"]} is {country["Capital"]}')
