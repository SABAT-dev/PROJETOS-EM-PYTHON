#QUESTÃO 3:
for voto in range(5):
    nome = str(input(f"Informe o nome do {voto + 1}º participante: ")).strip()
    nota = float(input(f"Informe a nota do {voto + 1}º participante: "))
    
    #CONDIÇÃO:
    if nota >= 0 and nota <= 10:
        print()
        if voto == 0 or nota > nota_vencedor:
            vencedor = nome
            nota_vencedor = nota
    else:
        quit()

print(f"O(a) vencedor(a) foi {vencedor} com nota {nota_vencedor}")