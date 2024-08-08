#Biblioteca de Livros
#o Crie uma lista com os títulos de 5 livros que você tem na sua
#estante. Substitua o terceiro livro por um novo título. Verifique se
#um determinado livro está na lista.


livros = []

while True:
    pergunta = input("vamos adicionar livros a sua estante ? y/n: ")
    if pergunta == "y":
        item_livro = input("insira um titulo de livro: ")
        livros.append(item_livro)
    elif pergunta == "n":
        break
    else:
        print("resposta invalida, selecione y ou n:")

print(f"Sua estante atual é: {livros}, vamos trocar o 3º titulo!\n")
del livros[2]
print(f"Estante atual: {livros}\n\n")

novo_livro = input("qual será o novo livro para a 3º posição ? \n")
if len(livros) > 2:
      livros.insert(2, novo_livro)
else:
    livros.append(novo_livro)
print(f"Sua estante atual é: {livros}")