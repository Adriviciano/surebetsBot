import re

def getMatchInfo(match):
    pattern = r'([A-Za-zÁÉÍÓÚáéíóúÑñ ]+) vs. ([A-Za-zÁÉÍÓÚáéíóúÑñ ]+)'

    texto = match.find('span', {'class': 'partido'}).text
    if not texto.__contains__("División"):
        n = re.search(pattern, texto)
        nombres = []
        precios = []
        nombres.append(n.group(1))
        nombres.append("X")
        nombres.append(n.group(2))
        for cuota in match.find_all('p', {'class': 'tipe1'}):
            precio = cuota.find('span', {'class': 'coef'}).text
            precios.append(precio)
        return nombres[0]+":"+precios[2]+"/"+nombres[1]+":"+precios[3]+"/"+nombres[2]+":"+precios[4]