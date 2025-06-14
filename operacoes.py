from os import system as limpar
limpar("cls") 


def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a,b):
    return a * b

def div(a, b):
     if b == 0:
        return "Erro: Divisão por zero!"
     return a / b

import operacoes

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Soma:",soma(a, b))
print("Subtração:",sub(a, b))
print("Multiplicação:",mult(a, b))
print("Divisão:",div(a, b))