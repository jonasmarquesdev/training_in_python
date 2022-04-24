import string
from random import random,choice
valores=string.ascii_letters #todas as letras maiusculas e minusculas 
valores+=string.digits #vai de 0 a 9
valores+=string.punctuation #caracteres especiais
tamanho=10
senha=""

#print(string.punctuation)
#print(string.digits)
#print(valores)

for i in range (tamanho):
    senha+=choice(valores)

    
print(senha) #dessa forma tenho um gerador de senha com o tamanho 10 que 
#vai fazer todas as possiveis formas para genhar senhas diferentes
#por isso que existem sistemas que permitem só o sistema de tentar a senhas poucas vezes até bloquear