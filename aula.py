from os import system as limp 
limp("cls")

while True:
        
    try:
             
        x = int(input("digite um valor"))

        if x > 0:
            print("o valor é maior que 0.")

        elif x == 0:
            print("valor é igual a 0")    

        elif x >= 0:
            print("valor é igual ou maior que 0") 

        elif x <= 0:
            print("valor é igual ou menor que 0")

        elif x < 0:
            print("valor menor que 0")        

        print("fim do programa")  

    except ValueError:  
        print("digite apenas numeros")
