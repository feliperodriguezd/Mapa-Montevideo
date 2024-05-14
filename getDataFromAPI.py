import http.client
import tokens

conn = http.client.HTTPSConnection("api.montevideo.gub.uy")
payload = f'grant_type=client_credentials&client_id={tokens.clientID}&client_secret={tokens.secretClient}'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
conn.request("POST", "https://mvdapi-auth.montevideo.gub.uy/auth/realms/pci/protocol/openid-connect/token", payload, headers)
res = conn.getresponse()
data = res.read()
dataInString = data.decode("utf-8")
token = dataInString[17:dataInString.index('","expires_in"')]
print(token)