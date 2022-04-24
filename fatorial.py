numero = int(input('Digite um numero para retornar seu fatorial: '))

resultado = 1
auxiliar = numero

while auxiliar > 0:
    resultado *= auxiliar
    print(auxiliar)
    auxiliar -= 1
    
print('O valor do fatorial e:', resultado)