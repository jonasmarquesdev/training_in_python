class Carro:
    def __init__(self, modelo, kmrodados, placa, valor_de_mercado, novo_ou_usado, quantidade_de_combustivel, km_percorridos_por_l, observacoes, valor_de_mercado_usado_defeito, ligado=False):
        self.modelo = modelo
        self.kmrodados = kmrodados
        self.placa = placa
        self.valor_de_mercado = valor_de_mercado
        self.novo_ou_usado = novo_ou_usado
        self.quantidade_de_combustivel = quantidade_de_combustivel
        self.km_percorridos_por_l = km_percorridos_por_l
        self.observacoes = observacoes
        self.valor_de_mercado_usado_defeito = valor_de_mercado_usado_defeito
        self.ligado = ligado


# Ligar
    def ligar(self):
        self.ligado = True
# Abastecer
# Corrida
# Valor de venda
    

'''
Deve ter os seguintes métodos:
- Ligar; Abastecer(retorna a conta); corrida(recebe uma quantidade de Km); valor de
venda(calculado baseado no valor total - (km rodada + quantidade de defeitos))(proponha uma
forma de calcular)
'''