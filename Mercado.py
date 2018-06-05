from requests import get
from json import loads
import datetime
import time
class Accion:
    API3 = ''
    def __init__(self):
        with open('./token3.txt', 'rU') as f:
            self.API3 = f.readline()
            f.close()
    def valor(self, empresa):
        try:
            print('--Mercado.valor--')
            URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}&datatype=json".format(empresa, self.API3)
            response = loads(get(URL, timeout=3).text)
            dataForAllDays = response['Time Series (Daily)']
            for n in dataForAllDays:
                respuesta = dataForAllDays[n]
                fecha = n
                #print(f'dataForAllDays -> {n} -> {respuesta}')
                break
            cierre = respuesta['4. close']
            mensaje = f'Ultima cotización de {empresa} a fecha {fecha} es {cierre} USD'
            print(mensaje)
            with open('./Mercado.txt', 'a') as f:
                f.write(f'{datetime.datetime.now().time()} | Mercado:Accion Valor -> : {mensaje}\n')
            f.close()
            time.sleep(1)
            return(mensaje)
        except Exception as ex:
            time.sleep(1)
            with open('./Mercadoerror.txt', 'a') as f:
                f.write(f'{datetime.datetime.now().time()} | Mercado:Accion Valor -> empresa:{empresa} {ex}\n')
            f.close()
            print('No se pudo calcular el valor de {empresa}')
            return 'No se pudo calcular el valor de {empresa}'
def main():
    '''with open('./token3.txt') as f:
        API3 = ''
        API3 = f.readline()
    f.close()'''
    #print(f'API3 -> {API3}')
    C = Accion()
    C.valor('GOOGL')
    C.valor('MSFT')
    C.valor('abc')
    C.valor('error forzado')

if __name__ == '__main__':

    main()
