import datetime
data = datetime.datetime.now()
data_atual = (str(data.day) + "/"  + str(data.month) + "/" + str(data.year))

class Produto:
    def __init__(self, nome, preco, validade, estoque, preco_promocao = 0, promocao = False):
        self.nome = nome
        self.preco = preco
        self.validade = validade
        self.estoque = estoque
        self.preco_promocao = preco_promocao
        self.promocao = promocao


# Vencer_de_validade
    def vencer_de_validade(self):
        if self.validade < data_atual:
            print('{} está Vencido'.format(self.nome))
        else:
            print('Não vencido')
        
# Atualização_de_preço
    def atualizar_preco(self, valor):
        self.preco = float(valor)
        
# Desconto
    def desconto(self, percentual):
        self.promocao = True
        self.preco_promocao = self.preco * (1 - (percentual / 100))

# Info_preço
    def exibir_preco(self):
            if self.promocao:
                print(self.preco_promocao)
            else:
                print(self.preco)

# Função de venda
    def vender(self, quantidade):
        if quantidade > self.estoque:
            print('Quantidade em estoque insuficiente')
        else:
            self.estoque = self.estoque - quantidade
            print('O valor da conta e:', self.preco * quantidade)