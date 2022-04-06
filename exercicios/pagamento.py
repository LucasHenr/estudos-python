valor_prestacao = int(input("Qual valor da prestacao: "))
dias_em_atraso = int(input("Quantos dias de atraso: "))

def calcula_valor_pagamento(valor_prestacao, dias_em_atraso):

    if dias_em_atraso or valor_prestacao < 0:
        print("Informe valores positivos")

    if dias_em_atraso == 0:
        valor_total = valor_prestacao      

    if dias_em_atraso >=1:
        valor_total = valor_prestacao + (0.3 * valor_prestacao) + (0.01 * valor_prestacao)

    return valor_total

valor_pagamento = calcula_valor_pagamento(valor_prestacao,dias_em_atraso)
print(valor_pagamento)




        


