from main import *
from estatiticas import *
from editaralunos import *

while True:

    print("""
    1 - Cadastrar Aluno
    2 - Adicionar Nota
    3 - Ver Boletim
    4 - Lista de Alunos
    5 - Editar Alunos
    6 - Procurar Turma
    7 - Estatisticas Gerais
    8 - Sair
    """)

    try:
        escolha = int(input("Digite o numero para a proxima etapa: "))

    except:
        print("Digite apenas números!")
        continue

    if escolha == 1:
        cadastrar_aluno()

    elif escolha == 2:
        adicionar_nota()

    elif escolha == 3:
        ver_boletim()

    elif escolha == 4:
        lista_alunos()

    elif escolha == 5:
        editar_alunos()

    elif escolha == 6:
        procurar_turma()

    elif escolha == 7:
        estatisticas_menu()

    elif escolha == 8:
        print("Saindo...")
        break