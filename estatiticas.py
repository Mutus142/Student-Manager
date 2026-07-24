from main import *

def estatisticas_menu():

 while True:

     print("""
        ===== ESTATÍSTICAS =====

        1 - Alunos aprovados
        2 - Alunos reprovados
        3 - Média geral da escola
        4 - Total de alunos
        5 - Voltar

        =======================
        """)

     escolha = int(input("Escolha uma opção: "))

     if escolha == 1:
          alunos_aprovados()

     elif escolha == 2:
          alunos_reprovados()

     elif escolha == 3:
          media_geral()

     elif escolha == 4:
          total_alunos()

     elif escolha == 5:
          print("Voltando...")
          break


def alunos_aprovados():

    contador = 0:

    for nome in alunos:

        notas = alunos[nome]["notas"]

        if len(notas) == 0:
            continue

        media = sum(notas) / len(notas)

        if media >= 6:
            print(f"\nNome: {nome}")
            print(f"Média: {media:.2f}")

            contador += 1

    if contador == 0:
        print("Nenhum aluno aprovado encontrado!")

    else:
        print(f"\nTotal de alunos aprovados: {contador}")

def alunos_reprovados():

    contador = 0

    for nome in alunos:

        notas = alunos[nome]["notas"]

        if len(notas) == 0:
            print("Nenhum aluno encontrado!")

        media = sum(notas) / len(notas)

        if media < 6:
            print("Nome: ", nome)
            print("Media: ", media)

        contador += 1

    if contador == 0:
        print("Nenhum aluno encontrado!")

    else:
        print(contador, "Alunos encontrados!")

def total_alunos():

    contador = 0:

    for nome in alunos:

        if len(notas) == 0:
            print("Nenhum aluno encontrado!")

        else:
            contador += 1

    if contador == 0:
        print("Nenhum aluno cadastrado!")

    else:
        print("O total de alunos é: ", contador)
