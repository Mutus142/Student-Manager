alunos = {}

def cadastrar_aluno():
    nome = input("Qual é o nome do aluno? ")
    turma = input("Qual é a turma do aluno? ")

    if nome in alunos:
        print("Aluno já cadastrado!")

    else:
        alunos[nome] = {
            "turma": turma,
            "notas": []
        }

        print("Aluno cadastrado!")


def adicionar_nota():

    nome = input("Qual o nome do aluno para adicionar a nota? ")

    if nome in alunos:
        nota = int(input("Qual a nota? "))

        if nota > 10:
            print("Nota inválida!")
            return

        alunos[nome]["notas"].append(nota)
        print("Nota adicionada!")

    else:
        print("Aluno não encontrado!")


def ver_boletim():

    nome = input("Qual o nome do aluno? ")

    if nome in alunos:

        notas = alunos[nome]["notas"]
        turma = alunos[nome]["turma"]

        if len(notas) == 0:
            print("Aluno sem notas!")
            return

        media = sum(notas) / len(notas)

        if media < 6:
            aprovacao = "Reprovado!"
        else:
            aprovacao = "Aprovado!"

        print(f"\nNome: {nome}")
        print(f"Turma: {turma}")
        print(f"Notas: {notas}")
        print(f"Média: {media:.2f}")
        print(f"Resultado: {aprovacao}")

    else:
        print("Aluno não encontrado!")

def lista_alunos():

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!")
        return

    for nome in alunos:

        turma = alunos[nome]["turma"]
        notas = alunos[nome]["notas"]

        if len(notas) == 0:
            media = 0
        else:
            media = sum(notas) / len(notas)

        if media < 6:
            resultado = "Reprovado!"
        else:
            resultado = "Aprovado!"

        print("\nNome:", nome)
        print("Turma:", turma)
        print("Média:", f"{media:.2f}")
        print("Situação:", resultado)