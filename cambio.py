# coding utf-8
from requests import get
from json import loads
from socket import timeout
import datetime


class Bolsa:
    def __init__(self, API):
        self.api = API

    def cambio(self, moneda1, moneda2):
        ###debug###
        #print((f'{moneda1} and {moneda2}'))
        #print(f'FORGE API KEY: {self.api}')
        try:
            ###con timeout de 1 segundo###
            URL = "https://forex.1forge.com/1.0.3/convert?from={}&to={}&quantity=1&api_key={}".format(moneda1, moneda2, self.api)
            response = loads(get(URL, timeout=1).text)
            valor = response['value']
            fecha = datetime.datetime.fromtimestamp(int(response['timestamp'])).strftime('%d-%m-%Y %H:%M:%S')
            return (f'1 {moneda1} equivale a {valor} {moneda2} \n fecha del valor {fecha}')
        except:
            return "Error: no podimos gestionar su peticion"

##para testear sin funcionar telegram###
def main():
        with open('token2.txt') as f:
            API2 = f.readline()
        print(f'API2: {API2}')
        c = Bolsa(API2)
        print(c.cambio('BTC', 'EUR'))
        print(c.cambio('USD', 'EUR'))
        print(c.cambio('GBP', 'EUR'))


if __name__ == '__main__':
    main()