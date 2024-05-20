import threading
import time
semaphore = threading.Semaphore(2)


def caja (id):
	print(f"Caja {id} intentando accedediendo a la base de datos")
	with semaphore:
		print(f"Caja {id} ha accedido")
		time.sleep(2)
		print(f"Caja {id} ha salido de la base de datos")
		



threads = []
for i in range(5):
	thread = threading.Thread(target=caja, args=(i,))
	threads.append(thread)
	thread.start()
	


for threads in threads:
	thread.join()
