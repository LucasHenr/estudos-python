def calcula_cedula():
    valor_saque = int(input("Qual valor você deseja sacar? "))
    cedulas = [100,50,10,5,1]
    valor_total = valor_saque
    quantidade_nota_100 = 0
    quantidade_nota_50 = 0
    quantidade_nota_10 = 0
    quantidade_nota_5 = 0
    quantidade_nota_1 = 0

    for valor in cedulas:
        if valor_total >= valor:
            valor_total = valor_total - valor
        if valor == 100:
            quantidade_nota_100 = quantidade_nota_100 + 1
        if valor == 50:
            quantidade_nota_50 = quantidade_nota_50 + 1
        if valor == 10:
            quantidade_nota_10 = quantidade_nota_10 + 1
        if valor == 5:
            quantidade_nota_5 = quantidade_nota_5 + 1
        if valor == 1:
            quantidade_nota_1 = quantidade_nota_1 + 1
        while valor <= valor_total:
            valor_total = valor_total - valor
            if valor == 100:
                quantidade_nota_100 = quantidade_nota_100 + 1
            if valor == 50:
                quantidade_nota_50 = quantidade_nota_50 + 1
            if valor == 10:
                quantidade_nota_10 = quantidade_nota_10 + 1
            if valor == 5:
                quantidade_nota_5 = quantidade_nota_5 + 1
            if valor == 1:
                quantidade_nota_1 = quantidade_nota_1 + 1
        else:
            continue
            
    print(f" Foi necessário {quantidade_nota_100} notas de 100, {quantidade_nota_50} nota/notas de 50, {quantidade_nota_10} nota/notas de 10, {quantidade_nota_5} nota/notas de 5 e {quantidade_nota_1} nota de 1")

   
calcula_cedula()






    

    




















    

















        


    
    

