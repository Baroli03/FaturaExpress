


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