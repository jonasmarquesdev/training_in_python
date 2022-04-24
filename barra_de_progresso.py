from time import sleep

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, preencher='>'):
    porcentagem = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    comprimento_preenchido = int(length * iteration // total)
    barra = preencher * comprimento_preenchido + '-' * (length - comprimento_preenchido)
    print(f'\r{prefix} |{barra}| {porcentagem}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 20))
l = len(items)

loadbar(0, l, prefix='Progresso', suffix='Completo', length=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, l, prefix='Progresso', suffix='Completo', length=l)