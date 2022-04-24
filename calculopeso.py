entrada = input('Digite m para masculino e f para feminino: ')

sexo = True

if entrada == 'm':
    sexo = False
else:
    pass    

altura = float(input('Digite a altura do individuo: '))
peso = 0


if sexo:
    peso = (62.1 * altura) - 44.7
else:
    peso = (72.7 * altura) - 58
    
print('O peso ideal do individuo e:', peso)