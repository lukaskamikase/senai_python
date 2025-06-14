from os import system as limpar
limpas = ("cls")
from time import sleep
limpar("cls") 


nome = (input("Digite seu nome:"))
vog = ("a,e,i,o,u")

for i in nome:
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        print(i, end="")
   
   
     

