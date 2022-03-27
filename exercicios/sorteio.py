from random import randint
tentativas = 5
numeros = [14,19,23]

while tentativas >=1:
    instrucao = input("Deseja jogar o dado (s/n)?")
    numero_sorteado = randint(10,26)
    print(f"Número sorteado {numero_sorteado}")
    if numero_sorteado in numeros:
        tentativas += 3
        print(f"Você acertou e tem {tentativas} tentativas")
        
    else:
        tentativas -= 1
        print(f"Você errou e tem {tentativas} tentativas")
    
    if tentativas == 0:
        print("GAME OVER")
        break
    