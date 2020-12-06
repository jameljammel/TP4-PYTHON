import time
from multiprocessing import Lock, Process, Pool
import random
import sys

from EX1 import a


def calcul_nombre(a):
    i = 0
    for i in a:
        l = (i ** 2)
        print(l)


def calcul_cube(a):
    for i in a:
        n = (i ** 3)
        print(n)


def task(lock, calcul):
    lock.acquire()
    try:
        i = 0
        while i < 20:
            for nombre in calcul:
                sys.stdout.write(nombre)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1, 60) / 100
                time.sleep(attente)
                i += 1
    finally:  # partie pour relacher le verrou sinon il part en infinie
        lock.release()


def main():
    lock = Lock()
    processes = []
    for i in a:
        proc1 = Process(target=task, args=(lock, calcul_nombre(a)))
        processes.append(proc1)
        proc1.start()
        proc2 = Process(target=task, args=(lock, calcul_cube(a)))
        processes.append(proc2)
        proc2.start()

    for proc1 in processes:
        proc1.join()

    for proc2 in processes:
        proc2.join()


if __name__ == '__main__':
    main()
    with Pool(10) as p:
        print(calcul_cube(a))
        print(calcul_nombre(a))
