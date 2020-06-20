num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))
num3 = int(input("Digite o primeiro número: "))
num4 = int(input("Digite o primeiro número: "))

menor = 1

resto = num1 % 2
if (resto == 0):
	if(menor == 1):
		menor = num1
	else:
		if (num1 < menor):
			menor = num1
			
resto = num2 % 2
if (resto == 0):
	if(menor == 1):
		menor = num2
	else:
		if (num2 < menor):
			menor = num2
			
resto = num3 % 2
if (resto == 0):
	if(menor == 1):
		menor = num3
	else:
		if (num3 < menor):
			menor = num3

resto = num4 % 2
if (resto == 0):
	if(menor == 1):
		menor = num4
	else:
		if (num4 < menor):
			menor = num4
			
print ("O menor número par é ",menor)
