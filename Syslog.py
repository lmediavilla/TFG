import time
class Syslog:
    def log(self, log):
        fecha = time.asctime(time.localtime(time.time()))
        with open('./log.txt', 'a') as f:
            f.write(f'{fecha} -> info -> {log}\n')
        f.close()
    def errorlog(self, log):
        fecha = time.asctime(time.localtime(time.time()))
        print("error")
        with open('./log.txt', 'a') as f:
            f.write(f'{fecha} -> error -> {log}\n')
        f.close()