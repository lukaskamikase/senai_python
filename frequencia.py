while True:

    try:
        x = int(input("digite a note do aluno: "))
        y = int(input("digite a frequencia do aluno: "))

        if x < 0 :
            print(f"digite um valor para nota entre 0 a 10, e para frequência de 0 a 100")
        
        if x > 10:
            print(f"digite um valor para nota entre 0 a 10, e para frequência de 0 a 100")

        elif x >= 7 and y >= 75 and x :
            print(f"aprovado pela nota {x} e pela frequência {y}%")

        if y > 100:
            print(f"digite um valor para nota entre 0 a 10, e para frequência de 0 a 100") 

        if y < 0:
            print(f"digite um valor para nota entre 0 a 10, e para frequência de 0 a 100")       
 
        elif x > 10 and x  < 0:
            print("digite um valor entre 0 a 10")
        
        elif x < 7 and y < 75:
            print(f"reprovado pela nota {x} e pela frequência {y}%")

        elif x >= 7 and y < 75:
            print(f"aprovado pela nota {x}, mas reprovado por conta da frequência {y}%")    

        elif x < 7 and y >= 75:
            print(f"aprovado pela frequência {y} mas, reprovado por conta da nota {x}")    

    except ValueError:
        print("digite apenas numeros")


