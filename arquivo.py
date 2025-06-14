from os import system as limpar
limpar("cls") 

#with open("dados.txt", "r") as arquivo:
  # conteudo = arquivo.read() 
#print(conteudo)  

with open("dados.txt", "a") as arquivo:
    arquivo.write("Salvando dados no arquivo\n")   