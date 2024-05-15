import matplotlib.pyplot as plt
import geopandas as gpd
import getData
import getToken
import Exceptions

def CreateMapFromJson(data, color):
    for singleData in data:
        xCoordinate = singleData["location"]["coordinates"][0]
        yCoordinate = singleData["location"]["coordinates"][1]
        if xCoordinate < -55.9 and xCoordinate > -56.5:
            if yCoordinate < -34.7 and yCoordinate > -34.95:
                plt.plot(xCoordinate, yCoordinate, 'o', color=color)


def CreateMapFromGeojson(name):
    geoJSONMontevideo = f"Data/{name}.geojson"
    montevideo = gpd.read_file(geoJSONMontevideo)
    montevideo.head()
    montevideo.plot(ax=ax, zorder=0, color='green')    


# Definir el formato del mapa
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title('Mapa omnibus', 
            pad = 20, 
            fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')

try:
    token = getToken.token
    print('Recopliando lineas de la parada')
    busesOfStop = getData.GetLinesOfStop('5615', token)

    busesOfStopToList = []

    for bus in busesOfStop:
        busesOfStopToList.append(bus['line'])

    busesOfStopInString = ",".join(str(elem) for elem in busesOfStopToList)

    print('Recopliando proximos omnibus')
    nextBusesOfStop = getData.GetNextBusesOfStop('5615', busesOfStopInString, token)
except Exceptions.APIError:
    print("Error al intentar recuparar los datos de la api")

stop = [getData.GetStop(5615)]

if stop != False:
    print('Generando mapa')
    CreateMapFromJson(stop, 'blue')
    CreateMapFromJson(nextBusesOfStop, 'red')
    print('Generando mapa de Montevideo')
    CreateMapFromGeojson('montevideoStreets')
else:
    print("No se encontro la parada deseada")

plt.show()