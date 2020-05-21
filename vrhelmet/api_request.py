import requests
import pprint

#response = requests.get('http://127.0.0.1:8000/api/v0/helmets/', auth=('anastasia', 'honyak79'))
#
# pprint.pprint(response.json())

token = '4a9558be9158c3babc79d753baf13e2be240b34c'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/helmets/', headers=headers)
#response = requests.get('http://127.0.0.1:8000/api/v0/helmets/')
pprint.pprint(response.json())