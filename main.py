from models.client_model import Client
from models.product_model import Product
from models.invoice_model import Invoice
from models.invoice_items_model import InvoiceItems

def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Produtos")
        print("3. Gerenciar Faturas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            menu_faturas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

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

def menu_produtos():
    while True:
        print("\n--- GERENCIAR PRODUTOS ---")
        print("1. Adicionar Produto")
        print("2. Ver Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            ver_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def menu_faturas():
    while True:
        print("\n--- GERENCIAR FATURAS ---")
        print("1. Criar Fatura")
        print("2. Ver Faturas")
        print("3. Atualizar Fatura")
        print("4. Deletar Fatura")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_fatura()
        elif opcao == "2":
            ver_faturas()
        elif opcao == "3":
            atualizar_fatura()
        elif opcao == "4":
            deletar_fatura()
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
    print("Atualizando cliente... (exemplo)")

def deletar_cliente():
    print("Deletando cliente... (exemplo)")

# Funções para gerenciar produtos (com exemplos simples)
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    unidade = input("Digite a unidade do produto (ex: kg, unidade, etc.): ")
    # Aqui você colocaria a lógica de adicionar o produto ao banco de dados
    print(f"Produto {nome} adicionado com sucesso!")

def ver_produtos():
    # Aqui você buscaria os produtos do banco e os exibiria
    print("Listando produtos... (exemplo)")

def atualizar_produto():
    print("Atualizando produto... (exemplo)")

def deletar_produto():
    print("Deletando produto... (exemplo)")

# Funções para gerenciar faturas (com exemplos simples)
def criar_fatura():
    print("Criando fatura... (exemplo)")

def ver_faturas():
    # Aqui você buscaria as faturas do banco e as exibiria
    print("Listando faturas... (exemplo)")

def atualizar_fatura():
    print("Atualizando fatura... (exemplo)")

def deletar_fatura():
    print("Deletando fatura... (exemplo)")

# Iniciar o menu
if __name__ == "__main__":
    menu_principal()
