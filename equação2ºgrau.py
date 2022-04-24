a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('Não existe raízes reais.')
else:
    r1 = (-b + delta**0.5) / (2 * a)
    r2 = (-b - delta**0.5) / (2 * a)
    print(f'As raízes são: {r1} e {r2}')