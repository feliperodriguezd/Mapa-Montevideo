import requests
import json
import Exceptions


def GeteAllBuses(token):
    url = "https://api.montevideo.gub.uy/api/transportepublico/buses?access_token=" + token 

    payload = ''
    headers = ''
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        dataInJson = json.loads(response.content)
    else:
        raise Exceptions.APIError

    with open('Data/omnibus.json', 'w') as fp:
        json.dump(dataInJson, fp)


def GetNextBusesOfStop(stop, lines, token):
    url = f"https://api.montevideo.gub.uy/api/transportepublico/buses/busstops/{stop}/upcomingbuses?lines={lines}&access_token=" + token 

    payload = ''
    headers = ''
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        dataInJson = json.loads(response.content)
    else:
        raise Exceptions.APIError
    return dataInJson


def GetLinesOfStop(stop, token):
    url = f"https://api.montevideo.gub.uy/api/transportepublico/buses/busstops/{stop}/lines?&access_token=" + token 

    payload = ''
    headers = ''
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        dataInJson = json.loads(response.content)
    else:
        raise Exceptions.APIError

    return dataInJson