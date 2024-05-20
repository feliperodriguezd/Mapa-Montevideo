import getData
import Exceptions
import createGraph
import AuxiliaryFunctions as AF
import getToken

if __name__ == '__main__':
    try:
        token = getToken.GetToken()
        print('Recopliando lineas de la parada')
        stop = AF.GetStop()
        busesOfStop = getData.GetLinesOfStop(str(stop['busstopId']), token)
        busesOfStopInString = AF.busesListToString(busesOfStop)

        print('Recopliando proximos omnibus')
        nextBusesOfStop = getData.GetNextBusesOfStop(str(stop['busstopId']), busesOfStopInString, token)

        stop = [stop]

        if stop != False:
            print('Generando mapa')
            stopCoordinates = stop[0]['location']['coordinates']
            createGraph.CreateFromJson(stop, stopCoordinates, 'blue')
            createGraph.CreateFromJson(nextBusesOfStop, stopCoordinates, 'red')
            print('Generando mapa de Montevideo')
            sections = AF.whichSectionsGenerate(stopCoordinates) 
            for section in sections:
                createGraph.CreateFromGeojson(f'Montevideo/{str(section)}', stopCoordinates)
            createGraph.ShowGraph()
        else:
            print("No se encontro la parada deseada")
            
    except Exceptions.APIError:
        print("Error al intentar recuparar los datos de la api")
    except Exceptions.APITokenError:
        print("Error al intentar conseguir el token para acceder a los datos de la api")
    except Exceptions.NoBusStopFound:
        print("No se encontro parada en esas calles")
    except Exception as error:
        print(error)

