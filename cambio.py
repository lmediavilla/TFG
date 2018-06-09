# coding utf-8
from requests import get
from json import loads
from socket import timeout
import datetime
from Syslog import Syslog

class Bolsa:
    api = ''
    Log = Syslog()
    def __init__(self):
        with open('./token2.txt', 'rU') as f:
            self.api = f.readline()
            #print(f'API2-> {self.api}')
            f.close()
    def cambio(self, moneda1, moneda2):
        ###debug###
        #print((f'{moneda1} and {moneda2}'))
        #print(f'FORGE API KEY: {self.api}')
        try:
            ###con timeout de 2 segundo###
            URL = "https://forex.1forge.com/1.0.3/convert?from={}&to={}&quantity=1&api_key={}".format(moneda1, moneda2, self.api)
            response = loads(get(URL, timeout=3).text)
            valor = response['value']
            fecha = datetime.datetime.fromtimestamp(int(response['timestamp'])).strftime('%d-%m-%Y %H:%M:%S')
            self.Log.log(f"Bolsa -> cambio : {moneda1} equivale a {valor} {moneda2} fecha del valor {fecha}")
            print(f"Bolsa -> cambio : {moneda1} equivale a {valor} {moneda2} fecha del valor {fecha}")
            return (f'1 {moneda1} equivale a {valor} {moneda2} \n fecha del valor {fecha}')
        except  Exception as ex:
            self.Log.errorlog(f"Bolsa -> cambio : moneda 1:{moneda1} moneda2:{moneda2} {ex}")
            print(f"Bolsa -> cambio : moneda 1:{moneda1} moneda2:{moneda2} {ex}")
            return "Error: no podimos gestionar su peticion"

##para testear sin funcionar telegram###
def main():
        c = Bolsa()
        print(c.cambio('BTC', 'EUR'))
        print(c.cambio('USD', 'EUR'))
        print(c.cambio('GBP', 'EUR'))
        print(c.cambio('ABC', 'CDE'))
        print(c.cambio('BTC', 'EUR'))
        print(c.cambio('USD', 'EUR'))
        print(c.cambio('GBP', 'EUR'))
        print(c.cambio('ABC', 'CDE'))



if __name__ == '__main__':
    main()