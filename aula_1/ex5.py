
# elaboração do ex4

nome = input("Nome: ")
idade = int(input("Idade: "))
sexo = input("Sexo (Masculino ou Feminino): ")


if idade > 50:
    if sexo == "m":
        print(f"{nome} tem {idade} anos e é experiente. M.")
    else:
        print(f"{nome} tem {idade} anos e é experiente. F.")

elif idade < 50:
    if sexo == "m":
        print(f"{nome} tem {idade}; está em treinamento. M")
    else:
         print(f"{nome} tem {idade}; está em treinamento. F")

else:
    if sexo == "m":
        print(f"{nome} tá com cinquentão! M.")
    else:
        print(f"{nome} tá com cinquentão! F.")
