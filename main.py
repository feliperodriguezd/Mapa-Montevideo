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


file = open('paradas.json', encoding="utf8")
data = json.load(file)

for stop in data:
    xCoordinate = stop["location"]["coordinates"][0]
    yCoordinate = stop["location"]["coordinates"][1]
    plt.plot(xCoordinate, yCoordinate, 'go', color='red')

geoJSON = "montevideo.geojson"
map_data = gpd.read_file(geoJSON)
map_data.head()
map_data.plot(ax=ax, zorder=0, color='green')

plt.show()