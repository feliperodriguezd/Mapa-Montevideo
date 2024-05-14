import requests
import getToken
import json

url = "https://api.montevideo.gub.uy/api/transportepublico/buses?access_token=" + getToken.token 

payload = ''
headers = ''
response = requests.request("GET", url, headers=headers, data=payload)

dataInJson = json.loads(response.content)

print(dataInJson[0])