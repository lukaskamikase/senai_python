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

a = 5
b = 10

print("Soma:",somar(a, b))
print("Subtração:", subtrair(a, b))
print("Multiplicação:", multiplicar(a, b))
print("Divisão:", dividir(a, b))