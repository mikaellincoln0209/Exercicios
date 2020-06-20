num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))
conta3 = 0
contan = 0
# Teste divisivel por 3
resto = num1 % 3
if(resto == 0):
	conta3 += 1

resto = num2 % 3
if(resto == 0):
	conta3 += 1
# teste do número 3
resto = num3 % 3
if(resto == 0):
	conta3 += 1
	
resto = num4 % 3
if(resto == 0):
	conta3 += 1
	
resto = num5 % 3
if(resto == 0):
	conta3 += 1
	
# teste negativo
if(num1 < 0):
	contan += 1
if(num2 < 0):
	contan += 1
if(num3 < 0):
	contan += 1
if(num4 < 0):
	contan += 1
if(num5 < 0):
	contan += 1
	
print(conta3," são divisiveis por 3\n.")
print(contan," são negativos.")
	
