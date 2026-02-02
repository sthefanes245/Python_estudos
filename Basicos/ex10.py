""" Atividade: Crie um script que peça ao usuário o nome de um produto, o preço (string) e a quantidade desejada.
    Requisitos:
    Converta o preço de str para float.
    Calcule o valor total e exiba uma mensagem usando f-strings formatando o preço com duas casas decimais (ex: R$ 10.50).
    Use o método .title() para garantir que o nome do produto comece com letra maiúscula.
"""

produto = str(input("Informe o nome do produto: "))
preco = str(input("Informe o valor do produto: "))
quantidade = int(input("Informe a quatidade desejada:"))

print("Informações da compra:")
print(produto.title())
#conversão de tipo:
preco_float = float(preco)

#Cálculo da compra
valor_final = preco_float * quantidade
print(f"Valor total da compra: R${valor_final:.2f}")