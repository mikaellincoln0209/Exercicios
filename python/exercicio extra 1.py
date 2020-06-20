numero_alunos = int(input("São quantos alunos: "))
alunos = []
medias = []
situacao = []
for x in range(0,numero_alunos,1):
	print("Aluno",(x+1))
	nome = str(input("Nome: "))
	ap1 = float(input("Ap 1: "))
	ap2 = float(input("Ap 2: "))
	aluno = {}
	aluno['Nome'] = nome
	aluno['Ap1'] = ap1
	aluno['Ap2'] = ap2
	alunos.append(aluno)

contador_aprovado = 0
contador_reprovado = 0
	
for x in range(0,numero_alunos,1):
	media = (alunos[x]['ap1'] + alunos[x]['ap2']) / 2
	medias.append(media)
	if(media >= 6):
		situacao.append('aprovado')
		contador_aprovado = contador_aprovado + 1
	else:
		situacao.append('reprovado')
		contador_reprovado = contador_reprovado + 1
		
print("Alunos Aprovados: ",contador_aprovado)
for x in range(0,numero_alunos,1):
	if(situacao[x] == 'aprovado'):
		print("Nome: ",alunos[x]['nome'])
		print("Medias;",medias[x])

print("Alunos Reprovados: ",contador_aprovado)
for x in range(0,numero_alunos,1):
	if(situacao[x] == 'reprovado'):
		print("Nome: ",alunos[x]['nome'])
		print("Medias;",medias[x])
