from datetime import datetime

def converte_horario(hora):
    horario = datetime.strptime(hora, '%H:%M')

    return datetime.strftime(horario, '%I:%M %p')

hora = input("Informe a hora no formato 00:00: " )
hora_formatada = converte_horario(hora)

print(hora_formatada)