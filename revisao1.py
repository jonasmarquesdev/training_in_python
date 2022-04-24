def filtro(vetor):
    
    for i in vetor:
        while vetor.count(i) > 1:
            vetor.remove(i)
            
    return vetor

def somatorio (numero):
    auxiliar = 0
    resultado = 0
    
    while auxiliar <= numero:
        resultado += auxiliar
        auxiliar += 1
         
    return resultado

def somatorio_rec (numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return numero + somatorio_rec(numero - 1)

def horario (segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    
    return str(horas) + ':' + str(minutos) + ':' + str(segundos)
    
def mmc(numero1, numero2):
    auxiliar = 1
    resultado = 1
    
    while auxiliar <= numero1 or auxiliar <= numero2:
        if numero1 % auxiliar == 0 and numero2 % auxiliar == 0:
            resultado *= auxiliar
            auxilar = 1
        else:
            if numero1 % auxiliar == 0:
                resultado *= auxiliar
                auxiliar = 1
            if numero2 % auxiliar == 0:
                resultado *= auxiliar
                auxiliar = 1
        auxiliar += 1
                
    return resultado

def mdc(numero1, numero2):
    auxiliar = 1
    resultado = 1
    
    while auxiliar <= numero1 or auxiliar <= numero2:
        if numero1 % auxiliar == 0 and numero2 % auxiliar == 0:
            numero1 = numero1 / auxiliar
            numero2 = numero2 / auxiliar
            resultado *= auxiliar
            auxiliar = 1
        else:
            if numero1 % auxiliar == 0:
                numero1 = numero1 / auxiliar
            if numero2 % auxiliar == 0:
                numero2 = numero2 / auxiliar
        auxiliar += 1
        
    return resultado

def fatorial(numero):
    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

def combinacao(n, p):
    comb = fatorial(n) / (fatorial(p) * fatorial(n - p))
    return comb

def uniao(vetor1, vetor2):
    vetorunido = vetor1 + vetor2
    vetorunido = filtro(vetorunido)
    vetorunido.sort()
    return vetorunido

def moda(vetor):
    elemento = 0
    maior = 0
    
    for i in vetor:
        if vetor.count(i) > maior:
            elemento = i
            maior = vetor.count(i)
    
    if maior == 1:
        return 'A sequencia e amodal'
    else:
        return 'A moda e: ' + str(elemento) + ' com ' + str(maior) + ' ocorrencias'


vet1 = [1, 2, 3, 4, 5, 6]
vet2 = [2, 3, 4, 5, 6, 7]
vet3 = [1,2,3,3,3,3,4,4,4,1,3,2,3,4,4,5]

print(uniao(vet1, vet2))

print(moda(vet1))
print(moda(vet3))