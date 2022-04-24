idade = int(input("Qual a idade do usuario? "))

aprovacao = bool(input("O responsável do usuário aprova que o usuario assista o filme?"))



if idade >= 16 or aprovacao:
    print("O usuario pode assistir o filme")
else:
    print("O usuario não pode assisitir o filme")