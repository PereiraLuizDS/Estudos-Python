# Construa um programa no qual um usuário informe a sua 
# estatura em metros e o programa converta-a para centímetros.
alturaM=float(input("qual é a sua altura?  "))
print(f"sua altura é {alturaM * 100}cm")
# 2. Construa um programa que receba do usuário a variação do 
#deslocamento de um objeto (em metros) e a variação do tempo  
#percorrido (em segundo). Ao fim, o programa deve calcular a 
#velocidade média, em m/s, do objeto.

Distancia=float(input("Digite a distancia " ))
tompoporS=float(input("digite a velocidade: "))
media= Distancia/tompoporS
print(f"O Vm é : {media:.2f}" )
print("\n\n\n") 

delta_s = float(input("Digite o deslocamento (em metros): "))
delta_t = float(input("Digite o tempo (em segundos): "))
velocidade = delta_s / delta_t
print(f"Vm = {velocidade:.2f} m/s")
