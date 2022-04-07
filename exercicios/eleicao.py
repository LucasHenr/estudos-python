def menu():
        print("Candidatos: \n"
        "Jõao - 1\n"
        "Zé - 2\n"
        "Marcos - 3\n"
        "Matheus - 4\n"
        "Nulo - 5\n"
        "Branco - 6\n")
    
def votacao():
    quantidade_votos = 0
    urna = []
    while quantidade_votos < 6:
        voto = input("Digite em quem deseja votar: ")
        quantidade_votos = quantidade_votos + 1
        urna.append(voto)

    else:
        print("Votacao encerrada")

    return urna

def calcula_candidato_eleito(urna):
    porcentagens = []
    candidatos = {
        '1': 'João',
        '2':  'Zé',
        '3': 'Marcos',
        '4': 'Matheus',
        '5': 'Nulo',
        '6': 'Branco'
    }

    for numero,candidato in candidatos.items():
        quantidade_votos = urna.count(numero)

        porcentagem_candidato = (quantidade_votos / len(urna) * 100)
        porcentagem_formatada = round(porcentagem_candidato,2)
        porcentagens.append(porcentagem_formatada)
        
    candidato_mais_votos = max(porcentagens)
    
    if candidato_mais_votos < 50:
        porcentagens.sort(reverse = True)
        segundo_turno = porcentagens[1]

        print("Será necessário segundo turno")
    
def simula_votacao():
    menu()
    votos = votacao()
    calcula_candidato_eleito(votos)
       
simula_votacao()
        










