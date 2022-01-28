
cont = 0

print("="*50 )
print(f"RETORNO C6".center(50))
print("="*50 )

arq = open("270122.txt")
linhas = arq.readlines()


for col in linhas:
    cont = cont + 1  
   
    ocorrencia = str(col[108]+col[109])

    if cont != 1:
        print(f"Linha : {cont} - Ocorrência: {ocorrencia}")
        print("-"*50)

print(f"Total de documentos: {cont - 1}")