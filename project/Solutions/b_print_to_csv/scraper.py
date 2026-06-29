"""Scrape UN member states from Wikipedia and save them to countries.txt."""

import csv

import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"
HEADERS = {"User-Agent": "python-beyond-basics scraper"}


def scrape_countries() -> list[dict[str, str]]:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table", class_="wikitable")

    assert len(tables) < 2, "Found more than one table with class 'wikitable'"
    assert len(tables) > 0, "Could not find UN member states table with class 'wikitable'"

    table = tables[0]

    countries: list[dict[str, str]] = []
    for row in table.find_all("tr")[1:]:
        name = row.th.a.string
        date_joined = row.td.span.string
        country = {
            "Name": name,
            "Date Joined": date_joined,
        }
        countries.append(country)

    return countries


def save_countries(countries: list[dict[str, str]]) -> None:
    with open('countries.csv', "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Date Joined"])
        writer.writeheader()
        writer.writerows(countries)


if __name__ == "__main__":
    countries_list = scrape_countries()
    save_countries(countries_list)