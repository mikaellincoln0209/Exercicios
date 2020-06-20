a = int(input("Entre com um número inteiro positivo: "))
fatorial = 1
for x in range(a,0,-1):
	fatorial = fatorial * x
print ("O resultado do fatorial é: ",fatorial)
