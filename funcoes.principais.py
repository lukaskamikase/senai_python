from os import system as limpar
limpar("cls") 

def operacoes():
    while True: 
        print("Escolha a operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        
        operacao = input("Digite o número da operação (1/2/3/4): ")
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if operacao == '1':
                print(f"{num1} + {num2} = {somar(num1, num2)}")
            elif operacao == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif operacao == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif operacao == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            else:
                print("Operação inválida!")
        
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

      
        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Saindo da calculadora... Até logo!")
            break
