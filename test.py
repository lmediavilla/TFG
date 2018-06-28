import pandas as pd
from Mercado import Accion


def main():
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
    print('######RESPUESTA##########')
    print(Respuesta)
if __name__ == '__main__':
    main()