#FUNÇÃO - (LETRA A):
from time import sleep
def calcular_juros_compostos(valor_inicial, rendimento, aporte, períodos):
    m = []
    mm = []

    #CONDICIONAIS ADICIONAIS; 
    if valor_inicial != 10000:
        print("\033[1;31mErro, digite novamente!\033[m")
        quit()
    elif rendimento != 0.54:
        print("\033[1;31mErro, digite novamente!\033[m")
        quit()
    elif aporte != 1000:
        print("\033[1;31mErro, digite novamente!\033[m")
        quit()
    elif períodos != 120:
        print("\033[1;31mErro, digite novamente!\033[m")
        quit()   

    #LAÇO DE REPETIÇÃO:
    for p in range(períodos):
        valorização =  (rendimento / 100 * valor_inicial ) + valor_inicial
        valorização_aporte = valorização + aporte                
        print(f"Após \033[7;34;40m{p + 1}º\033[m período(s), o montante será de \033[7;34;40mR${valorização_aporte:.2f}\033[m")
        valor_inicial = valorização_aporte
        m.append(p + 1)
        mm.append(valor_inicial)
    sleep(1)
    print("\n")
    print("\033[7;35;40mGERANDO GRÁFICO...\033[m")

    #LETRA B:
    def gráfico_evolução():
        from matplotlib import pyplot as plt
        plt.title("Gráfico da evolução do valor acumulado")
        plt.xlabel("Períodos")
        plt.ylabel("Valor acumulado")
        plt.plot(m, mm)
        plt.show()

    gráfico_evolução()

#BIBLIOTECA + DADOS:
print("\033[1;34m**\033[m" * 20)
valor_inicial = float(input("\033[1;32;44mValor inicial: R$\033[m"))
rendimento = float(input("\033[1;32;44mRendimento por período (%):\033[m "))
aporte = float(input("\033[1;32;44mAporte a cada período: R$\033[m"))
períodos = int(input("\033[1;32;44mTotal de períodos:\033[m "))
print("\033[1;34m**\033[m" * 20)
sleep(1)
print("\n")
print("\033[7;35;40mPROCESSANDO DADOS...\033[m\n")
sleep(1)

calcular_juros_compostos(valor_inicial, rendimento, aporte, períodos)

