
class Alerta:
    def __init__(self):
        with open('./token2.txt', 'rU') as f:
            self.api = f.readline()
            #print(f'API2-> {self.api}')
        f.close()