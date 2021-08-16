#QUESTÃO 1:
consumo = float(input("Informe o valor total do consumo: R$ "))
pessoas = float(input("Informe o total de pessoas: "))
taxa = float(input("Informe o percentual do serviço, entre 0 e 100: "))

#CONDIÇÕES:
if consumo > 0:
    if pessoas > 0:
        print()
    else:
        print("Valor inválido")
        quit()
    if taxa >= 0 and taxa <= 100:
        print()
    else:
        print("Valor inválido")
        quit()
    print()
else:
    print("Valor inválido")
    quit()

#FÓRMULA:
total_1 = consumo + (consumo * taxa / 100)
total_2 = total_1 / pessoas

#CONVERSÃO DO TOTAL_1:
valor1 = str(total_1)
novo_1 = valor1.replace(".", ",")

#CONVERSÃO DO TOTAL_2:
valor2 = str(total_2)
novo_2 = valor2.replace(".", ",")

print(f"O valor total da conta, com a taxa de serviço, será de R$ {novo_1}")
print(f"Dividindo a conta por {pessoas} pessoa(s), cada pessoa deverá pagar R$ {novo_2}")