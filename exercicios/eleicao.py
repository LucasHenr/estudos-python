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
    candidatos = {
        '1': 'Jo'
    }

    
def simula_votacao():
    menu()
    votos = votacao()

       
simula_votacao()
        


'''def obtem_candidato_eleito(urna):
    votos_candidato1 = urna.count(1)
    votos_candidato2 = urna.count(2)
    votos_candidato3 = urna.count(3)
    votos_candidato4 = urna.count(4)
    votos_nulo = urna.count(5)
    votos_branco = urna.count(6)
    porcentagem_candidato1 = (urna.count(1) / len(urna)) * 100

    print(porcentagem_candidato1)
'''






