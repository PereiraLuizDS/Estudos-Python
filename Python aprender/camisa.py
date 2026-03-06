"""
uma loja de roupas está vendendo camisas básicas com 
descontos, mas seus funcionários têm dificuldades no cálculo 
do valor final a ser cobrado. Por isso, seu Tanaka, dono da loja, 
convidou você para criar um programa para calcular o preço 
final a partir do número de camisas. Seu Tanaka definiu as se-
guintes regras de desconto:
• Até 5 camisas, desconto de 3%
• Acima de 5 camisas e até 10 camisas, desconto de 
5%; e 
• Acima de 10 camisas, desconto de 7%.
68
Pronto, calcule e imprima o valor a ser pago pelo clien-
te, sabendo que o preço da camisa é R$ 12,50. 
"""
Valorcamisa=12.50
camisa= int(input("Digite a quantidade de camisa: "))
if camisa < 5:
    print ("não há desconto")
    Total=Valorcamisa*camisa
    print(f"O totalda camisa é: {Total:.2f } ")
elif 5 < camisa  < 10: 
     Total=Valorcamisa*camisa
     desconto= Total*0.05
     Total= Total=desconto
     print(f"O valor total com desconto é : { Total:.2f}")    
else: 
     Total=Valorcamisa*camisa
     desconto= Total*0.07
     Total= Total-desconto
     print(f"O valor total com desconto é : { Total:.2f}")



