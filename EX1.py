import random
import sys
import math
from threading import Thread, RLock
import time

verrou = RLock()
a = [2, 3, 8, 9, 12]
def calcul_nombre(a):
    i =0
    for i in a:
     l= (i**2)
     print(l)



def calcul_cube(a) :
    for i in a:
        n = (i**3)
        print(n)

class Afficheur(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        self.a = a
    def run(self):
        i = 0
        while i < 10:
            with verrou:
                sys.stdout.write(self.a)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1, 60) / 1000000
                time.sleep(attente)
            i += 1

if __name__ == "__main__":
    thread_1 = calcul_nombre(a)
    thread_2 = calcul_cube(a)


    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()





