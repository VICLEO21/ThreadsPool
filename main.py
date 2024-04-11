import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

print("-----------------------------------------")
print("Dos hilos")
globalArrayNum = []
def contadorDos(inicio,fin):
    logging.info(f'Funcion con rango: {inicio} - {fin}')
    for i in range (inicio,fin+1,1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0 
t0 = time.time()
listaHilos = []
t = threading.Thread(target=contadorDos, args=(1,50))
listaHilos.append(t)
t.start()
t = threading.Thread(target=contadorDos, args=(51,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join()
tf=time.time()-t0

globalArrayNum.sort()
print(f'Tiempo de ejecucion: {tf}')
print(globalArrayNum)
print("-------------------------")
print("Pool de Hilos")


def printHW():
    logging.info(f'Funcion HW')
    print("Hola mundo")
    

subrango = 200//4
rangoActual = 1
executors = 4
globalArrayNum = []
with ThreadPoolExecutor(max_workers=2) as executor:
    for i in range (1,executors +1,1):
        j = subrango * i
        executor.submit(contadorDos, rangoActual , j)
        rangoActual = subrango + rangoActual

# Forma Hardcodeada
#    executor.submit(contadorDos,1,50)
#    executor.submit(contadorDos,51,100)
#    executor.submit(contadorDos,101,150)
#    executor.submit(contadorDos,151,200)
#    executor.submit(printHW)

tf = time.time() - t0
    
globalArrayNum.sort()
print(f'Tiempo de ejecucion: {tf}')
print(globalArrayNum)


