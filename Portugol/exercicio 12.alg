inicio
    inteiro num1, num2, num3, num4, menor, resto
    
    escrever "Digite o primeiro número: "
    ler num1
    escrever "Digite o segundo número: "
    ler num2
    escrever "Digite o terceiro número: "
    ler num3
    escrever "Digite o quarto número: "
    ler num4
    
    menor <- 1
    
    resto <- num1 % 2
    se resto = 0 entao
        se menor = 1 entao
            menor <- num1
        senao
            se num1 <= menor entao
                menor <- num1
            fimse
        fimse
    fimse
    
    resto <- num2 % 2
    se resto = 0 entao
        se menor = 1 entao
            menor <- num2
        senao
            se num2 <= menor entao
                menor <- num2
            fimse
        fimse
    fimse
    
    resto <- num3 % 2
    se resto = 0 entao
        se menor = 1 entao
            menor <- num3
        senao
            se num3 <= menor entao
                menor <- num3
            fimse
        fimse
    fimse
    
    resto <- num4 % 2
    se resto = 0 entao
        se menor = 1 entao
            menor <- num4
        senao
            se num4 <= menor entao
                menor <- num4
            fimse
        fimse
    fimse
    
    se menor = 1 entao
        escrever "Você não digitou nenhum número par."
    senao
        escrever "O menor número par é: ",menor
    fimse 
fim 
    
    
    
    