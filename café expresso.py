opçao1 = "1 - CAFÉ EXPRESSO"
opçao2 = "2 - CAFÉ COM LEITE"
opçao3 = "3 - CAPPUCINO"
opçao4 = "4 - ÁGUA QUENTE"
opçao5 = "5 - LEITE PURO"

a = "1 - x-burger"
b = "2 - x-salada"
c = "3 - x-tudo"
d = "4 - x-bacon"
e = "5 - x-frango"
while True:
        print("*"*40 ) 
        print("*"*40 ) 
        print("*"*40 ) 
        print("*"*40 ) 
        print ("","CAFÉ's SENAI", "", sep="*"*14)
        print ("\nESCOLHA UMA BEBIDA ABAIXO:")
        print("\n",opçao1,"\n",opçao2,"\n",opçao3,"\n",opçao4,"\n",opçao5)


        try:
                
                opção = int(input("digite a opção desejada: "))

                if opção == 1:
                        print("opção selecionada: café expresso")

                elif opção == 2:
                        print("opção selecionada: café com leite")

                elif opção == 3:
                        print("opção selecionada: cappuccino")

                elif opção == 4:
                        print("opção selecionada: água quente")    

                elif opção == 5:
                        print("opção selecionada: leite puro")    
                        
                elif opção == 75452:
                        print("*"*40 ) 
                        print("*"*40 ) 
                        print("*"*40 ) 
                        print("*"*40 ) 
                        print ("","MENU SECRETO", "", sep="*"*14)
                        print ("\nESCOLHA SEU LANCHÃO:")
                        print("\n",a,"\n",b,"\n",c,"\n",d,"\n",e)
                                
                        ped = int(input("selecione seu item secreto: "))
                        
                        if ped == 1:
                                print("opção selecionada: X-BURGUER  ")
                        elif ped == 2:
                                print("opção selecionada: X-SALADA ")    

                        elif ped == 3:
                                print("opção selecionada: X-TUDO")  

                        elif ped == 4:
                                print("opção selecionada: X-BACON ")     

                        elif ped == 5:
                                print("opção selecionada: X-FRANGO")     
                        
                        else:
                                print("por favor selecione uma das opçoes acima")          

                else:
                        print("por favor selecione uma das opçoes acima")

        except ValueError:
                print("digite apenas números")
                
        input("aperte enter para continuar")

  

