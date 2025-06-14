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

# nomes = []
# lista = []

# while True:
#     nome = input("Digite seu Nome: ")
#     data_nasc = input("Digite sua data de nascimento: ")
#     cpf = int(input("Digite seu Cpf: "))
#     Telefone = int(input("Digite seu telefone: "))

#     dicionario = {
#         'nome': nome,
#         'data_nasc': data_nasc,
#         'cpf': cpf,
#         'telefone': Telefone
#     }
    
    # lista.append(dicionario)
    # nomes.append(dicionario['nome'])

    # print(f"\nNOME: {nome}\nDATA DE NASCIMENTO: {data_nasc}\nCPF: {cpf}\nTELEFONE: {Telefone}")

    # delete = input("precione 'd' para deletar o CPF, 's' para sair ou 'c para consultar', precione enter para continuar: ").lower()

    # if delete == "d":
    #     del(dicionario['cpf'])
    #     print("\nCPF removido!")
    #     print(f"NOME: {dicionario['nome']}\nDATA DE NASCIMENTO: {dicionario['data_nasc']}\nTELEFONE: {dicionario['telefone']}")

    # elif delete == "s":
    #     break    

    # if delete == "c":
    #     consulta = input("digite o nome a ser pesquisado: ").lower()


    #     if consulta in nomes:
    #         print("\nUsuário Encontrado:\n")
    #         for pessoa in lista:
    #             if pessoa['nome'].lower() == consulta:
    #                 print(f"\nNOME: {pessoa['nome']} \nDATA DE NASCIMENTO: {pessoa['data_nasc']}")
                
    #                 if 'cpf' in pessoa:
    #                     print(f"CPF: {pessoa['cpf']}")
    #                 else:
    #                     print("CPF removido!!")  

    #                 print (f"TELEFONE: {pessoa['telefone']}")    

    #     else:
    #         print("Usuário não encontrado.")

# numero_de_convidados = 0
# lista = []

# while numero_de_convidados < 30:
    
#     nome = input("digite seu nome: ").lower()
#     numero_de_convidados += 1

#     dicionario = {
#                 'nome': nome,
#                 'quantidades': numero_de_convidados
#                 }

#     lista.append(dicionario)

# while True:
#     consulta = input("Deseja consuntar? s/n: ")

#     if consulta == "s":
#         pesquisa = input("digite o convidado: ")
        
#         if pesquisa in lista:
#             print("Convidado foi a festa")

#         else:
#             print("Convidado não foi a Festa", lista)  
#     else:
#         break
            

import math

def sub(valor1, valor2):
    return valor1 - valor2

def soma(valor1, valor2):
    return valor1 + valor2

def mult(valor1, valor2):
    return valor1 * valor2

def div(valor1, valor2):
    try:
        return valor1 / valor2
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
        return None

def expo(valor1, valor2):
    return valor1 ** valor2

def raiz(valor1):
    if valor1 < 0:
        print("Erro: Raiz de número negativo!")
        return None
    return math.sqrt(valor1)

def seno(valor1):
    return math.sin(math.radians(valor1))

def coss(valor1):
    return math.cos(math.radians(valor1))

def menu():
    while True:
        print("*" * 50)
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Exponenciação (**)")
        print("6 - Raiz")
        print("7 - Seno")
        print("8 - Cosseno")
        print("9 - SAIR")
        print("*" * 50)
        
        opcs = input("Digite a opção desejada: ").strip()

        if opcs == "1":
            return 1
        elif opcs == "2": 
            return 2
        elif opcs == "3":
            return 3
        elif opcs == "4":
            return 4
        elif opcs == "5":
            return 5
        elif opcs == "6":
            return 6
        elif opcs == "7":
            return 7
        elif opcs == "8":
            return 8
        elif opcs == "9":
            return 9
        else:
            print("Opção inválida! Digite um número entre 1 e 9.")

def logica_menu():
    while True:
        opcs = menu()
        
        if opcs == 9:
            print("Opção SAIR Selecionada.")
            break

        try:
            if opcs in [1, 2, 3, 4, 5]:
                x = float(input("Digite o primeiro valor: "))
                y = float(input("Digite o segundo valor: "))
            else:
                x = float(input("Digite o valor: "))

        except ValueError:
            print("Erro: Digite apenas números válidos.")
            continue

        if opcs == 1:
            print("Opção Soma Selecionada.")
            valor = soma(x, y)

        elif opcs == 2:
            print("Opção Subtração Selecionada.")
            valor = sub(x, y)

        elif opcs == 3:
            print("Opção Multiplicação Selecionada.")
            valor = mult(x, y)

        elif opcs == 4:
            print("Opção Divisão Selecionada.")
            valor = div(x, y)
            if valor is None:
                continue

        elif opcs == 5:
            print("Opção Exponenciação Selecionada.")
            valor = expo(x, y)

        elif opcs == 6:
            print("Opção Raiz Selecionada.")
            valor = raiz(x)
            if valor is None:
                continue

        elif opcs == 7:
            print("Opção Seno Selecionada.")
            valor = seno(x)

        elif opcs == 8:
            print("Opção Cosseno Selecionada.")
            valor = coss(x)
        
        print("Cálculo Realizado Com Sucesso!!")
        print(f"Resultado da operação: {valor}\n")

print("Calculadora Interativa")
logica_menu()


