op = 1
while(op != 0):
	print("======================")
	print("\tMenu")
	print("======================")
	print("[1] - Soma\t[2] - Subtração")
	print("[3] - Multiplicação\t [4] - Divisão")
	print("[5]- Sair")
	op = int(input("Informe uma opção válida: "))
	
	if(op > 0 and op < 5):
		if(op == 1):
			print("\nSoma")
			num1 = int(input("Entre com o primeiro número: "))
			num2 = int(input("Entre com o segundo número: "))
			soma = num1 + num2
			print("A soma é: ",soma)
		
		elif(op == 2):
			print("\nSubtração")
			num1 = int(input("Entre com o primeiro número: "))
			num2 = int(input("Entre com o segundo número: "))
			sub = num1 - num2
			print("A subtração é: ",sub)
		
		elif(op == 3):
			print("\nMultiplicação")
			num1 = int(input("Entre com o primeiro número: "))
			num2 = int(input("Entre com o segundo número: "))
			mult = num1 * num2
			print("A multiplicação é: ",mult)
		
		elif(op == 4):
			print("\nDivisão")
			num1 = int(input("Entre com o primeiro número: "))
			num2 = int(input("Entre com o segundo número: "))
			div = num1 / num2
			print("A divisão é: ",div)
		
print("Calculadora Encerrada!")
