print ("[M] - masculino ou [F] - feminino")
print ("M - masculino ou F - feminino")
sexo = str(input("Escolha uma opção válida: "))
idade = int(input("Qual a sua idade?"))
tempocontribuido = int(input("Quanto tempo você pagou: "))
tempoapagar = 15-tempocontribuido
if (sexo == "m"):
	if(tempoapagar <= 0 and idade >= 65):
		print("Você ja pode pedir sua aposentadoria.")
	elif(tempoapagar > 0 and idade < 65):
		print("Você ainda deve pagar, ",tempoapagar," anos.")
		idadeaesperar = 65 - idade
		print("Você deve esperar, ",idadeaesperar," anos.")
	elif(tempoapagar <= 0 and idade < 65):
		idadeaesperar = 65 -idade
		print("VocÊ deve esperar, ",idadeaesperar," anos.")
	elif(tempoapagar > 0 and idade >= 65):
		print("Você pode pedir um beneficio.")
else:
	if(tempoapagar <= 0 and idade >= 60):
		print("Você ja pode pedir sua aposentadoria.")
	elif(tempoapagar > 0 and idade < 60):
		print("Você ainda deve pagar, ",tempoapagar," anos.")
		idadeaesperar = 60 - idade
		print("Você deve esperar, ",idadeaesperar," anos.")
	elif(tempoapagar <= 0 and idade < 60):
		idadeaesperar = 60 -idade
		print("VocÊ deve esperar, ",idadeaesperar," anos.")
	elif(tempoapagar > 0 and idade >= 60):
		print("Você pode pedir um beneficio.")
