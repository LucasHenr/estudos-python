def exibe_numero_reverso(numero):
    numero_invertido = (numero)[::-1]
    
    return numero_invertido

numero = input("Digite um número: ")
numero_reverso = exibe_numero_reverso(numero)

print(numero_reverso)
