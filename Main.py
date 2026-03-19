from Sistema import Sistema

sistema = Sistema()

print("\n-=- AutoGest ERP Iniciado -=-\n")

while True:

    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Veículo")
    print("3 - Cadastrar Ordem de Serviço")
    print("4 - Listar Clientes")
    print("5 - Listar Veículos")
    print("6 - Listar Ordens")
    print("7 - Remover Cliente")
    print("8 - Remover Veículo")
    print("9 - Remover Ordem de Serviço")
    print("10 - Sair\n")

    opcao = input("Escolha: ")

    if opcao == "1":
        sistema.cadastrar_cliente()
    
    elif opcao == "2": 
        sistema.cadastrar_veiculo()
    
    elif opcao == "3":
        sistema.cadastrar_servico()
    
    elif opcao == "4":
        sistema.listar_clientes()
   
    elif opcao == "5":
        sistema.listar_veiculos()
    
    elif opcao == "6":
        sistema.listar_ordem()

    elif opcao == "7":
        sistema.remover_cliente()

    elif opcao == "8":
        sistema.remover_veiculo()

    elif opcao == "10":
        print("\nEncerrando...\n")
        break