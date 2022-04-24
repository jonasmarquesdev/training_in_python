from time import sleep

def linha(tam = 30):
    return '-' * tam

def linhab(tam = 30):
    return '=' * tam

def carregamento(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def titulo(txt):
    print(txt.center(42))

def carregamentocompleto(i=1, f=20, p=2):
    print(linhab())
    #titulo(f'Contagem de {i} até {f} de {p} em {p}')
    
    carregamento('Carregando')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')

carregamentocompleto()