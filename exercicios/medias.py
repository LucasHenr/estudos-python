import re
import sys
import logging

logging.basicConfig(filename = 'log.txt', format= '%(levelname)s-%(asctime)s-%(message)s', level=logging.DEBUG)

def executa():
    print("Menu: \n"
          "1. Média aritmética: \n"
          "2. Média ponderada: \n"
          "3. Sair\n")

    escolha_usuario = input("Escolha uma das opções: ")

    verifica_entrada = bool(re.match('^[0-3]$', escolha_usuario))

    logging.info(f"Escolha do usuário: {escolha_usuario}")
    
    if not verifica_entrada:
        print("Código inválido\n")
        executa()
    
    if escolha_usuario == '3':
        print("Programa encerrado!")
        sys.exit()

    primeiro_valor = input("Digite um valor: ")
    logging.info(f"Primeiro valor do usuário: {primeiro_valor}")

    segundo_valor =  input("Digite um valor: ")
    logging.info(f"Segundo valor do usuário: {segundo_valor}")

    validacao_valor1 = bool(re.match('^\d+$', primeiro_valor))
    validacao_valor2 = bool(re.match('^\d+$', segundo_valor))
    
    if not validacao_valor1:
        print("Valores/caracteres  inválidos")

    if not validacao_valor2:
        print("Valores/caracteres  inválidos")

    if escolha_usuario == '1':
        calcula_media(primeiro_valor, segundo_valor)
    
    if escolha_usuario == '2':
        peso1 = input("Digite o valor do peso: ")
        peso2 = input("Digite o valor do peso: ")

        validacao_peso1  = bool(re.match('^\d+$', peso1))
        validacao_peso2 = bool(re.match('^\d+$', peso2))

        if not validacao_peso1:
            print("Valores/caracteres  inválidos")
        
        if not validacao_peso2:
            print("Valores/caracteres  inválidos")
    
        calcula_media_ponderada(primeiro_valor, segundo_valor, peso1, peso2)


def calcula_media(primeiro_valor, segundo_valor):
        logging.info('iniciando calculo da média')
        media = (int(primeiro_valor) + int(segundo_valor)) / 2

        print(media)


def calcula_media_ponderada(primeiro_valor, segundo_valor, peso1, peso2):
    logging.info('iniciando calculo da média ponderada')
    if int(peso1 + peso2) == 0:

        logging.warning("Erro usuário, Náo é possível realizar divisão por zero")

    else:
        media_ponderada  = (int(primeiro_valor) * int(peso1) + int(segundo_valor) * int(peso2)) / int(peso1)+ int(peso2)
        
        print(media_ponderada)

executa()
        

    


    