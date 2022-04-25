import random

NAIPES = '♠ ♥ ♦ ♣'.split()
CARTAS = 'A 2 3 4 5 7 8 9 K J Q'.split()

def criar_baralho(aletatorio = False):
    baralho =  [(naipe,c) for c  in CARTAS for naipe in NAIPES ]

    if aletatorio:
        random.shuffle(baralho)
    
    return baralho

def distribuir_carta(baralho):
    return (baralho [0::4],  baralho [1::4], baralho [2::4], baralho [3::4])

def jogar():
    cartas = criar_baralho(aletatorio= True)
    jogadores = ' Jogador1 Jogador2 Jogador3 Jogador4'.split()
    maos = {j : mao for j, mao in zip(jogadores, distribuir_carta(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{jogadores}{cartas}" for (jogadores, cartas) in cartas)
        
        print(f"{jogador}: {carta}")

jogar()