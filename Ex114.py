# 114

import requests

while True:
    try:
        requests.head('http://pudim.com.br/').status_code
        print('O site está acessível.')
    except requests.RequestException:
        print('O site não está acessível.')
    break