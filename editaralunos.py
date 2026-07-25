from main import *

def editar_alunos():

    while True:

        print("""
===================================
        EDITAR ALUNOS
===================================

1 - Alterar Nota
2 - Alterar Nome
3 - Alterar Turma
4 - Remover Aluno
5 - Voltar ao Menu Principal

===================================
""")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            alterar_nota()

        elif escolha == 2:
            alterar_nome()

        elif escolha == 3:
            alterar_turma()

        elif escolha == 4:
            remover_aluno()

        elif escolha == 5:
            print("Voltando...")
            break

        else:
            print("Opção inválida!")

def remover_aluno():

    nome = input("Qual o nome do aluno que deseja remover? ")

    if nome in alunos:
        confirmacao = input("Voce realmente deseja remover? ").upper()

        if confirmacao == "sim":
                del alunos[nome]
                print("Aluno removido!")

        else:
            print("Operação cancelada!")

    else:
        print("Nome invalido!")

def alterar_nota():

    nome = input("Qual o nome do aluno que deseja alterar? ")
    nota = int(input("Qual a nota que deseja alterar? "))

    if nome in alunos:

        notas = alunos[nome]["notas"]

        for i in range(len(notas)):

            if notas[i] == nota:

                nota_nova = int(input("Qual a nota nova? "))
                notas[i] = nota_nova

                print("Nota alterada com sucesso!")

    else:
        print("Aluno não encontrado!")


def alterar_nome():

    nome = input("Qual o nome do aluno que voce deseja alterar? ")

    if nome in alunos:

        turma_antiga = alunos[nome]["turma"]
        nota_antiga = alunos[nome]["notas"]

        nome_novo = input("Qual o nome novo? ")

        alunos[nome_novo] = {
            "turma": turma_antiga,
            "notas": nota_antiga
        }

        del alunos[nome]
        print("Alterando nome...")
        print("Nome alterado!")

    else:
        print("Nenhum aluno encontrado!")


def alterar_turma():

    nome = input("Qual o nome do aluno? ")

    if nome in alunos:

        turma_nova = int(input("Qual a turma nova? "))

        alunos[nome]["turma"] = turma_nova

        print("Turma alterada com sucesso!")

    else:
        print("Aluno não encontrado!")