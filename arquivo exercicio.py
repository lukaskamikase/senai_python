from os import system as limpar
limpar("cls") 

perg1 = input("Digite seu nome: ")
perg2 = input("Digite sua idade: ")

with open ("dados_usuario.txt","a") as arquivo:
    arquivo.write("Seu nome: " + perg1 + "\n")
    arquivo.write("Seu nome: " + perg2 + "\n")

