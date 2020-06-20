inicio
    inteiro num1, num2, num3, aux
    
    escrever "Digite o primeiro número: "
    ler num1
    escrever "Digite o segundo número: "
    ler num2
    escrever "Digite o terceiro número: "
    ler num3
    
    se num1 < num2 entao
         aux <- num2
         num2 <- num1
         num1 <- aux
    fimse
    
    se num1 < num3 entao
        aux <- num3
        num3 <- num1
        num1 <- aux
    fimse
    
    se num2 < num3 entao
        aux <- num3
        num3 <- num2
        num2 <- aux
   fimse
   
   escrever "Os valores na ordem decrescente:\n"
   escrever num1,",",num2,",",num3
fim