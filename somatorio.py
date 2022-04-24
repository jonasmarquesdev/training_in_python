quantidade = int(input('Digite a quantidade de termos da série: '))

numerador = 1
denominador = 1

somatorio = 0

for i in range(quantidade, 0, -1):
    somatorio += numerador/denominador
    numerador += 1
    denominador += 2
    
print('Resultado do somatorio da serie e:', somatorio)