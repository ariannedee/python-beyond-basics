"""Scrape UN member states from Wikipedia and save them to countries.txt."""

import csv

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://en.wikipedia.org"
URL = BASE_URL + "/wiki/Member_states_of_the_United_Nations"
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
        url = row.th.a['href']
        country = {
            "Name": name,
            "Date Joined": date_joined,
            "URL": url,
        }
        countries.append(country)

    return countries


def get_country_data(countries: list[dict[str, str]]) -> list[dict[str, str]]:
    for country in countries[:3]:
        country_url = f"{BASE_URL}{country['URL']}"
        response = requests.get(country_url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        latitude = soup.find("span", class_="latitude").string
        longitude = soup.find("span", class_="longitude").string
        if latitude is None or longitude is None:
            print(f"Could not find latitude or longitude for {country['Name']}")
            continue
        country["Latitude"] = latitude
        country["Longitude"] = longitude

    return countries

def save_countries(countries: list[dict[str, str]]) -> None:
    with open('countries_more.csv', "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Date Joined", "Latitude", "Longitude", "URL"])
        writer.writeheader()
        writer.writerows(countries)


if __name__ == "__main__":
    countries_list = scrape_countries()
    countries_list = get_country_data(countries_list)
    save_countries(countries_list)