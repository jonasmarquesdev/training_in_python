def produto(operando1, operando2):
    parada = 0
    resposta = 0
    while parada < operando2:
        resposta += operando1
        parada += 1
        
    return resposta
    
def divinteira(numerador, denominador):
    resposta = 0
    auxiliar = numerador
    
    while auxiliar > denominador:
        auxiliar -= denominador
        resposta += 1
        
    return resposta
    
def resto(numerador, denominador):
    indice = 0
    auxiliar = numerador
    
    while auxiliar > denominador:
        auxiliar -= denominador
        indice += 1
        
    return auxiliar
    
def potencia(numero, expoente):
    
    if expoente == 0:
        print('O valor da potencia e: 1')
    else:
        resposta = 0
        controle = 1
        while controle < expoente:
            resposta += produto(numero, numero)
            controle += 1
        return resposta
        
numero1 = int(input('Digite o primeiro operando: '))
numero2 = int(input('Digite o segundo operando: '))

print('O valor do produto e:', produto(numero1, numero2))
print('O valor da divisao inteira e:', divinteira(numero1, numero2))
print('O valor do resto e:', resto(numero1, numero2))
print('O valor da potencia e:', potencia(numero1, numero2))