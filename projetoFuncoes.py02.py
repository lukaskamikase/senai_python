from os import system as limpar
limpar ("cls")

from os import system as limp
limp("cls")

def circ(num1):
    A = 3.14 * (num1 ** 2)
    return A

def quad(num1):
    A = num1 * num1
    return A

def triang(num1,num2):
    A = (num1 * num2)/2
    return A

def triret(num1,num2):
    A = (num1 * num2)/2
    return A

def ret(num1,num2):
    A = num1 * num2
    return A

def elipse(num1,num2):
    A = num1 * num2 * 3.14
    return A

print("SELECIONE UM CÁLCULO ABAIXO:")
print("1 - Circulo")
print("2 - Quadrado")
print("3 - Triângulo")
print("4 - Triângulo Retângulo")
print("5 - Retângulo")
print("6 - Elipse")

while True:

    opcao = input("Digite aqui a operação desejada: ")
    
    if opcao == "1":
        raio = float(input("Digite o raio: "))
        area = circ(raio)

    elif opcao == "2":
        lado = float(input("Digite o lado: "))
        area = quad(lado)

    elif opcao == "3":
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        area = triang(base,altura)

    elif opcao == "4":
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        area = triret(base,altura)

    elif opcao == "5":
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        resultado = ret(base,altura)

    elif opcao == "6":
        R = float(input("Digite o raio menor: "))
        r = float(input("Digite o raio maior: "))
        resultado = elipse(R,r)

    else:
        print("Selecione uma opção válida.")

    print(f"A área é: {resultado}")
    input("Pressiona Enter para continuar")