import re

def executa():
    print("Menu: \n"
          "1. Média aritmética: \n"
          "2. Média ponderada: \n"
          "3. Sair\n")

    escolha_usuario = input("Escolha uma das opções: ")

    primeiro_valor = int(input("Digite um valor: "))
    segundo_valor = int(input("Digite um valor: "))

    verifica_valores = re.match('/\d', primeiro_valor,segundo_valor)

    if escolha_usuario == '1':
        calcula_media(primeiro_valor, segundo_valor)
    
    if escolha_usuario == '2':
        peso1 = int(input("Digite o valor do peso: "))
        peso2 = int(input("Digite o valor do peso: "))

        verifica_peso = re.match('/\d', peso1,peso2)
        
        calcula_media_ponderada(primeiro_valor, segundo_valor, peso1, peso2)

def calcula_media(primeiro_valor, segundo_valor):
        media = (primeiro_valor + segundo_valor) / 2

        print(media)

def calcula_media_ponderada(primeiro_valor, segundo_valor, peso1, peso2):
    if peso1 + peso2 == 0:
        print("Não é possível dividir por 0")

    else:
        media_ponderada  = (primeiro_valor * peso1 + segundo_valor * peso2) / (peso1 + peso2)
        
        print(media_ponderada)

executa()
        

    


    