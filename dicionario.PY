from os import system as limpar
limpar("cls") 

dados = {"nome": None, "data" : None, "cpf" : None, "tel" : None}


print("BEM VINDO AO SISTEMA SENAI.")
print("INSIRA SEUS DADOS ABAIXO:")

dados["nome"] = input("Digite seu nome: ")
dados["data"] = input("Digite sua data de nascimento: ")
dados["cpf"] = input("Digite seu cpf: ")
dados["tel"] = input("Digite seu telefone: ")

print("Seus dados são:\n")
print("nome",dados["nome"])
print("data de nascimento ",dados["data"])
print("cpf:",dados["cpf"])
print("telefone",dados["tel"])

print()