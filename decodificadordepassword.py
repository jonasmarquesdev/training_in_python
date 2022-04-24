import string
from random import*


valores = string.ascii_letters # Todas as letras maiusculas e minusculas 
valores += string.digits # Vai de 0 a 9
valores += string.punctuation # Caracteres especiais
tamanho = 10
password = ""

for i in range (tamanho):
    password += choice(valores)

acho = ""
passwordk = password

letras = string.ascii_letters # Todas as letras maiusculas e minusculas 
letras += string.digits # Vai de 0 a 9
letras += string.punctuation # Caracteres especiais

while (acho != passwordk):
    acho = ""
    for letra in passwordk:
        acholetra = letras[randint(0,49)]
        acho = str(acholetra) + str(acho)
    print(acho)
    
print("Senha encontrada: {}".format(acho))