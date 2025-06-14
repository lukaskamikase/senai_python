from os import system as limpar
limpar("cls") 

# vezes = 0
# valores = []
# lista = []

# while  vezes <  6: 
#     entrada = input("digite valores: ")
#     valores.append(entrada)
#     vezes += 1

# valores.insert(4,"lukas")

# for i in valores:
#     print(i)

# while valores :
#     entrada = input()
    
#     if entrada == "":
#         del(valores[0])
#         print(f"valor removido, sua lista atual é {valores}")    


# nomes  =  ["lucas","gustavo","vinicius","heron","lucas"]

# print(nomes)

# nomes.sort()
# print(nomes)

# nomes.sort(reverse = True)
# print(nomes)

lista = []

nome = input("Digite seu Nome: ")
data_nasc = input("Digite sua data de nascimento: ")
cpf = input("Digite seu Cpf: ")
Telefone = input("Digite seu telefone: ")

dicionario = {'nome': nome,
              'data_nasc': data_nasc,
              'cpf': cpf,
              'telefone': Telefone}

lista.append(dicionario)

print(f"NOME: {nome}\n DATA DE NASCIMENTO: {data_nasc}\n CPF: {cpf}\n TELEFONE: {Telefone}")

delete = input("deseja excluir o Cpf")
