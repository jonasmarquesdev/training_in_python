numero = int(input('Digite um numero menor que mil: '))

while numero >= 1000:
    numero = int(input('Digite um numero menor que mil: '))
       
    
centena = numero // 100
numero %= 100

dezena = numero // 10
numero %= 10

unidade = numero

print('O numero digitado tem {} centenas, e {} dezenas e {} unidades'.format(centena, dezena, unidade))