# Scraping Real Websites - I

import requests
from bs4 import BeautifulSoup
response = requests.get("http://info.cern.ch/hypertext/WWW/TheProject.html")
print(response.status_code)
print(response)
data = BeautifulSoup(response.text,'html.parser')
print(data.get_text())
print(data.title.string)
print(data.a['href'])
