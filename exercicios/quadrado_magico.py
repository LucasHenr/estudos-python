def gerar_quadrado_magico(linhas):
    quadrado_magico = [[0 for x in range(linhas)]
                          for y in range(linhas)]

    linha = linhas / 2
    colunas = linhas -1
    numero = 1

    while numero <= (linhas * linhas):
        if linha == -1 and colunas == linhas:
            colunas = linhas -2
            linha = 0
        
        else:

            if colunas == linhas:
                colunas == 0

            if linha < 0:
                linha = linhas -1

        if quadrado_magico[int(linha),int(colunas)]:
            colunas = colunas -2
            linha = linha +1

            continue
        
        else:
            quadrado_magico[linha,colunas] = numero
            numero = numero +1
        
        colunas = colunas +1
        numero = numero -1

    print("Quadrado mágico do número: ", quadrado_magico)
    print(numero * (numero * numero + 1) / 2)
    for linha in range(0, numero):
        for coluna in range(0, numero):
            print('%2d' % (quadrado_magico[linha][coluna]), end = '')

            if coluna == numero - 1:
                print()

linhas = int(input("Número de linhas do quadrado mágico: "))
gerar_quadrado_magico(linhas)


