dicionario_convidados = {}
resp = "s"

while resp in ("s", "sim"):
    nome = input(f"Qual é o nome do convidado? ")
    idade = input(f"Qual é a idade de {nome}? ")
    estado_civil = input(f"Qual é o estado_civil de {nome}? ")

    caracteristicas = {}
    for i in range(3):
       caract = input(f"Qual a {i + 1} caracteristica de {nome} ?")
    caracteristicas[f" caracteristica {i + 1}"] = caract


dicionario_convidados[nome] = {
    "idade" = idade,
    "estado civil" = estado_civil,
    "caracteristicas" = caracteristicas}

resp = input("você quer cadastrar mais um? ").lower()
print(dicionario_convidados)

#
# conv_ok = sorted(convidados)
# dicionario_convidados["convidados"] = conv_ok
# print(f"Os convidados são {conv_ok}")


#
# estado_civil = []
# for conv_ok in convidados:
#     estado_civil = input(f"Qual o estado civil de {conv_ok} ")
#     estado_civil.append(conv_ok)
# print [conv_ok]