from os import system as limpar
from time import sleep
limpar("cls") 

vezes = 0

while vezes < 20:
    print(f"Numero de vezes: {vezes}")
    vezes += 1
    sleep(1)


