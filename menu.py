while True:

    print("""
    Escolha uma Opção

    1 - Cadastrar Aluno
    2 - Adicionar Nota
    3 - Ver Boletim
    4 - Sair
    """)

    escolha = int(input("Digite o numero para a proxima etapa: "))

    if escolha == 1:
        cadastrar_aluno()

    elif escolha == 2:
        adicionar_nota()

    elif escolha == 3:
        ver_boletim()

    elif escolha == 4:
        print("Saindo...")
        break

    else:
        print("Operação Inválida!")