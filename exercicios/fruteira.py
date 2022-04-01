def calcula_valor_morango(quantidade_morango):
    if quantidade_morango < 5:
        preco_morango = 2.50
    else:
        preco_morango = 2.20
    valor_morango = quantidade_morango * preco_morango
    return valor_morango 

def calcula_valor_maca(quantidade_maca):
    if quantidade_maca < 5:
        preco_maca = 1.80
    else:
        preco_maca = 1.50
    valor_maca = quantidade_maca * preco_maca
    return valor_maca

def calcula_valor_total():
    quantidade_morango = int(input("Digite a quantidade (kg) de morango ")) 
    quantidade_maca = int(input("Digite a quantidade (kg) de maca "))
    quantidade = quantidade_maca + quantidade_morango
    valor_morango = calcula_valor_morango(quantidade_morango)
    valor_maca = calcula_valor_maca(quantidade_maca)
    valor_total = valor_morango + valor_maca
    if quantidade > 8 or valor_total >25.00:
        valor_total = valor_total - (valor_total * 0.10)
    print(valor_total)

calcula_valor_total()




         
    



