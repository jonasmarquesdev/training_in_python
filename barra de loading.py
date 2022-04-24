from tqdm import tqdm
import time

#forma simples de fazer
#for i in tqdm(range(10)):
    #time.sleep(1)

with tqdm(total=100) as barra_progresso:
    for i in range(10):
        time.sleep(1)
        print('\nColetando dados')
        barra_progresso.update(10)
    print('\nCarregado')