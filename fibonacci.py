termo = int(input('Digite o termo da sequencia de fibonacci: '))

fib1 = 0
fib2 = 1

auxiliar = 3
resposta = 0


if termo == 1:
    print(fib1)
elif termo == 2:
    print(fib2)
else:
    while auxiliar <= termo:
        resposta = fib1 + fib2
        fib1 = fib2
        fib2 = resposta
        auxiliar += 1
        
    
    print(resposta)