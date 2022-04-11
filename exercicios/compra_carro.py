def compra_a_vista():
    valor_a_vista = preco_carro - (preco_carro * 0.20)

    print(f"Valor a vista: {valor_a_vista} ") 

def compra_parcelada():
    numero_parcela = 6
    percentual_porcentagem  = 3

    print(f" 6x,  3%,  {(preco_carro + preco_carro * 0.03)}   \n",
          f"12x, 6%,  {(preco_carro + preco_carro * 0.06)}  \n",
          f"18x, 9%,  {(preco_carro + preco_carro * 0.09)}  \n",
          f"24x, 12%, {(preco_carro + preco_carro * 0.12)} \n", 
          f"30x, 15%, {(preco_carro + preco_carro * 0.15)} \n",
          f"36x, 18%, {(preco_carro + preco_carro * 0.18)} \n",
          f"42x, 21%, {(preco_carro + preco_carro * 0.21)} \n",
          f"48x, 24%, {(preco_carro + preco_carro * 0.24)} \n",
          f"54x, 27%, {(preco_carro + preco_carro * 0.27)} \n",
          f"60x, 30%, {(preco_carro + preco_carro * 0.30)} \n")

    '''for parcela in range(1,10):
       print(numero_parcela +=3, percentual_porcentagem += 3, preco_carro + (preco_carro * 0.03))
       '''

preco_carro = float(input("Qual o valor do carro? "))
compra_a_vista()
compra_parcelada()




