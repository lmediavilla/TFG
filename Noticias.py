# coding utf-8
import feedparser
import pandas as pd
import datetime

class Noticias:

    def rss(self, url):
        try:
            df=pd.read_csv('rss.txt', sep=',',header=0)
            #print(df.values)
            #print(f'url -> {url}')
            col = list(df['url'].values)
            #print(f'col -> {col}')
            #print(f'col[url] -> {col[int(url)]}')
            #print(f'debug col: \n {col[url]}')
            rss = feedparser.parse(col[int(url)])
            #print(f'rss -> {rss}')
            array = []
            for i in range(0, 10):
                #print(f'i: {i} {rss.entries[i].link}')
                array.append(rss.entries[i].link)
            print(f'array -> {array}')
            return array
        except Exception as ex:
            print(f'Noticias: rss -> {datetime.datetime.now().time()}: {ex}')
    def longitud(self):
        try:
            num_lines = sum(1 for line in open('rss.txt'))
            return num_lines
        except Exception as ex:
            print(ex)
    def lista(self):
        try:
            df=pd.read_csv('rss.txt', sep=',',header=0)
            col = list(df['nombre'].values)
            #print(f'debug col: \n {col}')
            array = []
            array = list(col)
            return array
        except Exception as ex:
            print(f'Noticias: lista -> {datetime.datetime.now().time()}: {ex}')



##para testear sin funcionar telegram###
def main():
    C = Noticias()
    #print(C.lista())
    print(C.rss(2))


if __name__ == '__main__':
    main()
