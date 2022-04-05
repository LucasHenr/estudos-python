texto = input("Digite o texto aqui: ")

def obtem_quantidade_espaco_branco():
    espaco_em_branco = texto.count(" ")

    print(f"{espaco_em_branco} espaco/espacos vazios")

def obtem_quanditade_vogais(texto):
    quantidade_vogais = 0
    vogais = ['a','e','i','o','u']

    for letra in texto:
        if letra in vogais:
            quantidade_vogais += 1

    print(f"Possui {quantidade_vogais} vogais")

obtem_quanditade_vogais(texto)
obtem_quantidade_espaco_branco()

    