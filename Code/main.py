import matplotlib.pyplot as plt
import geopandas as gpd
import getData
import getToken
import Exceptions

def draw_line(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.plot(x_values, y_values, marker='o')

def CreateMapFromJson(data, color):
    for singleData in data:
        xCoordinate = singleData["location"]["coordinates"][0]
        yCoordinate = singleData["location"]["coordinates"][1]
        if xCoordinate < -55.9 and xCoordinate > -56.5:
            if yCoordinate < -34.7 and yCoordinate > -34.95:
                plt.plot(xCoordinate, yCoordinate, 'o', color=color)

def CreateMapFromGeojson(name, stopCoordinates):
    geoJSONMontevideo = f"Code/Data/{name}.geojson"
    montevideo = gpd.read_file(geoJSONMontevideo)
    data = gpd.GeoDataFrame.from_features(montevideo)
    print('Listo carga de datos')
    for feature in data.iterfeatures():
        coordinate = feature['geometry']['coordinates']
        points = []
        for cor in coordinate:
            if cor[0] < stopCoordinates[0] + 0.03 and cor[0] > stopCoordinates[0] - 0.03:
                if cor[1] < stopCoordinates[1] + 0.03 and cor[1] > stopCoordinates[1] - 0.03:
                    points.append((cor[0], cor[1]))
        if len(coordinate) == len(points):
            draw_line(points)


def CreateAllMapFromGeojson(name):
    geoJSONMontevideo = f"Code/Data/{name}.geojson"
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