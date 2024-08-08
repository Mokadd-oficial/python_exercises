#Alunos de uma Turma
#o Dada uma lista de nomes de alunos, ordene a lista em ordem
#alfabética. Em seguida, adicione um novo aluno no início da lista
#e outro no final.


l_alunos = []

while True:
    pergunta = input("gostaria de inserir um aluno ? y/n: ")
    if pergunta == "y":
        resposta = input("Insira o nome do aluno: ")
        l_alunos.append(resposta)
    elif pergunta == "n":
        break
    else:
        print: ("resposta invalida, selecione y ou n:")

l_alunos_ordenada = sorted(l_alunos)
print(f"a lista é: {l_alunos_ordenada}")