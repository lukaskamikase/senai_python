while True:

    x = int(input("digite sua idade: "))

    if x <= 12:
        print("voce se enquadra no grupo CRIANÇA" f"\nvoce tem {x} anos de idade")
        
    elif 13 <= x <= 17:
        print("voce se enquadra no grupo ADOLECESTE" f"\nvoce tem {x} anos de idade")

    elif 18 <= x <= 59:
        print("voce se enquadra no grupo ADULTO" f"\nvoce tem {x} anos de idade")

    elif 60 >= x:
        print("voce se enquadra no grupo IDOSO" f"\nvoce tem {x} anos de idade")
            
            
            

