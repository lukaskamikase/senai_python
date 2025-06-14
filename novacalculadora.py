from os import system as limp 
limp("cls")

while True:
    

    try:
        a, c, b = input("valor a ser calculado: ").split()
        a = float(a)
        b = float(b)

        if c == "+":
            soma = a + b
            print("valor da soma: ", soma)
            
        elif c == "-":
            sub = a - b
            print("valor da Subtração: ", sub)

        elif c == "*":
            mult = a * b
            print("valor da Multiplicação: ", mult)

        elif c == "/":
            div = a / b
            print("valor da divisão: ", div)    

        elif c == "**":
            exp = a ** b
            print("valor da exponenciação: ", exp)
            
        else:
            print("Por Favor Digite Uma Das Seguintes Operações: +, -, , /, *.")

    except ValueError:
        print("valor invalido, digite apenas números!!!")

    except ZeroDivisionError:
        print("impossivel dividir por zero")

    except:
        print("erro inesperado")