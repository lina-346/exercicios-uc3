
# esta função não recebe parâmetros/argumentos e não retorna valores
def exibirMensagem():
    print("Olá, eu sou o Python")

exibirMensagem()


# recebe parâmetro e não retorna valor: 
def exibirMensagemPlus(mensagem):
    print(f"Olá, eu sou o Python {mensagem}")

exibirMensagemPlus("José")

# função que recebe parâmeto e retorna valor:
def multiplicar(num1, num2):
    valor = num1 * num2
    return valor

retorno = multiplicar(4, 2)
print(retorno)


# não recebe parâetro e retorna valor
def acenderFarol():
    return "Farol aceso"

print(acenderFarol())