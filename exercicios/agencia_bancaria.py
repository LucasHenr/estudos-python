import re

def recebe_conta():
    tipo_conta = input("Informe o seu tipo de conta: \n"
                           "1 - Poupanca \n"
                           "2 - Poupanca Plus \n"
                           "3 - Fundos de renda fixa \n"
                           "Digite o tipo da sua tipo_conta: ")

    verifica_id_conta = re.match("[1-3]+", tipo_conta)

    if verifica_id_conta is None:
        print("Código inválido")
    
    else:
        return tipo_conta
        
def calcula_rendimento_mensal(tipo_conta):
    valor_investido = float(input("Digite o valor a ser investido: "))
    rendimento_mensal = 0
    
    if tipo_conta == '1':
        rendimento_mensal = valor_investido + (valor_investido * 0.015)
    
    if tipo_conta == '2':
        rendimento_mensal = valor_investido + (valor_investido * 0.02)

    if tipo_conta == '3':
        rendimento_mensal = valor_investido + (valor_investido * 0.04)

    return rendimento_mensal

def executa():
    print('Iniciado cálculo de rendimento mensal\n')

    conta = recebe_conta()
    if conta is not None:
        rendimento_mensal = calcula_rendimento_mensal(conta)

        print(f"O rendimento mensal foi de: {rendimento_mensal}")

    else:
        print("Para verificar o seu rendimento é necessário informar uma conta válida")
    

executa()

