import time
import threading

def codificar():
    time.sleep(2)
    print(f'Solo toma dos segundos en ejecutarlas')
    print(f'Codificando')

def responder_correos():
    time.sleep(2)

    print(f'Respondiendo correos')

def realizar_calculos():
    time.sleep(2)

    print(f'Realizar los calculos')


#Solo le toma 2 segundos en ejecutar las tres tareas
threading.Thread(target=codificar).start()
threading.Thread(target=responder_correos).start()
threading.Thread(target=realizar_calculos).start()

#Pero si ejecutamos de forma secuencial le tomaria 6 segundos en terminar todas las tareas
print(f'Le tomas 6 segundos en ejecutarlas')
codificar()
responder_correos()
realizar_calculos()