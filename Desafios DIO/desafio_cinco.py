# TODO: Crie uma função 'elementos_comuns' que receba duas 
# listas de números inteiros separados por espaço:

def elementos_comuns(lista1, lista2):
   #estou usando o set para converter para conjuntos e evitar repetições de numeros 
   set1 = set(lista1)
   set2 = set(lista2)
   return list(set1.intersection(set2))

#map(int, lista)

# Leitura das listas
#o split realiza cortes na string, nesse caso onde houver espaço em branco, ele ira fazer um corte/separar
lista1 = input().split()
lista2 = input().split()



# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    #transforma os elementos em inteiro, o map que faz essa  conversão um por um 
    elementos1 = map(int, lista1)
    elementos2 = map(int, lista2)
    
    comuns = elementos_comuns(elementos1, elementos2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")