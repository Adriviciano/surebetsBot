import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://sports.sportium.es/es/t/45211/La-Liga'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div that contains the matches
matches_table = soup.find('table', {'class': 'coupon'})

# Loop through each match and extract the team names and scores
for match in matches_table.find_all('tr', {'class': 'mkt'}):
   nombres = []
   precios = []
   for cuota in match.find_all('td', {'class': 'seln'}):
      nombre = cuota.find('span', {'class': 'seln-name'})
      precio = cuota.find('span', {'class': 'dec'})
      precios.append(precio.text)
      if nombre != None:
         nombres.append(nombre.text)
      else:
         nombres.append("X")
   print(f'{nombres[0]} {precios[0]} / {nombres[1]} {precios[1]} / {nombres[2]} {precios[2]}')

