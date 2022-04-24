class Individuo:
    def __init__(self, nome, estado, acordado = True, alimentado = True):
        self.nome = nome
        self.estado = estado
        self.acordado = acordado
        self.alimentado = alimentado
        
    def apresentar(self):
        if self.acordado:
            print(f'Ola, sou {self.nome}')
        else:
            print('ZZZ...')
            
    def dormir(self):
        print(f'{self.nome} esta dormindo...')
        self.acordado = False
        self.alimentado = False
    
    def acordar(self):
        print(f'{self.nome} acabou de acordar...')
        self.acorado = True
        self.dormindo = False