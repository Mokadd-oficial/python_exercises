#Lista de Compras
#o Crie uma lista com pelo menos 5 itens que você compraria em
#uma ida ao supermercado. Remova o terceiro item da lista e
#adicione dois novos itens ao final. Mostre a lista final.


lc = []

while True:
    pergunta = input("gostaria de adicionar item ? y/n: ")
    if pergunta == "y":
        item = input("insira um item da lista: ")
        lc.append(item)
    elif pergunta == "n":
        break
    else:
        print: ("resposta invalida, selecione y ou n:")

print(f"lista de compras atual: {lc}")

del lc[2]

print
print(f"lista de compras atual: {lc}")