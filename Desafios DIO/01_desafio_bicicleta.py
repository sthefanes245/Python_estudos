# Declarei minha classe e a nomeei de Bicicleta, ela é o meu molde, que define o que toda bicileta terá e o que ela saberá fazer 
class Bicicleta:
    # Inicializador __init__, aqui é onde estou definindo os atributos da minha instânca(b1)
    # Método construtor:
    def __init__(self, cor, modelo, ano, valor):
        # self é uma referência explícita para a instância do objeto-Biciclet.
        #Ou seja, estamos dizendo: "esta é a instância do objeto que foi passado".
        #Quando você diz self.cor = cor, você está dizendo: "Ei, Python, pegue esta cor que recebi agora e guarde-a na gaveta 'cor' desta bicicleta específica (a self)"
        # Inicializando os atributos da minha classe (self.cor), o atributo é a característica da minha instâcia b1
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1 
    
    # Método: definimos ao menos um argumento, nesse caso o self,
    # que é a referência explícita para o objeto.
    def buzinar(self):
        print("plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada")

    # Se o primeiro elemento que estou usando como argumento não for o self, 
    # tenho que ter cuidado, pois para o meu programa, o primeiro argumento 
    # é sempre a instância do objeto.
    def correr(self):
        print("Vrummm...")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha...")
        # Representa uma das vantagens da referência explícita. 
        # Aqui temos um método (lógica) dentro de outro método.
        def _trocar_marcha():
            # Consigo perceber que tudo que está dentro do meu método e tem a 
            # palavra 'self.' é um atributo da instância do meu objeto.
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
            else: 
                print("Não foi possível trocar de marcha...")
        
        _trocar_marcha()

    # Estou pegando a instância do meu objeto (self)
    # e fazendo a representação da minha classe:
    def __str__(self):
        # Concatenando a lista com a string que eu quero, nesse caso ', '.
        # Agora não preciso me preocupar com o quanto minha classe vai crescer,
        # não preciso ficar fazendo manualmente.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
        # Exemplo de como fazer de forma manual: 
        # return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"


# Instanciando o objeto
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# Chamando meus métodos 
b1.buzinar()
b1.correr()

"""
Essas chamadas são equivalentes a esta:
Bicicleta.buzinar(b1)
"""

# Acessar os atributos da minha classe
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1) # Aqui aciona o método __str__