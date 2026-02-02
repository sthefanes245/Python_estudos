#Receba três notas de um aluno e calcule a média simples
valor_metros = int(input("Informe o valor em metros:"))

opcao = int(input("Escolha 1 para converter em centímetros e 2 para converter em milímetro: "))

if(opcao == 1):
    valor_centimetros = valor_metros * 100
    print(f"{valor_metros} metros é igual a {valor_centimetros} centímetros")
else:
    valor_milimetros = valor_metros * 1000
    print(f"{valor_metros} metros é igual a {valor_milimetros} milímetros")