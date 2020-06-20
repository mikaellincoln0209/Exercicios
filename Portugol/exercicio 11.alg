inicio
    inteiro numero1, numero2, resto
    
    escrever "Digite o primeiro número: "
    	ler numero1
    escrever "Digite o segundo número: "
    	ler numero2

    resto <- numero1 % numero2
    se resto = 0 entao 
        escrever numero1," é divisivel por ",numero2,"\n"
    senao
        escrever numero1," não é divisivel por ",numero2,"\n"
    fimse
    
    resto <- numero2 % numero1
    se resto = 0 entao
        escrever numero2," é divisivel por ",numero1,"\n"
    senao
        escrever numero2," não é divisivel por ", numero1,"\n"
    fimse 
fim 
    
    
    
    