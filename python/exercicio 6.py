idade = int(input("Digite sua idade: "))
if(idade < 16):
	print("Você é menor de idade e por isso não pode votar.")
elif(idade >= 16 and idade < 18):
	print("Você é menor de idade, mas pode votar.")
elif(idade >= 70):
	print("Você é maior de idade e vota se quiser.")
elif(idade >= 18 and idade < 70):
	print("Você é maior de idade e obrigado a votar.")
