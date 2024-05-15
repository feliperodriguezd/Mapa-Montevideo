import matplotlib.pyplot as plt
import geopandas as gpd
import json
import getData

def CreateMapFromJson(name, color):
    data = open(f'Data/{name}.json', encoding="utf8")
    dataJson = json.load(data)

    for singleData in dataJson:
        xCoordinate = singleData["location"]["coordinates"][0]
        yCoordinate = singleData["location"]["coordinates"][1]
        if xCoordinate < -55.9 and xCoordinate > -56.5:
            if yCoordinate < -34.7 and yCoordinate > -34.95:
                plt.plot(xCoordinate, yCoordinate, 'go', color=color)


def CreateMapFromGeojson(name):
    geoJSONMontevideo = f"Data/{name}.geojson"
    montevideo = gpd.read_file(geoJSONMontevideo)
    montevideo.head()
    montevideo.plot(ax=ax, zorder=0, color='green')    


# Control del tamaño de la figura del mapa
fig, ax = plt.subplots(figsize=(10, 10))
    
# Control del título y los ejes
ax.set_title('Mapa de montevideo', 
            pad = 20, 
            fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')


getData.UpdateDataBuses()
CreateMapFromJson('omnibus', 'red')
CreateMapFromJson('paradas', 'blue')
CreateMapFromGeojson('montevideoStreets')

plt.show()