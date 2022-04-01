
from traceback import print_tb


def calcula_fibonacci():
    limite_fibonaci =int(input("Digite o valor limite do fibonacci: "))
    valor_inicial = 1
    penultimo= 0
    ultimo = 0
    sequencia = []
    while valor_inicial <= limite_fibonaci:
        sequencia.append(valor_inicial)
        ultimo = valor_inicial + penultimo
        penultimo = valor_inicial
        valor_inicial = ultimo
    print(sequencia)
    
calcula_fibonacci()