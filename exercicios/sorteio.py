from random import randint
maquina = randint(10,26)
print("Pensei em um número entre 10 e 26.... Acha que consegue adivinhar? ")
certo = False
tentativas = 0 
while not certo:
    jogador = input("Digite seu palpite")
    tentativas +=1
    if int(jogador) == maquina:
        print("Parabéns você acertou")
        certo = True

print("Programa encerrado")
