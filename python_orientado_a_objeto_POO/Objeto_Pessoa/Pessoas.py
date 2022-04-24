from pessoa import Pessoa as ps
#(nome, apelido, idade, rua, alimentado, acordado)
pessoa1 = ps('Jubileu', 'Jubis', 20, 'rua fulano de tal')
pessoa2 = ps('João Snow', 'João das Neves', 23, 'Winterfel')

"""
print(pessoa1.apelido)
print(pessoa2.apelido)

print(pessoa1.acordado)
print(pessoa2.acordado)
"""

print('<==>' * 10)
pessoa1.dormir()
pessoa2.apresentacao()
pessoa1.acordar()
pessoa1.comer('Maçâ')
pessoa2.comer('Pera')
# repare que a pessoa 2 esta satisfeita porque 
# não dormiu ainda para ficar com fome
print('<==>' * 10)
pessoa2.dormir()
pessoa2.acordar()
# no momento que a pessoa 2 
# acordadar vai acordar com fome
pessoa2.comer('Pera')
print('<==>' * 10)
