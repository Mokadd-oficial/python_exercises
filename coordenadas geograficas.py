#Coordenadas Geográficas
#o Crie uma tupla que represente as coordenadas geográficas
#(latitude, longitude) de uma cidade. Mostre essas coordenadas de
#forma formatada.

tCoor = (25.36, -36.89)
sufLat = "S"
sufLon = "o"

if tCoor[0] > 0:
    sufLad = "N"

if tCoor[1] > 0:
    sufLad = "N"
print(f'''Latitude:{abs(tCoor[0])} {sufLat}
Longitude:{abs(tCoor[1])} {sufLat}''')
