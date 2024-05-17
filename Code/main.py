import getData
import getToken
import Exceptions
import createGraph
import json


def whichSectionsGenerate(stopCoordinates):
    sections = []
    xCoordinate = stopCoordinates[0]
    xCoordinatePlus = xCoordinate + 0.03
    xCoordinateMinus = xCoordinate - 0.03
    for num in range(10, 0, -1):
        data = open(f'Code/Data/Montevideo/{str(num)}.geojson', encoding="utf8")
        dataJson = json.load(data)
        dataJsonLen = len(dataJson['features'])
        coordinateMinus = dataJson['features'][0]['geometry']['coordinates'][0][0]
        coordinateMax = dataJson['features'][dataJsonLen-1]['geometry']['coordinates'][0][0]
        if coordinateMinus < xCoordinatePlus < coordinateMax:
            sections.append(num)
        elif coordinateMinus < xCoordinateMinus < coordinateMax:
            sections.append(num)
    return sections

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
    createGraph.CreateFromJson(stop, 'blue')
    createGraph.CreateFromJson(nextBusesOfStop, 'red')
    print('Generando mapa de Montevideo')
    stopCoordinates = stop[0]['location']['coordinates']
    sections = whichSectionsGenerate(stopCoordinates) 
    createGraph.CreateFromGeojson('montevideoStreets', stopCoordinates)
    createGraph.ShowGraph()
else:
    print("No se encontro la parada deseada")