lados = int(input('Digite a quantidade de lados do poligono: '))

if lados == 3:
    base = float(input('Digite o valor da base: '))
    altura = float(input('Digite o valor da altura: '))
    area = base * altura / 2
    print('O poligono é um triangulo de area:', area)
elif lados == 4:
    lado = float(input('Digite o valor do lado: '))
    area = lado ** 2
    print('O poligono é um quadrado de area:', area)
elif lados == 5:
    print('O poligono é um pentagono.')
else:
    print('O poligono digitado nao esta cadastrado')