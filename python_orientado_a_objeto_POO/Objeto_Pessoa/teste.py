from pessoa import Pessoa as ps

pessoa1 = ps('Andre', 'dre', 23, 'rua fulaninho de tal')
pessoa2 = ps('Beatriz', 'bia', 19, 'rua ciclaninho')

pessoa1.dormir()
pessoa2.comer('banana') 

pessoa1.acordar()
pessoa1.comer('maca')
pessoa1.comer('banana')

pessoa2.dormir()
pessoa2.apresentacao()
pessoa1.apresentacao()

pessoa3 = pessoa1.fabricarpessoa('joao', 'jao', 7, pessoa1.rua)
print(pessoa3.nome)

print(ps.somar(3, 4))

pessoa1.envelhecer()
print(pessoa1.idade)
pessoa4 = ps('Claudia', 'clay', '21', 'rua ciclaninho')

pessoa4.envelhecer()
print(pessoa4.idade)