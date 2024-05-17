import http.client
import credentials
import json

connection = http.client.HTTPSConnection("api.montevideo.gub.uy")
payload = f'grant_type=client_credentials&client_id={credentials.clientID}&client_secret={credentials.secretClient}'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
connection.request("POST", "https://mvdapi-auth.montevideo.gub.uy/auth/realms/pci/protocol/openid-connect/token", payload, headers)

response = connection.getresponse()

if response.status == 200:
    data = response.read()
    dataInJson = json.loads(data)
    token = dataInJson['access_token']
else:
    print("Error al acceder a la api")