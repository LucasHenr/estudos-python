import time

def calcula_soma(valor1,valor2,valor3):
    soma = valor1 + valor2 + valor3

    return soma

resultado = calcula_soma(2,4,5)

print(resultado)

def soma_imposto(imposto, valor):
    valor_produto = (imposto * valor) + valor 

    return valor_produto

resultado = soma_imposto(0.20,100)

print(f"R$ {resultado} reais")







        

