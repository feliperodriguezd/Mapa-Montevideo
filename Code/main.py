import getData
import getToken
import Exceptions
import createGraph

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
    createGraph.CreateFromGeojson('montevideoStreets', stopCoordinates)
    createGraph.ShowGraph()
else:
    print("No se encontro la parada deseada")