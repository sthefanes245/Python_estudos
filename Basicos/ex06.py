#Leia a velocidade de um carro. Se ultrapassar 80 km/h, exiba uma mensagem dizendo que ele foi multado. (Bônus: a multa custa R$ 7,00 por cada km acima do limite).
velocidade_carro = int(input("Informe a velocidade do carro: \n"))

velocidade_limite = 80
multa = 7.00


if velocidade_carro > velocidade_limite:
    velocidade_ultrapassada =  velocidade_carro - velocidade_limite

    multa_final = velocidade_ultrapassada * 7 

    print(f"Você foi multado em {multa_final:.2f}")
else:
    print("Tenha um bom dia! Dirija com segurança.")