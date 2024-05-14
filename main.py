import geopandas as gpd
import matplotlib.pyplot as plt
import json


# Control del tamaño de la figura del mapa
fig, ax = plt.subplots(figsize=(10, 10))
 
# Control del título y los ejes
ax.set_title('Mapa de montevideo', 
             pad = 20, 
             fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')


paradas = open('Data/paradas.json', encoding="utf8")
paradasData = json.load(paradas)

for stop in paradasData:
    xCoordinate = stop["location"]["coordinates"][0]
    yCoordinate = stop["location"]["coordinates"][1]
    plt.plot(xCoordinate, yCoordinate, 'go', color='#14CBDD')

omnibus = open('Data/omnibus.json', encoding="utf8")
omnibusData = json.load(omnibus)

for stop in omnibusData:
    xCoordinate = stop["location"]["coordinates"][0]
    yCoordinate = stop["location"]["coordinates"][1]
    if xCoordinate < -55.9 and xCoordinate > -56.5:
        if yCoordinate < -34.7 and yCoordinate > -34.95:
            plt.plot(xCoordinate, yCoordinate, 'go', color='#DD14D1')

geoJSONMontevideo = "Data/montevideo.geojson"
montevideo = gpd.read_file(geoJSONMontevideo)
montevideo.head()
montevideo.plot(ax=ax, zorder=0, color='green')

geoJSONDirecciones = "Data/direcciones.geojson"
direcciones = gpd.read_file(geoJSONDirecciones)
direcciones.head()
direcciones.plot(ax=ax, zorder=0, color='red')

plt.show()