numero = int(input("Digite um valor interio positivo: "))

soma = 0

for x in range(1,(numero + 1)):
	valor = int(input("Digite o %d° numero: " % x))
	soma = soma + valor
print ("A soma é: ",soma)	
