import pandas as pd
from Syslog import Syslog
import pandas as pd
from numpy import isnan
from Mercado import Accion
class Alerta:
    Log = Syslog()
    def listar(self, chatId):
        try:
            df = pd.read_csv('alertas.csv', sep=',',header=0)
            #print(df['empresa']['modificador']['precio'].where(df['chatId'] == chatId))
            df = df.loc[df['chatId'] == chatId]
            df = df[['Id','empresa','modificador','valor']]
            #print(df.to_string(index=False))
            array1 = []
            array = []
            narray = df.as_matrix()
            array1 = narray.flatten()
            print(array1)
            for i in range(0,len(array1),4):
                str = (f'id: {array1[i]} -> {array1[i+1]} {array1[i+2]} {array1[i+3]} ').upper()
                array.append(str)
                if i > len(array1):
                    break
            #array.strip('[')
            for i in range(len(array)):
                print(f'{i} -> {array[i]}')
            return array
        except Exception as ex:
            self.Log.errorlog(f"Alerta -> listar : chatId: {chatId} -> {ex}")
            print(f"Alerta -> listar : chatId: {chatId} -> {ex}")
    def borrar(self, chatId, Id):
        try:
            df = pd.read_csv('alertas.csv', sep=',',header=0)
            print(f'Id: {Id}, chatId: {chatId}')
            df1 = df
            df1 = df1[df1['Id'] == Id]
            df1 = df1[df1['chatId'] == chatId]
            print('borrado')
            print(df1)
            print(df)
            if df1.empty:
                return False
            df = df[df['Id'] != Id]
            self.Log.log(f"Alerta -> borrar : chatId: {chatId} id: {id} -> borrando {df1}")
            df.to_csv('alertas.csv',sep=',',encoding='utf-8',index=False)
            return True
        except Exception as ex:
            self.Log.errorlog(f"Alerta -> borrar : chatId: {chatId} id: {id} -> {ex}")
            print(f"Alerta -> borrar : chatId: {chatId} id: {id} -> {ex}")
            return False
    def borrar_todo(self, chatId):
        try:
            print('a borrar todo')
            df = pd.read_csv('alertas.csv', sep=',',header=0)
            print('antes')
            print(df)
            df = df[df['chatId'] != chatId]
            df.to_csv('alertas.csv',sep=',',encoding='utf-8',index=False)
            print('despues')
            print(df)
            return True
        except Exception as ex:
            self.Log.errorlog(f"Alerta -> borrar_todo : chatId: {chatId} -> {ex}")
            print(f"Alerta -> borrar_todo : chatId: {chatId} -> {ex}")
            return False
    def existe_alerta(self, chatId, empresa, modificador, valor):
        vexiste = True
        df = pd.read_csv('alertas.csv', sep=',',header=0)
        df = df[df['chatId'] == chatId]
        df = df[df['empresa'] == empresa]
        df = df[df['modificador'] == modificador]
        df = df[df['valor'] == valor]
        if df.empty:
            vexiste = False
        return vexiste
    def calculo(self):
        return True
    def add(self, chatId, empresa, modificador, valor):
        print(f'empresa {empresa} modificador {modificador} valor {valor}')
        C = Accion()
        if (((modificador == '<') | (modificador == '>')) & (type(valor) == int or type(valor) == float)&(C.cotizacion(empresa))):
            print('vamonos atomos')
            if self.existe_alerta(chatId, empresa, modificador, valor):
                return False
            else:
                try:
                    print('añadir')
                    df = pd.read_csv('alertas.csv', sep=',',header=0)
                    index = df['Id'].max()
                    print(f'index: {index}')
                    if isnan(index):
                        index = 0
                    print(index)
                    index = index + 1
                    df.loc[len(df)]=[index,chatId,empresa,modificador,valor]
                    df.to_csv('alertas.csv',sep=',',encoding='utf-8',index=False)
                    self.Log.log(f"Alerta -> add -> alerta añadida")
                    print(f"Alerta -> add -> alerta añadida")
                    return True
                except Exception as ex:
                    self.Log.errorlog(f"Alerta -> add -> {ex}")
                    print(f"Alerta -> add -> {ex} {repr(ex)}")
                    return False
        else:
            return False
    def comprobar(self):
        Empresas = []
        Cotizaciones = []
        df = pd.read_csv('alertas.csv', sep=',',header=0)
        Empresas = df.empresa.unique()
        print(Empresas)
        C = Accion()
        for i in range(len(Empresas)):
            Cotizaciones.append(C.precio(Empresas[i]))
        print(Cotizaciones)
        #resputsa chatId string alarma, string precio actual, id para borrar
        tam = len(df)
        Respuesta =[]
        p=0
        for i in range(len(Empresas)):
            print('$$$$$$$$$$$$$')
            df = pd.read_csv('alertas.csv', sep=',',header=0)
            df = df.loc[df['empresa'] == Empresas[i]]
            for j in range(len(df)):
                print(df.iloc[j])
                print('##################')
                print(f'Cotizaciones[i]: {Cotizaciones[i]}')
                print(f'df.iloc[j].modificador: {df.iloc[j].modificador}')
                print(f'df.iloc[j].valor: {df.iloc[j].valor}')
                if(df.iloc[j].modificador == '<'):
                    if(float(Cotizaciones[i])<float(df.iloc[j].valor)):
                        print('añadir alerta')
                        Respuesta.append([df.iloc[j].chatId,df.iloc[j].empresa,df.iloc[j].modificador,float(df.iloc[j].valor),float(Cotizaciones[i]),df.iloc[j].Id])
                    else:
                        print('no')
                else:
                    if(float(Cotizaciones[i])>float(df.iloc[j].valor)):
                        print('añadir alerta')
                        Respuesta.append([df.iloc[j].chatId,df.iloc[j].empresa,df.iloc[j].modificador,float(df.iloc[j].valor),float(Cotizaciones[i]),df.iloc[j].Id])
                    else:
                        print('no')
            p = p + 1
            df = pd.read_csv('alertas.csv', sep=',',header=0)
        #print('######RESPUESTA##########')
        #print(Respuesta)
        return Respuesta
def main():
    C = Alerta()
    '''
    array = []
    array =  C.listar(7457541)
    str = ''
    for i in range(len(array)):
        str = str + (f'{array[i]}\n')
    print(str)
    '''
    if C.add(7457541,'AAPL','<',2000):
        print('añadida')
    else:
        print('no añadida')
if __name__ == '__main__':
    main()