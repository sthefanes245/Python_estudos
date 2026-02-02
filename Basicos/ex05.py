#Peça o ano de nascimento do usuário e diga se ele já é maior de idade (considere 18 anos).
ano_nascimento =  int(input("Informe seu ano de nascimento: \n"))

ano_atual = 2026
maioridade = 18

idade = ano_atual - ano_nascimento

if idade < maioridade:
    print("Você é menor de idade!")

else:
    print("Voce é maior de idade!")
