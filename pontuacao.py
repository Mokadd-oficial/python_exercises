#Pontuações de um Jogo
#o Você tem uma lista com as pontuações dos jogadores em um
#jogo. Encontre a pontuação mais alta, a mais baixa e a média das
#pontuações.


pontuacao = [50,100,300]
maior_pontuacao = max(pontuacao)
menor_pontuacao = min(pontuacao)
media_pontuacao = sum(pontuacao) / len(pontuacao)
print(f' a maior pontuacao é: {maior_pontuacao}')
print(f' a menor pontuacao é: {menor_pontuacao}')
print(f' a media da pontuacao é: {media_pontuacao}')

print("\n\n")

#ou
print(f" Max:{max(pontuacao)}\n Min:{min(pontuacao)}\n Média: {sum(pontuacao)/ len(pontuacao)}")

