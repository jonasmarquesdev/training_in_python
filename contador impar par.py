quantidade = 10

contadorpar = 0
contadorimpar = 0

while quantidade > 0:
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        contadorpar += 1
    else:
        contadorimpar += 1
    
    quantidade -= 1
    
print('A quantidade de numeros pares e {} e impares {}'.format(contadorpar, contadorimpar))