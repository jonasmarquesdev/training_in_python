import string
from itertools import combinations_with_replacement #vai gerar caracteres repetidos
from random import random,choice

def gerar_senhas(valores,tamanho):
    comb=combinations_with_replacement(valores,tamanho)
    print(list(comb))
    
valores='abc' #vou colocar os valores q eu quero que forme a senha
gerar_senhas(valores, 3) #e o tamanho