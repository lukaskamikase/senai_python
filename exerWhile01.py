from os import system as limpar
limpas = ("cls")

senha =(input("Digite a senha:"))
senha = 123
while senha != 123:
    print("Senha incorreta")
    senha = int(input("Digite novamente:"))
 
print("senha correta")

erro += 1
if erro >= 3:
    print("Voce não tem mais tentativas.\
    Sistema bloqueado")
   
else: 
    print("Senha errada. tente novamente...")
    password = input ("Digite uma nova senha:")
     
print("Bem vindo ao sistema da lanchonete do senai")
