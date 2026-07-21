alunos = []

def cadastrar_aluno():
    nome = input("Qual é o nome do aluno? ")

    if nome in alunos:
        print("Aluno já cadastrado!")

    else:
        alunos[nome] = {}
        print("Aluno Cadastrado!")