from os import system as limp 
limp("cls")

# def cadastro_de_produtos():

#     produtos = []

#     while True:
#         try:
        
#             nome = input("digite o nome do produto: ").lower()
            
#             if nome == "sair":
#                 print("Saindo...")
#                 break

#             if nome == "consultar":
#                 input("Digite o valor a ser pesquisado: ").lower()

#                 for pesquisa in produtos:
#                     print("Produto Encontrado:\n ")
#                     print(f"Nome: {pesquisa['nome']}, Preço: {pesquisa['preço']}, Quantidade: {pesquisa['quantidade']}\n")
#                     continue

#             preço = float(input("digite o preço do produto: "))
#             quantidade = int(input("digite a quantidade: "))

#             produto = { 'nome': nome,
#                         'preço': preço,
#                         'quantidade': quantidade}

#             produtos.append(produto)

#             print("\nProduto cadastrado")
#             print(f"Nome: {nome}, Preço: {preço}, Quantidade: {quantidade}")

#         except ValueError:
#             print("digite números para PREÇO e QUANTIDADE")

# cadastro_de_produtos()  


lista = []

while True:
    nome = input("Digite seu Nome: ")
    data_nasc = input("Digite sua data de nascimento: ")
    cpf = int(input("Digite seu Cpf: "))
    Telefone = int(input("Digite seu telefone: "))

    dicionario = {
        'nome': nome,
        'data_nasc': data_nasc,
        'cpf': cpf,
        'telefone': Telefone
    }

    lista.append(dicionario)

    print(f"\nNOME: {nome}\nDATA DE NASCIMENTO: {data_nasc}\nCPF: {cpf}\nTELEFONE: {Telefone}")

    delete = input("precione 'd' para deletar o CPF, 's' para sair ou 'c para consultar', precione enter para continuar: ").lower()

    if delete == "d":
        del(dicionario['cpf'])
        print("\nCPF removido!")
        print(f"NOME: {dicionario['nome']}\nDATA DE NASCIMENTO: {dicionario['data_nasc']}\nTELEFONE: {dicionario['telefone']}")
        print("Eu sou o nego doce gay!")
    elif delete == "s":
        break    

    if delete == "c":
        consulta = input("digite o nome a ser pesquisado: ").lower()

        if consulta in lista:
            print("Usuario Encontrado:\n ")
            print(f"{ksks['nome']} {ksks['data_nasc']} {ksks['cpf']} {ksks['telefone']}")
        
        else:
            print("item não encontrado")    


        
    

