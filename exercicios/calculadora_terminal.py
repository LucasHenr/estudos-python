import sys

def calculadora():
    if len(sys.argv) <= 3:
        print("Para continuar informe dois valores e uma opcao de conta")
    
    else:
        valor1 = int(sys.argv[1])
        valor2 = int(sys.argv[2])
        opcao =  int(sys.argv[3])

        if opcao == 1:
            adicao(valor1,valor2)
        
        if opcao == 2:
            subtracao(valor1,valor2)
        
        if opcao == 3:
            multiplicacao(valor1,valor2)
        
        if opcao == 4:
            divisao(valor1,valor2)
    
def adicao(valor1,valor2):
    adicao = valor1 + valor2

    print(adicao)

def subtracao(valor1,valor2):
    subtracao = valor1 - valor2

    print(subtracao)

def multiplicacao(valor1,valor2):
    multiplicacao = valor1 * valor2

    print(multiplicacao)

def divisao(valor1,valor2):
    if valor2 == 0:
        print("Não é possível dividir por 0")
    
        return
        
    divisao = valor1 / valor2
    divisao_formatada = round(divisao, 2)

    print(divisao_formatada)


calculadora()


