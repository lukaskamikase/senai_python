from os import system as limpar
limpar("cls")


dados = []
print("INSIRA SEUS DADOS ABAIXO:")
dados.append(input("Digite seu nome: "))                   
dados.append(input("Digite sua data de nascimento: "))  
dados.append(input("Digite seu cpf: "))                     
dados.append(input("Digite seu telefone: "))  


limpar("cls")
print("Meus dados são")
print(f"Nome: {dados [0]}")
print(f"Data de nascimento: {dados [1]}")
print(f"Digite seu cpf: {dados [2]}")
print(f"Digite seu telefone: {dados [3]}")

    
del(dados[2])
print(dados)
