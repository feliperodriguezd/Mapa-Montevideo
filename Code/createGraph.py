import matplotlib.pyplot as plt
import geopandas as gpd

# Definir el formato del mapa
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title('Mapa omnibus', 
            pad = 20, 
            fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')

def draw_line(points):
    xValues = [point[0] for point in points]
    yValues = [point[1] for point in points]
    plt.plot(xValues, yValues, zorder=0, color='green')

def IsInsideMontevideo(XorY, coordinate):
    if XorY == 'x':
        return coordinate < -55.9 and coordinate > -56.5
    else:
        return coordinate < -34.7 and coordinate > -34.95

def CreateFromJson(data, stopCoordinates , color):
    for singleData in data:
        xCoordinate = singleData["location"]["coordinates"][0]
        yCoordinate = singleData["location"]["coordinates"][1]
        if IsInsideMontevideo('x', xCoordinate):
            if IsInsideMontevideo('y', yCoordinate):
                if IsNearStop(stopCoordinates[0], xCoordinate):
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

def ShowGraph():
    plt.show()