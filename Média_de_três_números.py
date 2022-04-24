#números
n1 = int(input('Digite o Primeiro número.'))
n2 = int(input('Digite o Segundo número.'))
n3 = int(input('Digite o Terceiro número.'))

#média
media = (n1 + n2 + n3) / 3

#ou
'''
cal = n1 + n2 + n3
media = cal / 3
'''

#resultado
print('A média entre {}, {} e {} é igual a {}'.format(n1, n2, n3, media))