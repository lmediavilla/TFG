from requests import get
from json import loads
import datetime
import time
from Syslog import Syslog
class Accion:
    API3 = ''
    Log = Syslog()
    def __init__(self):
        with open('./token3.txt', 'rU') as f:
            self.API3 = f.readline()
            #para linux
            self.API3 = self.API3.rstrip('\n')
            f.close()
    def cotizacion(self, empresa):
        try:
            URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}&datatype=json".format(empresa, self.API3)
            response = loads(get(URL, timeout=3).text)
            dataForAllDays = response['Time Series (Daily)']
            for n in dataForAllDays:
                respuesta = dataForAllDays[n]
                fecha = n
                #print(f'dataForAllDays -> {n} -> {respuesta}')
                break
            cierre = respuesta['4. close']
            return True
        except:
            return False
    def precio(self, empresa):
        try:
            URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}&datatype=json".format(empresa, self.API3)
            response = loads(get(URL, timeout=3).text)
            dataForAllDays = response['Time Series (Daily)']
            for n in dataForAllDays:
                respuesta = dataForAllDays[n]
                fecha = n
                #print(f'dataForAllDays -> {n} -> {respuesta}')
                break
            cierre = respuesta['4. close']
            return cierre
        except:
            return -1
    def valor(self, empresa):
        try:
            #print('--Mercado.valor--')
            URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}&datatype=json".format(empresa, self.API3)
            response = loads(get(URL, timeout=3).text)
            dataForAllDays = response['Time Series (Daily)']
            for n in dataForAllDays:
                respuesta = dataForAllDays[n]
                fecha = n
                #print(f'dataForAllDays -> {n} -> {respuesta}')
                break
            cierre = respuesta['4. close']
            mensaje = f'Ultima cotización de *{empresa}* a fecha {fecha} es *{cierre}* USD'
            print(mensaje)
            self.Log.log(f"Accion -> valor : Ultima cotización de {empresa} a fecha {fecha} es {cierre} USD")
            time.sleep(1)
            return(mensaje)
        except Exception as ex:
            time.sleep(1)
            self.Log.errorlog(f"Accion -> valor : empresa: {empresa} -> {ex}")
            print('No se pudo calcular el valor de {empresa}')
            return 'error'
def main():
    C = Accion()
    C.valor('TEF')
    C.valor('MSFT')
    C.valor('abc')
    C.valor('error forzado')

if __name__ == '__main__':

    main()
