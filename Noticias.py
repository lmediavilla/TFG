# coding utf-8
import feedparser


class Noticias:
    def __init__(self):
        self.URLa = 'http://estaticos.expansion.com/rss/mercados.xml'
        self.URLb = 'https://cincodias.elpais.com/seccion/rss/mercados/'
        self.URLc = 'http://www.abc.es/rss/feeds/abc_Economia.xml'
        self.URLd = 'http://www.eleconomista.es/rss/rss-flash-del-mercado.php'

    def rss(self, url):
        try:
            URL = ''
            #print(f'MODULO: NOTICIAS -> url -> {url}')
            if int(url) == 1:
                URL = self.URLa
                rss = feedparser.parse(URL)
                array = []
                for i in range(0, 10):
                    #print(f'i: {i} {rss.entries[i].link}')
                    array.append(rss.entries[i].link)
                #print(array)
                return array
            elif int(url) == 2:
                URL = self.URLb
                rss = feedparser.parse(URL)
                array = []
                for i in range(0, 10):
                    #print(f'i: {i} {rss.entries[i].link}')
                    array.append(rss.entries[i].link)
                #print(array)
                return array
            elif int(url) == 3:
                URL = self.URLc
                rss = feedparser.parse(URL)
                array = []
                for i in range(0, 10):
                    #print(f'i: {i} {rss.entries[i].link}')
                    array.append(rss.entries[i].link)
                #print(array)
                return array
            elif int(url) == 4:
                URL = self.URLd
                rss = feedparser.parse(URL)
                array = []
                for i in range(0, 10):
                    #print(f'i: {i} {rss.entries[i].link}')
                    array.append(rss.entries[i].link)
                #print(array)
                return array
            else:
                array = []
                array.append('No tenemos ese valor en las noticias')
                return array
        except Exception as ex:
            print(ex)


##para testear sin funcionar telegram###
def main():
    C = Noticias()
    print(C.rss(1))
    print(C.rss(2))
    print(C.rss(3))
    print(C.rss(4))


if __name__ == '__main__':
    main()
