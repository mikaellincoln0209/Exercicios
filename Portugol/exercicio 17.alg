inicio
    real nota1, nota2, nota3, media
    
    escrever "Digite a primeira nota: "
    ler nota1
    escrever "Digite a segunda nota: "
    ler nota2
    escrever "Digite a terceira nota: "
    ler nota3
    
    media <- (nota1 + nota2 + nota3) / 3
    
    se media = 10 entao
        escrever "Aprovado com excelência."
    senao
        se media >= 6 entao
            escrever "Aprovado"
        senao
            escrever "Estude mais"
        fimse
    fimse
fim