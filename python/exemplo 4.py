#definir uma lista
numeros = [] #lista vazia
numeros = [12,35,100]

#inseriri elemento na lista
numeros.append(33)

#modificar elemento na lista
numeros[0] = 10

#remover elemento na lista pelo valor
numeros.remove(100)

#imprimir ultimo elemento da lista
tamanho = len(numeros)
print("ultimo elemento: ",numeros[2])

#remover elemento pela posição
del numeros[2]

print(numeros)

print("#------------------------------------------------------------#")
print("||                        Sua mensagem                      ||")
print("#------------------------------------------------------------#")

frutas = ["laranja","abacaxi","manga","kiwi","morango",
		 "pera","mamão","uva","abacate","tamarindo"]

for x in range(0,(len(frutas))):
	if(frutas[x] == "abacate"):
		print("O indice que você busca é",x)

print("#------------------------------------------------------------#")
print("||                        Sua mensagem                      ||")
print("#------------------------------------------------------------#")

#definição das listas N e I
N = []
I = []

for x in range(0,4):
	print("---------------------")
	nome = str(input("Nome: "))
	idade = int(input("Idade: "))
	N.append(nome)
	I.append(idade)

for x in range(0,4):
	if(N[x] == "joão"):
		print("A idade de joão é: ",I[x])
		
print(N)
print(I)

print("#------------------------------------------------------------#")
print("||                        Sua mensagem                      ||")
print("#------------------------------------------------------------#")

alunos = []
x = 0
while(x < 4):
	print("---------------------")
	nome = str(input("Nome: "))
	nota = float(input("Nota: "))
	aluno = {}
	aluno['nome'] = nome
	aluno['nota'] = nota
	alunos.append(aluno)
	x = x + 1
print(alunos)
