from produto import Produto as pdt
import os
# marca, nome, preço, validade
produto1 = pdt('Café Solúvel Granulado Clássico', 4.49, '25/10/2021', 40)
produto2 = pdt('Refrigerante', 7.99, '10/11/2022', 20)

# Limpar console
os.system("cls")

# Info
produto1.desconto(10)
produto1.exibir_preco()
produto1.promocao = False
produto1.exibir_preco()

produto1.vender(50)
produto1.vender(30)
produto1.vender(10)
produto1.vender(1)