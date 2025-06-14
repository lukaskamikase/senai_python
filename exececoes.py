from os import system as limpar
limpar("cls") 

def cadastro_de_produtos():

    produtos = []

    while True:
        try:
        
            nome = input("digite o nome do produto: ").lower()
            
            if nome == "sair":
                print("Saindo...")
                break

            if nome == "consultar":
                consulta = input("Digite o valor a ser pesquisado:\n").lower()

                for pesquisa in produtos:
                    if pesquisa['nome'] == consulta:

                        print("Produto Encontrado:\n ")
                        print(f"Nome: {pesquisa['nome']}, Preço: {pesquisa['preço']}, Quantidade: {pesquisa['quantidade']}\n")
                        continue
                    else:
                        print("Produto não encontrado")
                        break
                        

            preço = float(input("digite o preço do produto: "))
            quantidade = int(input("digite a quantidade: "))

            produto = { 'nome': nome,
                        'preço': preço,
                        'quantidade': quantidade}

            produtos.append(produto)

            print("\nProduto cadastrado")
            print(f"Nome: {nome}, Preço: {preço}, Quantidade: {quantidade}")


        except ValueError:
            print("digite números para PREÇO e QUANTIDADE")

cadastro_de_produtos()            
