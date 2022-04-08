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
        voto = int(input("Digite em quem deseja votar: "))
        if voto >= 7:
            print("Código de candidato inválido, digite outro código")
            continue
        quantidade_votos = quantidade_votos + 1
        urna.append(voto)

    else:
        print("Votacao encerrada")

    return urna

def calcula_candidato_eleito(urna):
    candidatos = {
        '1': 'João',
        '2':  'Zé',
        '3': 'Marcos',
        '4': 'Matheus',
        '5': 'Nulo',
        '6': 'Branco'
    }

    resultado_final = calcula_voto(urna,candidatos)

    if resultado_final[0][0] < 50:
        print(f"{resultado_final[0][1]} e {resultado_final[1][1]} estão no segundo turno")
        segundo_turno(urna,candidatos)

    else:
        print(f"{resultado_final[0][1]}, ELEITO")
    
def segundo_turno(urna, candidatos):
        
        votacao()

        resultado_votacao = calcula_voto(urna, candidatos)

        resultado = resultado_votacao[0][1]
        print(f"{resultado}, ELEITO")
        
def calcula_voto(urna, candidatos):
    resultado_final = []

    for numero, candidato in candidatos.items():         
        quantidade_votos = urna.count(numero)

        porcentagem_candidato = (quantidade_votos / len(urna) * 100)
        porcentagem_formatada = round(porcentagem_candidato,2)

        resultado_candidato = (porcentagem_formatada, candidato,numero)
        
        resultado_final.append(resultado_candidato)
  
    resultado_final.sort(reverse = True)

    return resultado_final

def simula_votacao():
    menu()
    votos = votacao()
    calcula_candidato_eleito(votos)
       
simula_votacao()
        










