

lista_aluno_nota = []

nome = input("Insira o nome do aluno: ")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
media = ((nota1 + nota2) / 2)


if media > 6.5:
    print(f"{nome}. {media}. Aprovado(a)")
else:
    print(f"{nome}. {media}. Reprovado(a)")