from main import *

def ver_turmas():

    while True:

        print("""
===================================
             TURMAS
===================================

1 - Procurar Turma
2 - Ranking das Turmas
3 - Voltar ao Menu Principal

===================================
""")

        try:
            escolha = int(input("Escolha uma operação: "))
        except:
            print("Escolha um número válido!")
            continue

        if escolha == 1:
            procurar_turma()

        elif escolha == 2:
            rank_turmas()

        elif escolha == 3:
            print("Voltando...")
            break

        else:
            print("Escolha uma opção válida!")

def procurar_turma():

    turma_procurada = input("Qual a turma deseja procurar? ")
    contador = 0
    print(f"\n===== TURMA {turma_procurada} =====\n")


    for nome in alunos:

        turma_aluno = alunos[nome]["turma"]

        if turma_aluno == turma_procurada:

            print(f"Nome: {nome}")
            print(f"Turma: {turma_aluno}")
            print("-----------------------")

            contador += 1


    if contador == 0:
        print("Nenhum aluno encontrado nessa turma!")

    else:
        print(f"\n{contador} aluno(s) encontrado(s)!")

def rank_turmas():

    notas_turma = {}

    for nome in alunos:
        turma = alunos[nome]["turma"]
        notas = alunos[nome]["notas"]

        if turma not in notas_turma:
            notas_turma[turma] = []

        notas_turma[turma].extend(notas)

    media_turma = {}

    for turma, notas in notas_turma.items():

        media = sum(notas) / len(notas)
        media_turma[turma] = media

    ranking_ordenado = sorted(media_turma.items(), key=lambda x: x[1], reverse=True)

    print("--- RANKING DAS TURMAS ---")
    for turma, media in ranking_ordenado:
        print(f"Turma {turma} - Média: {media:.2f}")

    


            
