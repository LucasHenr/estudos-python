def calcula_media():
    idade_alunos = []
    for idade in range(6):
        idade_alunos.append(int(input("Digite a sua idade: ")))
        media_idade = sum(idade_alunos)/len(idade_alunos)
        media_formatada = round(media_idade,2)
    if media_idade >= 60:
        print("Turma de idosos")
    elif media_idade > 26:
        print("Turma de adultos")
    else:
        print("Turma de jovens")
    print(media_formatada)

calcula_media()






