"""Scrape UN member states from Wikipedia and save them to countries.txt."""
import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"
HEADERS = {"User-Agent": "python-beyond-basics scraper"}


def scrape_countries() -> list[str]:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table", class_="wikitable")

    assert len(tables) < 2, "Found more than one table with class 'wikitable'"
    assert len(tables) > 0, "Could not find UN member states table with class 'wikitable'"

    table = tables[0]

    countries: list[str] = []
    for row in table.find_all("tr")[1:]:
        name = row.th.a.string

        countries.append(name)

    return countries


def save_countries(countries: list[str]) -> None:
    with open('countries.txt', "w", encoding="utf-8") as f:
        f.write("\n".join(countries))


if __name__ == "__main__":
    countries_list = scrape_countries()
    save_countries(countries_list)