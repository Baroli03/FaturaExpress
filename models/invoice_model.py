# invoice_model.py

from datetime import datetime
from .model import Model
from .client_model import Client
import sqlite3
from connections import config


def getUpdate_Invoice():
    try:
        id = int(input("Digite o ID da fatura que deseja alterar: "))
    except ValueError as e:
        print("ERRO: Digite apenas números inteiros para o ID.", e)
        return None

    entrada = input("Digite o novo cliente_id, status, valorTotal (separados por vírgula): ")
    dados = [item.strip() for item in entrada.split(',')]

    if len(dados) != 3:
        print("Erro: Você deve inserir exatamente 3 dados (cliente_id, status, valorTotal).")
        return None

    try:
        cliente_id = int(dados[0])
        status = dados[1]
        valor_total = float(dados[2])
    except ValueError as e:
        print("Erro: cliente_id deve ser inteiro e valorTotal deve ser um número decimal.", e)
        return None

    if not status:
        print("Erro: O status não pode estar vazio.")
        return None

    return [cliente_id, status, valor_total, id]

class Invoice(Model):
    def __init__(self, client_id: Client, status: str, valorTotal: float = 0.0, id: int = None):
        """ Status possíveis valores: "Paga", "Pendente", "Vencida", "Cancelada" """
        status_esperado = ["Paga", "Pendente", "Vencida", "Cancelada"]
        if status not in status_esperado:
            raise ValueError(f'Status inválido: "{status}". Deve ser um dos: {", ".join(status_esperado)}')
        self.id = id
        self.client_id = client_id.id
        self.status = status
        self.valorTotal = valorTotal
        self.dataEmissao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Data e hora atuais

    def salvar(self):  
        # Verificar se já existe uma fatura com o mesmo cliente e data de emissão
        sql_check = f"SELECT id FROM {config.TABLE_NAME_INVOICE} WHERE client_id = ? AND dataEmissao = ?"
        dados_check = [self.client_id, self.dataEmissao]

        with sqlite3.connect(config.DB_FILE_INVOICE) as connection:
            cursor = connection.cursor()
            cursor.execute(sql_check, dados_check)
            resultado = cursor.fetchone()

            if resultado is None:
                # A fatura não existe, então cria uma nova
                sql_insert = f"INSERT INTO {config.TABLE_NAME_INVOICE} (client_id, dataEmissao, valorTotal, status) VALUES(?, ?, ?, ?)"
                dados_insert = [self.client_id, self.dataEmissao, self.valorTotal, self.status]
                cursor.execute(sql_insert, dados_insert)
                self.id = cursor.lastrowid  # Pega o ID da nova fatura
                connection.commit()
                print(f"Fatura criada com sucesso com ID {self.id}!")
            else:
                # A fatura já existe, atualiza os dados
                self.id = resultado[0]  # Pega o ID da fatura existente
                print(f"Fatura já existe com ID {self.id}, atualizando...")

                # Atualiza a fatura com novos valores
                sql_update = f"UPDATE {config.TABLE_NAME_INVOICE} SET valorTotal = ?, status = ? WHERE id = ?"
                dados_update = [self.valorTotal, self.status, self.id]
                cursor.execute(sql_update, dados_update)
                connection.commit()
                print(f"Fatura com ID {self.id} atualizada.")

    def consultar(self):
        if self.id is None:
            print("Erro: ID da fatura não está definido. Não é possível consultar.")
            return None
        dados_invoice = self._consultar_por_id_banco(config.DB_FILE_INVOICE, config.TABLE_NAME_INVOICE, self.id)
        if dados_invoice is None:
            print(f"Erro: Fatura com ID {self.id} não encontrada.")
            return None
        self.id, self.client_id, self.dataEmissao, self.valorTotal, self.status = dados_invoice
        print(f"Fatura encontrada: {self.id}, {self.client_id}, {self.dataEmissao}, {self.valorTotal}, {self.status}")       
        return dados_invoice

    def atualizar_valor_total(self, dados: list):
        if len(dados) != 2:
            print("Erro: a lista de dados precisa ter 5 elementos.")
            return
        sql = f"""
            UPDATE {config.TABLE_NAME_INVOICE}
            SET valorTotal = ?
            WHERE id = ?
        """

        return self._atualizar_banco(config.DB_FILE_INVOICE, sql, dados)

    def excluir(self, id: int):
        self._excluir_do_banco(config.DB_FILE_INVOICE, config.TABLE_NAME_INVOICE, id)

    def adiciona_valor_total(self, quantidade, preco):
        self.valorTotal = quantidade * preco
        self.atualizar_valor_total([self.valorTotal, self.id])

    def atualizar(self, dados):
        sql = f"""
            UPDATE {config.TABLE_NAME_INVOICE}
            SET cliente_id = ?, status = ?, valorTotal = ?
            WHERE id = ?
        """
        dados = [self.cliente.id, self.status, self.valorTotal, self.id]
        self._atualizar_banco(config.DB_NAME, sql, dados)
