class Veiculo:

    def __init__(self, id, modelo, placa, ano, cliente):
        self.id = id
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.cliente = cliente
        self.ordemdeservico = []

    def mostrar_dados(self):
        print(f"ID: {self.id}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Ano: {self.ano}")
        print(f"Cliente: {self.cliente.id} - {self.cliente.nome}")

        