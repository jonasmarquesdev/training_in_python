class Pessoa:
    def __init__(self, nome, apelido, idade, rua, alimentado = True, acordado = True):
        self.nome = nome
        self.apelido = apelido
        self.idade = idade
        self.rua = rua
        self.alimentado = alimentado
        self.acordado = acordado
        
    def apresentacao(self):
        if self.acordado:
            print('Ola, meu nome é ', self.nome)
        else:
            print('ZZZ')
    
    def falar(self):
        print('bla bla bla')
        
    def acordar(self):
        self.acordado = True
        self.alimentado = False
        print('{} está acordado'.format(self.nome))
    
    def cumprimentar(self):
        if self.acordado:
            print('Olá, tudo bem?')
        else:
            print('ZZZ')

    def envelhecer(self):
        self.idade = self.idade + 1 

    def dormir(self):
        print('{} está dormindo'.format(self.nome))
        self.acordado = False
        self.dormindo = False
        
    def comer(self, alimento):
        if self.acordado and not self.alimentado:
            print('{} está comendo {}'.format(self.nome,alimento))
            self.alimentado = True
        elif self.acordado and self.alimentado:
            print('{} -estou satisfeito'.format(self.nome))
        else:
            print('ZZZ')

    @classmethod
    def fabricarpessoa(cls, nome, apelido, idade, rua):
        return cls(nome, apelido, idade, rua)
        
    @staticmethod
    def somar(numero1, numero2):
        return numero1 + numero2

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        self._idade = int(valor)