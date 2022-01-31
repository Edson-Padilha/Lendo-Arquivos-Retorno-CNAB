#Author: Edson Padilha


# import kivy
# kivy.require("1.9.1")
# from kivy.app import App

cont = 0


print("="*50 )
print(f"RETORNO C6".center(50))
print("="*50 )

arq = open("270122.txt")
linhas = arq.readlines()


for col in linhas:
    cont = cont + 1  
    ir = str(col[0])#Identificador de registro
    tie = str((col[2],col[3]))#Tipo de inscrição da empresa

    
    if ir == "1":
        rt =  "Registro de Transação"
#VALIDANDO TIPO DE INSCRIÇÃO DA EMPRESA
    if tie == "1":
        t = "CPF"

    elif tie == "2":
        t = "CNPJ"

    elif tie == "3":
        t = "PIS/PASEP"

    elif tie == "98":
        t = "NÃO TEM"

    elif tie == "99":
        t = "OUTROS"
 


    ocorrencia = str(col[108]+col[109])

    if cont != 1:        
        print(f"{rt} - {t}")
        print(f"Linha : {cont} - Ocorrência: {ocorrencia}")
        print("-"*50)

print(f"Total de colunas: {len(col)}")#Conta a quantidade de colunas
if len(col) > 400:
    print(f"Quantidade de colunas excedente no arquivo. Linha: {cont -1}")
print(f"Total de documentos: {cont - 1}")#Total de registros no retorno

class RetornoApp(App):
    pass

janela = RetornoApp()
janela.run()