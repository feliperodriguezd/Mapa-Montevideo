import matplotlib.pyplot as plt
import geopandas as gpd
import getData
import getToken
import Exceptions

def draw_line(points):
    xValues = [point[0] for point in points]
    yValues = [point[1] for point in points]
    plt.plot(xValues, yValues, color='green')

def IsInsideMontevideo(XorY, coordinate):
    if XorY == 'x':
        return coordinate < -55.9 and coordinate > -56.5
    else:
        return coordinate < -34.7 and coordinate > -34.95

def CreateFromJson(data, color):
    for singleData in data:
        xCoordinate = singleData["location"]["coordinates"][0]
        yCoordinate = singleData["location"]["coordinates"][1]
        if IsInsideMontevideo('x', xCoordinate):
            if IsInsideMontevideo('y', yCoordinate):
                plt.plot(xCoordinate, yCoordinate, 'o', color=color)

def IsNearStop(stopCoordinate, compareCoordinate):
    return compareCoordinate < stopCoordinate + 0.03 and compareCoordinate > stopCoordinate - 0.03

def AllThePointsAreNear(coordinate, points):
    return len(coordinate) == len(points)

def CreateFromGeojson(name, stopCoordinates):
    geoJSONMontevideo = f"Code/Data/{name}.geojson"
    montevideo = gpd.read_file(geoJSONMontevideo)
    data = gpd.GeoDataFrame.from_features(montevideo)
    print('Listo carga de datos de Montevideo')
    for feature in data.iterfeatures():
        coordinate = feature['geometry']['coordinates']
        points = []
        for cor in coordinate:
            if IsNearStop(stopCoordinates[0], cor[0]):
                if IsNearStop(stopCoordinates[1], cor[1]):
                    points.append((cor[0], cor[1]))
        if AllThePointsAreNear(coordinate, points):
            draw_line(points)


def CreateAllFromGeojson(name):
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
    CreateFromJson(stop, 'blue')
    CreateFromJson(nextBusesOfStop, 'red')
    print('Generando mapa de Montevideo')
    stopCoordinates = stop[0]['location']['coordinates']
    CreateFromGeojson('montevideoStreets', stopCoordinates)
else:
    print("No se encontro la parada deseada")

plt.show()