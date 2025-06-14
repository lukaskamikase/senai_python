from os import system as limpar
limpar("cls") 

# while True:
#     contador = 1
#     numero = (input("Digite uma Tabuada ou digite (sair) para encerrar: "))
    
#     if numero == "sair":
#         import time

#         print("saindo", end="", flush=True)

#         for i in range(5):
#             time.sleep(0.5)
#             print(".", end="", flush=True)
#         break
            

#     while contador <= 10:

#         try:
#             converter = int(numero)
            
#             resultado = converter * contador
#             print(f"{converter} X {contador} = {resultado}")
#             contador += 1 


#         except ValueError:
#             print("Digite números")
#             break

# pares = 0
# impares = 0

# while pares < 3:
    
#     entrada = int(input("Digite números: "))

#     if entrada % 2 == 0:
#         print(f"{entrada} é par")
#         pares +=1

#     else:
#         print(f"{entrada} é ímpar")    
#         impares += 1

#     if pares == 3: #or impares == 3:
#         print("\nmáximo de número pares atingindo!!.")

# valor =  int(input("Digite valor: "))
# print(f"Multiplos de {valor} são: \n")

# for i in range(0, valor + 1 ,10):
#     print(i)

# letra = input("valor: ")

# import time


# for i in letra:
#     time.sleep(0.5)
#     print(i, end=" ")

# print("\n")  

# for i in letra: 
#     time.sleep(0.5)
#     print(i)

numero_vogais = 0
vogais = "aeiou"

nome = input("Digite: ").lower()

if nome in vogais:
    print("A frase começa com vogal")
 
else:
    print("A frase começa com Consoante")   

for letra in nome:
    if letra in vogais:
        numero_vogais += 1

print(f"Número de vogais na palavra: {numero_vogais}")




