from os import system as limpar
limpar ("cls")

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("Opção 1: soma")
print("Opção 2: subtração")
print("Opção 3: divisão")
print("Opção 4: multiplicação")

opção = int(input("Digite uma opção de 1 a 4: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opção == 1:
    resultado = soma(num1, num2)
    print(f"O resultado da soma é: {resultado}")
elif opção == 2:
    resultado = sub(num1, num2)
    print(f"O resultado da subtração é: {resultado}")
elif opção == 3:
    resultado = div(num1, num2)
    print(f"O resultado da divisão é: {resultado}")
elif opção == 4:
    resultado = mult(num1, num2)
    print(f"O resultado da multiplicação é: {resultado}")
