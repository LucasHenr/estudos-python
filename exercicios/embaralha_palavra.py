import random


def embaralha_palavra():
    palavra = input("Digite uma palavra ")
    resultado = ''.join(random.sample(palavra,len(palavra)))
    caixa_baixa = resultado.lower()
    return(caixa_baixa)

embaralha_palavra()
