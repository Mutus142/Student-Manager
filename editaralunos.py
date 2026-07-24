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

