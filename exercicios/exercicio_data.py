import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')

def converte_data(data):
    data_texto = datetime.strptime(data, '%d/%m/%Y')

    return datetime.strftime(data_texto, '%d de %B de %Y')

data = input("Forneca a data no valor DD/MM/YYYY: ")
data_formata = converte_data(data)

print(data_formata)