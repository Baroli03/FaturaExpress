from views.menu_cliente import menu_clientes
from views.menu_produto import menu_produtos
from views.menu_fatura import menu_faturas


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