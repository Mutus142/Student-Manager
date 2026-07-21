alunos = {}

def cadastrar_aluno():
    nome = input("Qual é o nome do aluno? ")

    if nome in alunos:
        print("Aluno já cadastrado!")

    else:
        alunos[nome] = []
        print("Aluno Cadastrado!")

def adicionar_nota():
    nome = input("Qual o nome do aluno para adicionar a nota?")

    if nome in alunos:
        nota = int(input("Qual a nota?"))
        alunos[nome].append(nota)
        print("Nota adicionada!")

    else:
        print("Aluno não encontrado!")

def ver_boletim():

    nome = input("Qual o nome do aluno? ")
    if nome in alunos:
        nota = alunos[nome]

        if len(nota) == 0:
            print("Aluno sem nota!")
            return

        media = sum(nota) / len(nota)

        if media < 6:
            aprovacao = "Reprovado!"
        else:
            aprovacao = "Aprovado!"

        print("Nome:", nome)
        print("Notas:", nota)
        print("Média:", media)
        print("Resultado:", aprovacao)

    else:
        print("Aluno não encontrado!")

