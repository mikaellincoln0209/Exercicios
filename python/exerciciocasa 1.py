inicio = int(input("Entre com o primeiro número: "))
fim = int(input("Entre com o segundo número: "))

if(inicio == fim):
	print("Não há o que somar, números iguais.")
else:
	if(inicio > fim):
		maior = inicio
		menor = fim
	else:
		maior = fim
		menor = inicio

	soma = 0

	for x in range (menor + 1,maior,1):
		resto = x % 2
		if(resto == 0):
			soma = soma + x
	print("A soma dos pares entre",inicio,"e",fim,"é",soma)
