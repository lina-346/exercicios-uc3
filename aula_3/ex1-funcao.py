
def imParVerificar(num):
    if (num % 2 == 0):
        ''' print(f"{num} é um número par") -->  o ideal é a função fazer só uma coisa
        (nesse caso, apenas verificar os números.)
        '''
        return True
    else:
        return False


valor = int(input("Informe um número: "))

if (imParVerificar(valor)):
    print("O número é par.")
else:
    print("O número é ímpar")


########

# forma alternativa:
    
#def imParVerificar(num):
#  if (num % 2 == 0):
#    return True
#  else:
#    return False

# valor = int(input("Informe um número: "))

# print(imParVerificar(valor))