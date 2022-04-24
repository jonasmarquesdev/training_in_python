def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    #print(linha())

def cabeçalhofor(txt):
    print(txt.center(42))
    print(linha())

def center(txt):
    print(txt.center(55))

def menu(lista):
    cabeçalhofor('DESEJA JOGAR?')
    c = 1
    for item in lista:
        center(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc

from random import randint
import os

os.system("cls")
cabeçalho('DADOS V1.0')

while True:
    resposta = menu(['SIM', 'NÂO'])
    if resposta == 1:
        for num in range(1):
            dado = (randint(1,6))
            cabeçalho('Voçê tirou {} no dado!!'.format(dado))
            print(linha())
        break
    elif resposta == 2:
        print('\033[31mVocê desejou não jogar...\033[m')
        break
    else:
        os.system("cls")
        print('\033[31mERRO! Digite uma Opção válida\033[m')