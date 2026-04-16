from Cliente import Cliente
from OrdemDeServico import OrdemDeServico
from Veiculo import Veiculo

class Sistema:

    def __init__(self):
        self.clientes = []
        self.veiculos = []
        self.ordemdeservico = []
    
    #Cadastrar Clientes
    def cadastrar_cliente(self):
        
        id = len(self.clientes) + 1
        
        nome = input("Nome: ")
        while nome == "":
            print("Nome não pode ser vazio!")
            nome = input("Nome: ")

        cpf = input("Cpf: ")
        while cpf == "":
            print("CPF não pode ser vazio!")
            cpf = input("Cpf: ")

        telefone = input("Telefone: ")
        while telefone == "":
            print("Telefone não pode ser vazio!")
            telefone = input("Telefone: ")
            
        cliente = Cliente(id, nome, cpf, telefone)
        
        self.clientes.append(cliente)

        print(f"\nCliente cadastrado! ID {id}\n")
    
    #Cadastrar Veiculos
    def cadastrar_veiculo(self):

        if not self.clientes:
            print("\nNenhum cliente cadastrado!\n")
            return

        print("\n-=- Clientes Cadastrados -=-\n")
        for cliente in self.clientes:
            print(f"ID: {cliente.id} - Nome: {cliente.nome}")
        
        cliente_cadastr = input("\nCliente está cadastrado? (S/N): ")

        if cliente_cadastr.lower() == "n":
            print(("\nCadastre o cliente para continuar!\n"))
            return
        
        elif cliente_cadastr.lower() == "s":
            id_cliente = int(input("Digite o ID do cliente: "))
            
            for cliente in self.clientes:
                if id_cliente == cliente.id:
                    print("\nCliente Encontrado!\n")
                    
                    modelo = input("Modelo: ")
                    placa = input("Placa: ")
                    ano = int(input("Ano do Veículo: "))
                    id = len(self.veiculos) + 1

                    veiculo = Veiculo(id, modelo, placa, ano, cliente)
                    cliente.veiculos.append(veiculo)
                    self.veiculos.append(veiculo)

                    print("\nVeículo cadastrado!\n")
                    return
        
        print("\nCliente não encontrado!\n")        

    #Cadastrar Serviços
    def cadastrar_servico(self):

        if not self.veiculos:
            print("\nNenhum veículo cadastrado!\n")
            return
        
        print("\n-=- Veículos Cadastrados -=-\n")

        for veiculo in self.veiculos:
            print(f"{veiculo.id} - {veiculo.modelo} - {veiculo.cliente.nome}")

        veic_cadastr = input("Seu veículo está cadastrado? (S/N): ")
        
        if veic_cadastr.lower() == "n":
            print("\nCadastre seu veículo!\n")
            return
        
        elif veic_cadastr.lower() == "s":
            id_veiculo = int(input("Digite o ID do veículo: \n"))

        else:
            print("Digite apenas (S/N)!.")
            return
        
        encontrado = False
        
        for veiculos in self.veiculos:
            if id_veiculo == veiculos.id:
                encontrado = True
                print("Veículo encontrado!\n")

                descricao = input("Descrição do Serviço: ")
                valor = float(input("Valor do Serviço: "))
                status = input("Status: ")
                id = len(self.ordemdeservico) + 1

                veiculo = veiculos
                cliente = veiculos.cliente

                servico = OrdemDeServico(id, descricao, valor, status, veiculo, cliente)
                

                veiculo.ordemdeservico.append(servico)
                self.ordemdeservico.append(servico)
                print("\nServiço cadastrado!\n")
                break
        
        if not encontrado:
            print("\nVeículo não encontrado!\n")
                
    #Listar Clientes
    def listar_clientes(self):

        if not self.clientes:
            print("\nNenhum cliente cadastrado!\n")
            return
        
        print("\n-=- Lista de Clientes -=-\n")

        for cliente in self.clientes:
            cliente.mostrar_dados()
            print("----------------")
    
    #Listar Veiculos
    def listar_veiculos(self):

        if not self.veiculos:
            print("\nNenhum veículo cadastrado!\n")
            return
        
        print("\n-=- Lista de Veículos -=-\n")

        for veiculo in self.veiculos:
            veiculo.mostrar_dados()
            print("----------------")
    
    #Listar Serviços
    def listar_ordem(self):

        if not self.ordemdeservico:
            print("\nNenhum serviço cadastrado!\n")
            return
        
        print("\n-=- Lista de Serviços -=-\n")

        for servicos in self.ordemdeservico:
            servicos.mostrar_dados()
            print("----------------")
    
    #Remover Cliente
    def remover_cliente(self):
        
        if not self.clientes:
            print("\nNenhum cliente cadastrado!\n")
            return

        print("\n-=- Clientes Cadastrados -=-\n")
        
        for cliente in self.clientes:
            print(f"ID {cliente.id} - Nome: {cliente.nome}")

        pedir_id = int(input("\nDigite o ID do cliente irá remover: "))
        
        for cliente in self.clientes:
            if pedir_id == cliente.id:
                self.clientes.remove(cliente)
                print("\nCliente removido!\n")
                return
    
    def remover_veiculo(self):

        if not self.veiculos:
            print("\nNenhum veículo cadastrado!\n")
            return
        
        print("\n-=- Veículos Cadastrados -=-\n")

        for veiculo in self.veiculos:
            print(f"ID - {veiculo.id}")
            print(f"Dono do Veículo: {veiculo.cliente.nome}")
            print(f"Placa: {veiculo.placa}")
            print(f"Modelo: {veiculo.modelo}")
            print("-=-=-=--=-=-=-=-=-")
        
        pedir_id_veiculo = int(input("\nDigite o ID do veículo irá remover: "))

        for veiculo in self.veiculos:
            if pedir_id_veiculo == veiculo.id:
                self.veiculos.remove(veiculo)
                print("\nVeículo removido!\n")
                return

        print("\nVeículo não encontrado!\n")

    def remover_servico(self):
        
        if not self.ordemdeservico:
            print("Não há serviços cadastrados!")
            return
    
        print("-=- Serviços Cadastrados -=-\n")
        
        for servico in self.ordemdeservico:
            print(f"ID {servico.id} - {servico.descricao}")
        
        pedir_id_servico = int(input("\nDigite o ID do serviço que deseja remover: "))
        
        for servico in self.ordemdeservico:
            if pedir_id_servico == servico.id:
                self.ordemdeservico.remove(servico)
                
                if servico in servico.veiculo.ordemdeservico:
                    servico.veiculo.ordemdeservico.remove(servico)
                    
                print("\nServiço removido!\n")
                return
        
        print("\nServiço não encontrado!\n")
    
    def atualizar_cliente(self):

        if not self.clientes:
            print("\nNenhum cliente cadastrado!\n")
            return
        
        print("\n-=- Clientes -=-\n")
        for cliente in self.clientes:
            print(f"ID {cliente.id} - {cliente.nome}")
        
        id_busca = int(input("\nDigite o ID do cliente: "))

        for cliente in self.clientes:
            if cliente.id == id_busca:
                cliente.nome = input("Novo nome: ")
                cliente.cpf = input("Novo CPF: ")
                cliente.telefone = input("Novo telefone: ")
                
                print("\nCliente atualizado!\n")
                return
        
        print("\nCliente não encontrado!\n")

    def atualizar_veiculo(self):

        if not self.veiculos:
            print("\nNenhum veículo cadastrado!\n")
            return

        for veiculo in self.veiculos:
            print(f"ID {veiculo.id} - {veiculo.modelo}")

        id_busca = int(input("\nDigite o ID do veículo: "))

        for veiculo in self.veiculos:
            if veiculo.id == id_busca:
                veiculo.modelo = input("Novo modelo: ")
                veiculo.placa = input("Nova placa: ")
                veiculo.ano = int(input("Novo ano: "))

                print("\nVeículo atualizado!\n")
                return

        print("\nVeículo não encontrado!\n")

    def atualizar_servico(self):

        if not self.ordemdeservico:
            print("\nNenhum serviço cadastrado!\n")
            return

        for servico in self.ordemdeservico:
            print(f"ID {servico.id} - {servico.descricao}")

        id_busca = int(input("\nDigite o ID do serviço: "))

        for servico in self.ordemdeservico:
            if servico.id == id_busca:
                servico.descricao = input("Nova descrição: ")
                servico.valor = float(input("Novo valor: "))
                servico.status = input("Novo status: ")

                print("\nServiço atualizado!\n")
                return

        print("\nServiço não encontrado!\n")