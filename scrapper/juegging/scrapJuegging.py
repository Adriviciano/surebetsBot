import requests
from bs4 import BeautifulSoup
from juegging.getMatchInfo import getMatchInfo

def scrap(url):
    allInfo=[]
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div that contains the matches
    matches_table = soup.find('ul', {'class': 'apuestas'})

    # Loop through each match and extract the team names and scores
    for match in matches_table.find_all('li', {'class': 'filtroCategoria'}):
        allInfo.append(getMatchInfo(match))
    return allInfo
