import json
import Exceptions

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
        if xCoordinateMinus < coordinateMinus < xCoordinatePlus:
            sections.append(num)
        elif xCoordinateMinus < coordinateMax < xCoordinatePlus:
            sections.append(num)
    return sections

def busesListToString(busesOfStop):
    busesOfStopToList = []
    for bus in busesOfStop:
        busesOfStopToList.append(bus['line'])
    busesOfStopInString = ",".join(str(elem) for elem in busesOfStopToList)
    return busesOfStopInString

def EstaEnCalle(parada, calle):
    try:
        return parada.find(calle) != -1
    except:
        return False

def GetStop():
    data = open(f'Code/Data/paradas.json', encoding="utf8")
    dataJson = json.load(data)
    print('¿En que calles esta para parada que busca?')
    street1 = input("Calle 1: ").upper()
    street2 = input("Calle 2: ").upper()

    posibleBusStops = []
    for stop in dataJson:
        if EstaEnCalle(stop['street1'], street1) or EstaEnCalle(stop['street2'], street1):
            if EstaEnCalle(stop['street1'], street2) or EstaEnCalle(stop['street2'], street2):
                posibleBusStops.append(stop)
    
    if len(posibleBusStops) > 1:
        print('¿A cual se refiere?')
        count = 1
        for stop in posibleBusStops:
            print(f'{str(count)}: Parada en : ' + stop['street1'] + ' y '  + stop['street2'])
            count += 1
        option = int(input("Opcion: "))
        return posibleBusStops[option-1]
    elif len(posibleBusStops) == 1:
        return posibleBusStops[0]
    else:
        raise Exceptions.NoBusStopFound