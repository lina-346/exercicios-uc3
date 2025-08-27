# elaboração do ex3

nome = input("Nome: ")
idade = int(input("Idade: "))


if idade > 50:
    print(f"{nome} tem {idade} anos e é experiente.")
elif idade < 50:
    print(f"{nome} tem {idade}; está em treinamento.")
else:
    print(f"{nome} tá com CINQUENTÃO!")
