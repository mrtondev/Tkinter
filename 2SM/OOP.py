#Classe
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def descrever_carro(self):
        descricao = f"{self.ano} {self.marca} {self.modelo}"
        return descricao
    
    def ler_odometro(self):
        print(f"Este carro tem {self.odometro} km rodados.")

    def atualizar_odometro(self, km):
        if km >= self.odometro:
            self.odometro = km
        else:
            print("Você não pode diminuir o valor do odômetro!")
        
    def incrementador_odometro(self, km):
        if km >= 0:
            self.odometro += km
        else:
            print("Não é possível incrementar com um valor negativo.")

#Criando Objeto:
meu_carro = Carro('Toyota', 'Corolla', 2020)
print(meu_carro.descrever_carro())
meu_carro.atualizar_odometro(15000)
meu_carro.ler_odometro()