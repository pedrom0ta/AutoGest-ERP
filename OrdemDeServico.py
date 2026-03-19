class OrdemDeServico:
    def __init__(self, id, descricao, valor, status, veiculo, cliente):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.status = status
        self.veiculo = veiculo
        self.cliente = cliente

    def mostrar_dados(self):
        print(f"ID: {self.id}")
        print(f"Veículo: {self.veiculo.modelo}")
        print(f"Dono: {self.cliente.nome}")
        print(f"Serviço: {self.descricao}")
        print(f"Valor: {self.valor}")
        print(f"Status: {self.status}")
        

        