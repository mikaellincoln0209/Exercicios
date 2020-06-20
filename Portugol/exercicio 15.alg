inicio
    inteiro idade
    real salario, novosalario
    
    escrever "Digite a sua idade: "
    ler idade
    escrever "Digite seu salário: "
    ler salario
    
    se idade < 40 entao
        novosalario <- salario + (salario * 0.15)
        escrever "Seu sálario é: ",salario,"\n"
        escrever "Sofreu reajuste de: 15%\n"
        escrever "Seu novo sálario: ",novosalario
    senao
        se idade > 60 entao
            novosalario <- salario + (salario * 0.3)
            escrever "Seu sálario é: ",salario,"\n"
            escrever "Sofreu reajuste de: 30%\n"
            escrever "Seu novo sálario: ",novosalario
        senao
            se (idade >= 40 e idade <= 60) entao
            novosalario <- salario + (salario * 0.25)
            escrever "Seu sálario é: ",salario,"\n"
            escrever "Sofreu reajuste de: 25%\n"
            escrever "Seu novo sálario: ",novosalario
            fimse
        fimse
    fimse
fim 