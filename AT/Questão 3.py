from math import trunc
from time import sleep
def diagnosticar_saúde_financeira ():

    #FÓRMULAS:
    porcent_moradia = trunc((moradia_gastos * 100) / renda_mensal)
    porcent_educação = trunc((educação_gastos * 100) / renda_mensal)
    porcent_transporte = trunc((transporte_gastos * 100) / renda_mensal)

    #TIPO - LISTA:
    tipo = ["moradia", "educação", "transporte"]

    #CONDIÇÕES:
    sleep(1)
    print("\n")
    print("\033[7;35;40mPROCESSANDO DIAGNÓSTICO...\033[m\n")
    sleep(1.5)
    if porcent_moradia <= 30:
        print(f"Seus gastos totais com \033[7;33;40m{tipo[0]}\033[m comprometem \033[1;32m{porcent_moradia}%\033[m de sua renda total. O máximo recomendado é de \033[7;33;40m30%\033[m\033[m. Seus gastos estão dentro da margem recomendada\n")
    else:
        máx_moradia = renda_mensal * 30 / 100
        print(f"Seus gastos totais com \033[7;33;40m{tipo[0]}\033[m comprometem \033[1;31m{porcent_moradia}%\033[m de sua renda total. O máximo recomendado é de \033[7;33;40m30%\033[m.\nPortanto, idealmente, o máximo de sua renda comprometida com \033[7;33;40m{tipo[0]}\033[m deveria ser de \033[7;34;40mR$ {máx_moradia:.2f}\033[m\n")
    
    if porcent_educação <= 20:
        print(f"Seus gastos totais com \033[7;33;40m{tipo[1]}\033[m comprometem \033[1;32m{porcent_educação}%\033[m de sua renda total. O máximo recomendado é de \033[7;33;40m20%\033[m. Seus gastos estão dentro da margem recomendada\n")
    else:
        máx_educação = renda_mensal * 20 / 100
        print(f"Seus gastos totais com \033[7;33;40m{tipo[1]}\033[m comprometem \033[1;31m{porcent_educação}%\033[m de sua renda total. O máximo recomendado é de \033[7;33;40m20%\033[m.\nPortanto, idealmente, o máximo de sua renda comprometida com \033[7;33;40m{tipo[1]}\033[m deveria ser de \033[7;34;40mR$ {máx_educação:.2f}\033[m\n")
    
    if porcent_transporte <= 15:
        print(f"Seus gastos totais com \033[7;33;40m{tipo[2]}\033[m comprometem \033[1;32m{porcent_transporte}%\033[m de sua renda total. O máximo recomendado é de \033[7;33;40m15%\033[m. Seus gastos estão dentro da margem recomendada\n")
    else:
        máx_transporte = renda_mensal * 15 / 100
        print(f"Seus gastos totais com \033[7;33;40m{tipo[2]}\033[m comprometem \033[1;31m{porcent_transporte}%\033[m de sua renda total. O máximo recomendado é de \033[7;33;40m15%\033[m.\nPortanto, idealmente, o máximo de sua renda comprometida com \033[7;33;40m{tipo[2]}\033[m deveria ser de \033[7;34;40mR$ {máx_transporte:.2f}\033[m\n")    

#DADOS:
print("\033[1;34;40m...\033[m" * 15)
renda_mensal = float(input("\033[1;30;44mRenda mensal total: R$\033[m"))
moradia_gastos = float(input("\033[1;30;44mGastos totais com moradia: R$\033[m"))
educação_gastos = float(input("\033[1;30;44mGastos totais com educação: R$\033[m"))
transporte_gastos = float(input("\033[1;30;44mGastos totais com transporte: R$\033[m"))
print("\033[1;34;40m...\033[m" * 15)

diagnosticar_saúde_financeira()