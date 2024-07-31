import requests
from bs4 import BeautifulSoup


def add_one(number):
    return number + 1


def get_google_title():
    response = requests.get("https://www.google.com")
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").text
    print(title)
    return title
