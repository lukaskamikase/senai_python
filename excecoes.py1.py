from os import system as limpar
limpar("cls") 

num1 = None
num2 = None
res = None


while True:
   
    try:
        num1 = int(input("digite um valor:\n"))
        num2 = int(input("digite um valor:\n"))
        res = num1 / num2
        print(f"O resultado é {res}.")

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")

