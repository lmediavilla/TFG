import time
class Syslog:
    def log(self, log):
        try:
            fecha = time.asctime(time.localtime(time.time()))
            with open('./log.txt', 'a') as f:
                f.write(f'{fecha} -> info -> {log}\n')
            f.close()
        except Exception as ex:
            print(f'{fecha} -> error -> no se pudo guardar en log')
        
    def errorlog(self, log):
        try:
            fecha = time.asctime(time.localtime(time.time()))
            print("error")
            with open('./log.txt', 'a') as f:
                f.write(f'{fecha} -> error -> {log}\n')
            f.close()
        except Exception as ex:
            print(f'{fecha} -> error -> no se pudo guardar en log')
