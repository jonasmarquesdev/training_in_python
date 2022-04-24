numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

maior = 0

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
else:
    maior = numero3
    
medio = 0

if (numero1 < numero2 and numero1 > numero3) or (numero1 < numero3 and numero1 > numero2):
    medio = numero1
elif (numero2 < numero1 and numero2 > numero3) or (numero2 < numero1 and numero2 > numero2):
    medio = numero2
else:
    medio = numero3
    
menor = 0
    
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
else:
    menor = numero3
    
print(maior, '<', medio, '<', menor)