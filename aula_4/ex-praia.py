
class Praia:
    def __init__(self, nome, distancia_do_centro, qtd_veranistas, tipo_de_acesso):
        self.nome = nome  # nome da praia
        self.distancia_do_centro = distancia_do_centro  # distância da praia até o centro da cidade
        self.qtd_veranistas = qtd_veranistas  # quantidade de veranistas na praia
        self.tipo_de_acesso = tipo_de_acesso  # tipo de acesso à praia (por exemplo, pedonal, de carro, etc.)

    def __str__(self):
        return (f"Praia {self.nome}, {self.distancia_do_centro} Km do centro, {self.qtd_veranistas} veranistas, acesso {self.tipo_de_acesso}")

# Exemplo de criação de um objeto da classe Praia #
'''
praia1 = Praia("Copacabana", 5, 3000, 1)
print(praia1)
'''

lista_de_praias = []
qntd_praias = int(input("Quantas praias serão informadas? "))

for i in range(qntd_praias):
    nome_praia = input("Informe o nome da praia: ")
    distancia_centro = int(input("Informe a distância da praia ao centro (Km): "))
    media_veranistas = int(input("Informe a média de veranistas que frequentaram na última temporada: "))
    tipo_acesso = int(input("Informe o tipo de acesso à praia ['0' - não asfaltado, '1' - asfaltado]: "))

    praia = Praia(nome_praia, distancia_centro, media_veranistas, tipo_acesso)
    lista_de_praias.append(praia)


'''for item in lista:
    print(item)
'''

# praias +15km do centro
num_praias_mais_15km  = 0

for praia in lista_de_praias:
    if praia.distancia_do_centro > 15:
        num_praias_mais_15km += 1

print(f"{num_praias_mais_15km}")

# qntd média de veranistas nas praias com acesso NÃO asfaltado
soma_veranistas = 0
qntd_praias = 0
qntd_media_veranistas_acesso_nasf = 0

for praia in lista_de_praias:
    if praia.tipo_de_acesso == 0:
        soma_veranistas += praia.veranistas
        qntd_praias += 1

qntd_media_veranistas_acesso_nasf = soma_veranistas / qntd_praias

print(f"{qntd_media_veranistas_acesso_nasf}")

praias_asf_menos_1000_veranistas = {}
for praia in lista_de_praias:
    if praia.tipo_de_acesso == 1 and praia.veranistas < 1000:
        praias_asf_menos_1000_veranistas.append({"nome": praia.nome, "distancia": praia.distancia_do_centro })

print(f"{praias_asf_menos_1000_veranistas}")