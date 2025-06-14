# a = int(input("digite sua pressão"))
b = float(input("digite sua temperatura: "))
# c = int(input("digite seus batimentos cardiacos por minuto"))


if b < 35:
    print(f"temperatura abaixo de {b}°C HIPOTERMIA PROCURE UM MEDICO")

elif b >= 35 and b <= 36.5:
    print(f"temperatura normal {b}°C")

elif b >= 36.6 and b <= 39:
    print(f"temperatura de {b}°C FEBRE LEVE")

elif b > 39:
    print(f"Temperatura de {b}°C FEBRA ALTA PROCURE UM MEDICO")
    
