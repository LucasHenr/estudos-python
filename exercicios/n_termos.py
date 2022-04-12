def calcula_n():
    h = 0
    n = int(input("Digite o valor de n: "))

    for numero in range (1, 5):
        h = h + 1/n
    
    print(h)

calcula_n()