inicio
    inteiro lado1, lado2, lado3, lado4
    
    escrever "Digite o primeiro lado: "
    ler lado1
    escrever "Digite o segundo lado: "
    ler lado2
    escrever "Digite o terceiro lado: "
    ler lado3
    escrever "Digite o quarto lado: "
    ler lado4
    
    se (lado1 = lado2) e (lado1 = lado3) e (lado1 = lado4) e (lado2 = lado3) e (lado2 = lado4) e (lado3 = lado4) entao
        escrever "É um quadrado."
    senao
        se (lado1 =/= lado2) e (lado1 =/= lado3) e (lado1 =/= lado4) e (lado2 =/= lado3) e (lado2 =/= lado4) e (lado3 =/= lado4) entao
            escrever "É um trapézio escaleno."
       senao
           se (lado1 = lado2) ou (lado1 = lado3) ou ( lado1 = lado4) ou (lado2 = lado3) ou (lado2 = lado4) ou (lado3 = lado4) entao
               escrever "É um trapézio isósceles."
           fimse
       fimse
    fimse
fim