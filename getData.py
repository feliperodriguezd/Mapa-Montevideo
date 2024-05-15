import requests
import getToken
import json


def UpdateDataBuses():
    url = "https://api.montevideo.gub.uy/api/transportepublico/buses?access_token=" + getToken.token 

    payload = ''
    headers = ''
    response = requests.request("GET", url, headers=headers, data=payload)

    dataInJson = json.loads(response.content)

    with open('Data/omnibus.json', 'w') as fp:
        json.dump(dataInJson, fp)