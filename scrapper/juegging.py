import requests
from bs4 import BeautifulSoup
import re

patron = r'([A-Za-zÁÉÍÓÚáéíóúÑñ ]+) vs. ([A-Za-zÁÉÍÓÚáéíóúÑñ ]+)'

# URL of the page to scrape
url = 'https://apuestas.juegging.es/esp/Sport/Deporte/40/ESP'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div that contains the matches
matches_table = soup.find('ul', {'class': 'apuestas'})

# Loop through each match and extract the team names and scores
for match in matches_table.find_all('li', {'class': 'filtroCategoria'}):
   texto = match.find('span', {'class': 'partido'}).text
   if texto.__contains__("División"):
      break
   n = re.search(patron, texto)
   nombres = []
   precios = []
   nombres.append(n.group(1))
   nombres.append("X")
   nombres.append(n.group(2))
   for cuota in match.find_all('p', {'class': 'tipe1'}):
      precio = cuota.find('span', {'class': 'coef'}).text
      precios.append(precio)
   print(f'{nombres[0]} {precios[2]} / {nombres[1]} {precios[3]} / {nombres[2]} {precios[4]}')
