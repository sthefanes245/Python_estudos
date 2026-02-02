#Peça um número ao usuário e exiba a tabuada dele de 1 a 10 usando um laço for
n1 = int(input("Informe um numero:\n"))

print(f"Tabuada de {n1}:")
for contador in range(1, 11):
    tabuada = n1 * contador 
    print(f"{contador} * {n1} = {tabuada}")

