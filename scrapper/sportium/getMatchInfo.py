def getMatchInfo(match):
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
    return nombres[0]+":"+precios[0]+"/"+nombres[1]+":"+precios[1]+"/"+nombres[2]+":"+precios[2]