




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


