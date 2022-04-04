def calcula_cedula():
    valor_saque = int(input("Qual valor você deseja sacar? "))
    cedulas = [100,50,20,10,5,1]
    contador = 0

    for valor_nota in cedulas:
        while valor_saque >= valor_nota:
            valor_saque = valor_saque - valor_nota
            contador = contador + 1
        
        if contador != 0:
            print(f"{contador} nota/notas de {valor_nota}")

        contador = 0

calcula_cedula()
    