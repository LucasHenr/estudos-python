def recebe_numeros():
    numeros = []
    quantidade_numeros = 0

    while quantidade_numeros < 10:
        numero = int(input("Digite um número: "))
        quantidade_numeros = quantidade_numeros + 1
        numeros.append(numero)
        
    return numeros

def calcula_numeros_menores_35(numeros):
    quantidade_menores_35 = 0

    for numero in numeros:
        if numero < 35:
            quantidade_menores_35 = quantidade_menores_35 + 1
    
    print(f"{quantidade_menores_35} números inferiores a 35")


def calcula_media_positivos(numeros):
    quantidade_numeros_positivos = 0
    soma_valores = 0

    for numero in numeros:
        if numero > 0:
            soma_valores = soma_valores + numero
            quantidade_numeros_positivos = quantidade_numeros_positivos + 1
        
        media_positivos =  soma_valores / quantidade_numeros_positivos
        media_formatada = round(media_positivos, 2)

    print(f"A média dos números positivos {media_formatada}")

def porcentagem_numeros_entre_50_100(numeros):
    quantidade_numeros_entre_50_100 = 0

    for numero in numeros:
        if numero >= 50 and numero < 100:
            quantidade_numeros_entre_50_100 = quantidade_numeros_entre_50_100 + 1

        porcentagem = (quantidade_numeros_entre_50_100 / 10) * 100
        porcentagem_formatada = round(porcentagem, 2)

    print(f"A porcentagem de números entre 50 e 100 é de: {porcentagem_formatada}%")

def porcentagem_10_20_entre_menores_50(numeros): 
        quantidade_entre_10_20 = 0
        menores_50 = []

        for numero in numeros:
            if numero < 50:
                menores_50.append(numero)

        #ESTUDAR LIST COMPREHENSION
        #menores_50 = [numero for numero in numeros if numero < 50]
        
        for valor in menores_50:
            if valor >= 10 and valor <=20:
                quantidade_entre_10_20 = quantidade_entre_10_20 +1
        
        porcentagen = (quantidade_entre_10_20 / len(menores_50)) * 100
        porcentagem_formatada = round(porcentagen,2)

        print(f"A porcentagem de números entre 10 e 20, menores que 50 é de: {porcentagem_formatada}%")
        

def executa():
    entradas = recebe_numeros()
    calcula_numeros_menores_35(entradas)
    calcula_media_positivos(entradas)
    porcentagem_numeros_entre_50_100(entradas)
    porcentagem_10_20_entre_menores_50(entradas)

executa()