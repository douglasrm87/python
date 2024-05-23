import threading
def tarefa1 ():
	x = 0
	while x < 5000:
		print("\nTeste execução 1 ")
		x += 1
def tarefa2():
	y = 0
	while y < 5000:
		print ("\nTeste execução 2")
		y += 1
def tarefa3():
	y = 0
	while y < 5000:
		print ("\nTeste execução 3")
		y += 1

#tarefa1()
#tarefa2()
#tarefa3()
threading.Thread(target=tarefa1).start()
threading.Thread(target=tarefa2).start()
threading.Thread(target=tarefa3).start()
