numero = int(input("Digite um número inteiro positivo: "))

contador = 0

for x in range(numero,0,-1):
	resto = numero % x
	if (resto == 0):
		contador = contador + 1
if(contador == 2):
	print(numero,"é um número primo")
else:
	print(numero,"não é um número primo")
