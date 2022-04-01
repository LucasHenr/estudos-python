def calcula_total_pao():
    sequencia = []
    valor_pao = float(input("Digite o preco do pão: "))
    
    for valor in range(50):
        valor_total = (valor_pao * valor)
        valor_formatado = round(valor_total,2)
        sequencia.append(valor_formatado)

    print(sequencia)

calcula_total_pao()

