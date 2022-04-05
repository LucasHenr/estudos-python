import re


def obtem_quantidade_vogal():
    texto = input("Digite um texto: ")

    vogais = re.findall('[aeiou]', texto, re.IGNORECASE)

    print(f"Possui {len(vogais)} vogais")

    return len(vogais)

obtem_quantidade_vogal()

