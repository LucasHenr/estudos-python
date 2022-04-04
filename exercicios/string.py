texto = input("Digite o texto aqui: ")

def obtem_quantidade_espaco_branco():
    espaco_em_branco = texto.count(" ")

    print(f"{espaco_em_branco} espaco/espacos vazios")

def obtem_quanditade_vogais(texto):
    vogais = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}
    for letra, quantidade in vogais.items():
        if letra in texto:
            quantidade = quantidade +1
        print(letra, quantidade)

obtem_quanditade_vogais(texto)

    