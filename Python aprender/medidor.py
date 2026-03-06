print(f"{("*"*10)}MEDIDOR DE GRANDEZA{("*"*10)}")
tenção=0.00
print(f"{("*"*39)}")
print ("1-tenção (em volt)\n2-Resistencia (em 0hm)\n3-Corrente (em ampére)")
print (f"{("*"*39)+("*\n"*50)}")
opção=int(input("Qual opção você deseja? " ))
if opção==1:
    resistencia=float(input("Digite o Valor da resistencia: "))
    corrente=float(input("Digite o Valor da corrente: "))
    tenção=resistencia*corrente
    print(f"O valor da tenção é : {tenção:.2f} ")
    print(f"{("*\n"*39)}")
elif opção==2: 
    tenção=float(input("Digite a tenção: "))
    corrente=float(input("Digite a corrente: "))
    print(f"O valor da resistencia é: {tenção/corrente} Ω")
    print(f"{("*"*39)}")
elif opção==3: 
    tenção=float(input("Digite a tenção: "))
    resistencia=float(input("Digite o Valor da resistencia: "))
    corrente=tenção/resistencia
    print(f"O valor da corrente é: {corrente}")
else:
    print("Digite apenas uma das 3 opções")
print(f"{("*"*39)}")

    
