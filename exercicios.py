# você está organizando uma agenda colocando a informação de cada pessoa.
# Utilize a colecao que imita formulario para pegar itens como nome, endereco,
# telefone, idade

resp = "s"
LAgenda = []

while resp in ("s", "sim"):
    pessoa = {}
    # pessoa["nome"] = input("entre com o nome: ")
    # pessoa["tel"] = int(input("Entre com o tel: "))
    LAgenda.append({"nome" : input("Entre com o nome: "), "tel": int(input("entre com o tel: "))})
    # LAgenda.append(pessoa)
    resp = input("você quer cadastrar mais um? ").lower()
print(LAgenda)
#     nome = input("Entre com o nome: ")
#     tel = input("Entre com o tel: ")
#     pessoa = {"nome" : nome, "tel" : tel}
#     LAgenda.append(pessoa)
#     resp = input("você quer cadastrar mais um? ").lower()
#     interesses = []
for i in range(3):
        interesses.append = input(f"entre com {i+1} o interesses: ")
        pessoa["interesse"] = interesses
LAgenda = input("você quer cadastrar mais um? ").lower()

print(LAgenda)

# Acrescente os dados estado civil na colecao. Você vai montar um novo tinder em breve

LAgenda = [{"nome" : "Pat", "tel": 123}, {"nome" : "Ro", "tel" : 65456}]
for pessoa in LAgenda:
    # print(f"{item["nome"]}")
    pessoa["estado civil"] = input(f"Entre com o estado civi de {pessoa["nome"]}: ")
print(LAgenda)
# LAgenda["Estado Civil "] = input(f"Qual o estado civil de {nome}")
# print(LAgenda)

convidados = []
while resp in ("s", "sim"):
    convidados = input("Qual será o nome do convidado? ")
conv_ok = sorted(convidados)
resp = input("você quer cadastrar mais um? ").lower()
for i in range(3):
    caract = input(f"Qual a {i+1} caracteristica de {conv_ok} ?")

estado_civil = []
for conv_ok in convidados:
    estado_civil = input(f"Qual o estado civil de {conv_ok} ")
    estado_civil.append(conv_ok)
print [conv_ok]