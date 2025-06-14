from os import system as limpar
limpar("cls") 
 
nomes = ["maria","yasmin","katarina","jessica"]
print (f"Os nomes são: {nomes}")
#listas multaveis
nomes.append("Senai")
print (f"Os nomes são: {nomes}")


#tuplas sao nao multaveis, ou seja,
#nao podem ter seu valor alterado
idade = (17,18,20,25)
idade.append(19)
print(idade)


cidades = ["Sertãozinho","Pontal","Barrinha"]
print(cidades)

cidades.insert(1, "Ribeirão Preto")
print(cidades)
      