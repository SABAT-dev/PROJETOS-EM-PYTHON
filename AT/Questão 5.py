def extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        arquivo = open(caminho_arquivo, encoding='utf8')
        recheio = arquivo.read()

    anos = []

    recheio = recheio.splitlines()
    países = recheio[0]
    países = países.split(',')

    recheio = recheio[1:]
    dados = []

    for parte in recheio:
        parte = parte.split(',')
        dados.append(parte)

    for i in range(8):
        anos.append(dados[i][0])

    return países, dados, anos

extrair_dados('Assessment_PIBs - modelo 2.csv')

#LETRA A:
from time import sleep
def pib_país(país, ano):
    países, dados, anos = extrair_dados('Assessment_PIBs - modelo 2.csv')
    if país not in países:
        print("País não disponível")
        print("\033[1;31;40mTente novamente!\033[m")
        quit()    
    if ano not in anos:
        print("Ano não disponível")
        print("\033[1;31;40mTente novamente!\033[m")
        quit()
    indice_país = países.index(país)
    indice_ano = anos.index(ano)

    print(f"PIB \033[1;31m{país}\033[m em \033[1;31m{ano}\033[m: \033[1;31mUS${dados[indice_ano][indice_país]}\033[m trilhões.\n")

print("\033[1;33m*+*\033[m" * 15)
país = input("\033[1;33;41mInforme um País:\033[m ")
ano = input("\033[1;33;41mInforme um ano entre 2013 e 2020:\033[m ")
print("\033[1;33m*+*\033[m" * 15)
pib_país(país, ano)
sleep(2)
print("\033[7;35;40m PROCESSANDO INFORMAÇÕES...\033[m")
print("\n")

#LETRA B:
def estimativa_variação_pib():
    países, dados, anos = extrair_dados('Assessment_PIBs - modelo 2.csv')
    contador = 1
    for z in países[1:]:
        pib1 = float(dados[0][contador])
        pib2 = float(dados[7][contador])
        contador = contador + 1
        var_pib = (pib2 / pib1 - 1) * 100
        print(f"\033[1;30;42m{z:<10}\033[m Variação de \033[1;30;46m{var_pib:.2f}%\033[m entre 2013 e 2020")
        
estimativa_variação_pib()

#LETRA C:
from matplotlib import pyplot as plt
def evolução_pib(país):
    países, dados, anos = extrair_dados('Assessment_PIBs - modelo 2.csv')

    lista_ranking = []
    indice = países.index(país)
    for i in range(8):
        lista_ranking.append(float(dados [i][indice]))
    plt.title("Gráfico da evolução do valor do PIB")
    plt.xlabel("Anos")
    plt.ylabel("Valores do PIB")
    plt.plot(anos, lista_ranking)
    plt.show()  

sleep(2)
print("\n")
print("\033[7;35;40m PROCESSANDO INFORMAÇÕES FINAIS...\033[m")
print("\n")
print("\033[1;33m*+*\033[m" * 15)
país = str(input("\033[1;33;41mInforme um país:\033[m ")).strip()
print("\033[1;33m*+*\033[m" * 15)
sleep(1)
print("\n")
print("\033[7;35;40m GERANDO GRÁFICO...\033[m")

evolução_pib(país)