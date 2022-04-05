import re

texto = input("Digite um texto: ")

def obtem_quantidade_vogal(texto):
    vogais = re.findall('[aeiou]', texto, re.IGNORECASE)
    return len(vogais)

print(f"Possui {obtem_quantidade_vogal(texto)} vogais")

