#Dicionario
#Coleção tipo chave/valor
#Mutaveis
#indexadas
#tipos de dados diferentes (incluindo chaves)
#exemplo
#nome: Patricia
#sexo nasc:
#idade: 52
#construtor da classe: {}, dict

print("Dicionarios")
meuDicionario = {"nome": "Patricia", "sexo":"feminino", "idade": 52}
print(type(meuDicionario))
print(meuDicionario)

outroDic = dict((("nome", "Patricia"),("sexo", "feminino"),(52, "idade")))
print(outroDic)

print("\n Acessando valor")
meuNome = meuDicionario["nome"]
print(meuNome)
print(meuDicionario["idade"])
print(outroDic[52])

print("\nRecuperando as chaves")
chaves = meuDicionario.keys()
print(chaves)

print("\n recuperando os valores")
valores = meuDicionario.values()
print(valores)

print("\n Recuperando os elementos\\itens")
itens = meuDicionario.items()
print(itens)

print("\n Recuperando todos as chaves um a um")
for chaves in meuDicionario:
    print(chaves)
for chaves in meuDicionario.keys():
    print(chaves)

print("\n Recuperando todos os valores")
for valor in meuDicionario.values():
    print(valor)

print("\n Recuperando todos os valores um a um")
for item in meuDicionario.items():
    print(item)

print("\n Truques")
print("\n Recuperando os valores a partir da chave")
for chaves in meuDicionario:
    print(meuDicionario[chaves])

print("\n Recuperando o par chave/valor separado")
for chaves, valor in meuDicionario.items():
    print(f"chave:{chaves} e o valo {valor}")

#atribuicao multipla
temperatura_minima, temperatura_máxima = 6, 27
print("Máx", temperatura_máxima)
print("Min", temperatura_minima)

print("Acrescentando items no dicionario")
meuDicionario["tipo saguineo"] = "0 Rh-"
print(meuDicionario)

print("\n mudando valores")
meuDicionario["idade"]=53

print("\nmudando valores com update")
meuDicionario.update({"nome":"Patricia Angelini"})
print(meuDicionario)
meuDicionario.update({"estado civil": " casada"})

print("\n Apagando itens")
print("Funcao NATIVA del")
del meuDicionario['estado civil']
print(meuDicionario)
print("Popitem - retira o ULTIMO PAR do dicionario")
meuDicionario.popitem()
print(meuDicionario)
print("Pop - escolho o que eu quero retirar")
meuDicionario.pop("sexo")
print(meuDicionario)


meuDicionario = {"nome": "Patricia", "sexo":"feminino", "idade": 52, "tipo sanguineo": "0 rh-"}
print(meuDicionario)
print("\nLocazando itens")
if "idade" in meuDicionario:
    print("Tem idade nas chaves do meu dicionario")
if "patricia angelini" in meuDicionario.values():
    print("Pat esta la")
if "idade" in meuDicionario:
    print("a idade é:" ,meuDicionario["idade"])


print("como gerar uma copia do dicionario")
meuDicionario = {"nome": "Patricia", "sexo":"feminino", "idade": 52, "tipo sanguineo": "0 rh-"}

copiaDicFake = meuDicionario
print("original\n", meuDicionario)
print("Copia\n", copiaDicFake)

copiaDicFake.popitem()
print("Depois do popitem")
print("original\n", meuDicionario)
print("Copia\n", copiaDicFake)

print("\n\nA copia real precisa se feita pelo método cp - Copy")
copiaDic = meuDicionario.copy()
print("original\n", meuDicionario)
print("Copia\n", copiaDic)



copiaDic.popitem()
copiaDic.popitem()
print("\n\nDepois do popitem")
print("original\n", meuDicionario)
print("Copia\n", copiaDic)
