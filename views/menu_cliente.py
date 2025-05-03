from models.client_model import Client
from models.client_model import get_update_client

def menu_clientes():
    while True:
        print("\n--- GERENCIAR CLIENTES ---")
        print("1. Adicionar Cliente")
        print("2. Ver Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_cliente()
        elif opcao == "2":
            ver_clientes()
        elif opcao == "3":
            atualizar_cliente()
        elif opcao == "4":
            deletar_cliente()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")



# Funções para gerenciar clientes (com exemplos simples)
def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    cliente = Client(nome, email, telefone, endereco)
    cliente.salvar()
    cliente.consultar()

def ver_clientes():
    # Aqui você buscaria os clientes do banco e os exibiria
    clientes = Client.consultar_geral_client()  # Chama o método estático
    if clientes:
        for cliente in clientes:
            print(f'''
                \n[Id] {cliente[0]} [Nome] {cliente[1]} [Email] {cliente[2]} [telefone] {cliente[3]} [endereco] {cliente[4]}  
                  ''')
    else:
        print("Nenhum cliente encontrado.")

def atualizar_cliente():
    dados = get_update_client()
    cliente_novo = Client(*dados)
    cliente_novo.atualizar()

def deletar_cliente():
    print("Deletando cliente... (exemplo)")