#exercicio moedas


dinheiro = 3.73


dinheiro = dinheiro * 100


moedas1real = dinheiro // 100
dinheiro = dinheiro % 100


moedas50centavos = dinheiro // 50
dinheiro = dinheiro % 50


moedas25centavos = dinheiro // 25
dinheiro = dinheiro % 25


moedas10centavos = dinheiro // 10
dinheiro = dinheiro % 10


moedas5centavos = dinheiro // 5
dinheiro = dinheiro % 5


print('Para o dinheiro informado precisamos de:')
print(moedas1real, 'moedas de 1 real')
print(moedas50centavos, 'moedas de 50 centavos')
print(moedas25centavos, 'moedas de 25 centavos')
print(moedas10centavos, 'moedas de 10 centavos')
print(moedas5centavos, 'moedas de 5 centavos')
print(dinheiro, 'moedas de 1 centavo')