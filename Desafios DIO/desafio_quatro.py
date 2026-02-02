# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma 
# tupla de números inteiros como argumento:Explicação de Resolução:

#Converta cada string na "lista_strings" em um número inteiro utilizando a função "int()".
#Use a função "map()" para aplicar a função "int()" a cada elemento da "lista_strings".
#Armazene o resultado em uma variável chamada "elementos".

def soma_tupla(elementos):
    return sum(elementos)


if __name__ == "__main__":
    entrada = input()
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")