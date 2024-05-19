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

def busesListToString(busesOfStop):
    busesOfStopToList = []
    for bus in busesOfStop:
        busesOfStopToList.append(bus['line'])
    busesOfStopInString = ",".join(str(elem) for elem in busesOfStopToList)
    return busesOfStopInString