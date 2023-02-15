import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://betway.es/es/sports/grp/soccer/spain/la-liga'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)

# Find the div that contains the matches
matches_table = soup.find('div', {'class': ''})
i=0
# Loop through each match and extract the team names and scores
for match in matches_table.find_all('div', {'class': 'cf-main-wrapper'}):
   nombres1 = [] #i*2-1
   nombres2 = [] #2*i
   precios = []
   for cuota in match.find_all('div', {'class': 'sgl-ParticipantOddsOnly80'}):
      precio = cuota.find('span', {'class': ''})
      precios.append(precio.text)
      print(f'{precios[i]}')
      i+=1

#print(f'{nombres[0]} {precios[0]} / {nombres[1]} {precios[1]} / {nombres[2]} {precios[2]}')

