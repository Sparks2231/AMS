import threading
import time
#Crear un semáforo con un contador inicial de 2
semaphore = threading.Semaphore(1)

"""
Aquí se crea un semáforo con un contador inicial de 2.
Esto significa que hasta dos hilos pueden adquirir el semáforo simultaneamente.
Si un tercer hilo intenta adquirir el semáforo mientras los dos primeros aún lo tienen,
deberá esperar a que uno de los hilos lo libere.
"""

def tarea (id):
	print(f"Tarea {id} intentando acceder al recurso")
	with semaphore:
		print(f"Tarea {id} ha adquirido el semáforo")
		time.sleep(1)
		print(f"Tarea {id} ha liberado el semáforo")
		
"""
En esta función:
Si el contador del semáforo es 0 (porque otros hilos ya lo han adquirido),
el hilo se bloquea hasta que el semáforo sea liberado por otro hilo.
"""

# Crear múltiples hilos que ejecuten la función `tarea`
threads = []
for i in range(5):
	thread = threading.Thread(target=tarea, args=(i,))
	threads.append(thread)
	thread.start()
	
"""
En esta partde del código:

Se crea una lista threads para almacenar los objetos Thread.
En un bucle for que va de 0 a 4 (creando 5 hilos), se crea un nuevo hilo que ejecuta 
la función tarea con el argumento i (el índice del bucle).
Cada hilo se inicia con thread.start(), lo que hace que la función tarea se ejecute 
en paralelo en ese hilo.
"""

# Esperar a que todos los hilos terminen
for threads in threads:
	thread.join()
	

