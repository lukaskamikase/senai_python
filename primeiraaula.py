banco_de_dados = []

def introducao():
    
    print("=" * 50)
    print("      SISTEMA DE GERENCIAMENTO DE ALUNOS")
    print("=" * 50)
    print("Bem-vindo! Aqui você pode cadastrar, consultar,")
    print("listar e remover alunos de forma simples.")
    print("Escolha uma das opções do menu para começar.")
    print("=" * 50)

introducao()

def mostrar_menu():
    print("\nMenu de Opções:")
    print("1 - Cadastrar aluno")
    print("2 - Consultar aluno")
    print("3 - Listar todos os alunos")
    print("4 - Remover aluno")
    print("5 - Sair")

mostrar_menu()    

def cadastrar_usuarios():

    nome =  input("digite seu nome: ").lower()
    idade = int(input("digite sua idade: "))
    nota = float(input("digite a nota do aluno: "))

    dicionario = {'nome' : nome,
                  'idade' : idade,
                  'nota' : nota   }
    
    banco_de_dados.append(dicionario)

    print("Usuário cadastrado com sucesso")
    input("precione enter para continuar")
    
    return mostrar_menu(),selecionar_menu() 

def consultar_usuarios():
    
    consultar = input("Digite o nome para ser consultado: ").lower()

    encontrado = False

    for dicionario in banco_de_dados:
        if dicionario['nome'].lower() == consultar:
            print("\n=== Aluno Encontrado ===")
            print(f"Nome: {dicionario['nome']}")
            print(f"Idade: {dicionario['idade']}")
            print(f"Nota: {dicionario['nota']}")
            
            encontrado = True

    if encontrado == False:
        print("Aluno não encontrado.")

def consultar_todos_alunos():
    
    print("\n=== ALUNOS CADASTRADOS ===")
    
    for dicionario in banco_de_dados:
        print(f"Aluno: {dicionario['nome']}")

def apagar_alunos():

def selecionar_menu():

    menu = int(input("Digite uma opção: "))
    if menu == 1:
        return cadastrar_usuarios()

    elif menu == 2:
        return consultar_usuarios()

    elif menu == 3:
        return consultar_todos_alunos()

    elif menu == 4:
        return

selecionar_menu()


