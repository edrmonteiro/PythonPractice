from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())

temperature = soup.find("span", id="current-weather-temperature")

print(temperature.string)