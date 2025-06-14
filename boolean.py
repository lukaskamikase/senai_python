while True:

    from os import system as limp 
    limp ("cls")


    try:
        x, y = map(int,input("digite os valor nesse formato xx xx: ").split(','))

        if x > y:
            print("primeiro valor é maior")

        elif x < y:
            print("segundo valor é maior")

        elif x == y:
            print("valores iguais")
    
    except ValueError:
        print("digite apenas numeros, ou insira dois valores ")

    except:
        print("use ',' para separar os valores")