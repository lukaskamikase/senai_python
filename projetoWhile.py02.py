

from os import system as limpar
limpar("cls") 
valor = int(input("Digite um número: "))

contador = 0

while contador <= 10:
    resultado = valor * contador
    print(f"{valor} * {contador} = {resultado}")
    contador += 1