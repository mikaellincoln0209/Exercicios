inicio
    real numerador, denominador, resultado
    
    escrever "Digite o numerador: "
    ler numerador
    escrever "Digite o denominador: "
    ler denominador
    
    se denominador = 0 entao
        escrever "Fração inválida: denominador é zero."
    senao
        resultado <- numerador / denominador
        escrever "O resultado da divisão é: ",resultado
    fimse
fim