#QUESTÃO 2:
idade = int(input("Informe a sua idade: "))

#CONDIÇÃO:
if idade > 0:
    print()  
    if idade >= 18 and idade < 70:
        print("Voto obrigatório")
        print("Eleitor Obrigatório")
    elif idade >= 16 and idade < 18 or idade >= 70:
        print("Voto opcional")
        print("Eleitor Facultativo")
    else:
        if idade < 16:
            print("Sem direito ao voto")
            print("Não Eleitor")
else:
    quit()