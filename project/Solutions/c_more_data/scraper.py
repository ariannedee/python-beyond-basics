import csv

import requests

from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org"
URL = BASE_URL + "/wiki/Member_states_of_the_United_Nations"
HEADERS = {"User-Agent": "<Your name here>"}


def scrape_countries() -> list[dict[str, str]]:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="wikitable")
    if table is None:
        raise RuntimeError("Could not find countries table on the page")

    countries: list[dict[str, str]] = []

    for row in table.find_all("tr")[1:]:  # Skip header row
        country_cell = row.th

        link = country_cell.a
        name = link.text

        country_dict = {
            "Name": name,
            "URL": link["href"],
        }
        countries.append(country_dict)

    return sorted(countries, key=lambda c: c["Name"])


def scrape_country_page(country_dict: dict) -> None:
    response = requests.get(BASE_URL + country_dict["URL"], headers=HEADERS)

    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    lat = soup.find("span", class_="latitude").string
    lon = soup.find("span", class_="longitude").string
    country_dict["Latitude"] = lat
    country_dict["Longitude"] = lon


def save_countries(countries: list[dict]) -> None:
    with open("countries.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=("Name", "URL", "Latitude", "Longitude"))
        writer.writeheader()
        writer.writerows(countries)


if __name__ == "__main__":
    countries_list = scrape_countries()
    for country in countries_list[:2]:
        scrape_country_page(country)
    save_countries(countries_list)
    print(f"Saved {len(countries_list)} countries to countries.txt")
