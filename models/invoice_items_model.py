# invoice_items_model.py

from connections import config
from .model import Model
from .invoice_model import Invoice
from .product_model import Product
import sqlite3

class InvoiceItems(Model):
    """Resposta Esperada: Id da Fatura de itens / Id da Fatura pega / id do Produto / Quantidade de produtos pegos / Valor do produto
    """
    def __init__(self, invoice: Invoice, produto: Product, quantidade: int, id: int = None):
        self.invoice_id = invoice.id
        self.invoice = invoice
        self.product_id = produto.id
        self.quantidade = quantidade
        self.valor_produto = produto.precoUnitario
        self.id = id

    def salvar(self):     
        # Calcula o subtotal e atualiza a fatura
        subtotal = self.quantidade * self.valor_produto
        sql = f"INSERT INTO {config.TABLE_NAME_INVOICE_ITEMS} (invoice_id, product_id, quantidade, subtotal) VALUES(?, ?, ?, ?)"
        dados = [self.invoice_id, self.product_id, self.quantidade, self.valor_produto]
        
        # Adiciona valor total à fatura
        self.invoice.adiciona_valor_total(self.quantidade, self.valor_produto)

        # Atualiza a fatura após adicionar o item
        dados_invoice = [self.invoice.client_id, self.invoice.dataEmissao, self.invoice.valorTotal, self.invoice.status, self.invoice.id]
        
        return self._salvar_no_banco(config.DB_FILE_INVOICE_ITEMS, sql, dados, config.TABLE_NAME_INVOICE_ITEMS, "invoice_id", self.invoice_id)

    def atualizar(self, dados: list):
        if dados is None:
            print("Erro ao atualizar dados. Operação cancelada.")
            return 
        sql = f'UPDATE {config.TABLE_NAME_INVOICE_ITEMS} SET invoice_id = ?, product_id = ?, quantidade = ?, subtotal = ? WHERE id = ?'
        return self._salvar_no_banco(config.DB_FILE_INVOICE_ITEMS, sql, dados)

    def consultar(self):
        if self.id is None:
            print("Erro: ID do item não está definido. Não é possível consultar.")
            return None
        dados_invoice_item = self._consultar_por_id_banco(config.DB_FILE_INVOICE_ITEMS, config.TABLE_NAME_INVOICE_ITEMS, self.id)
        if dados_invoice_item is None:
            print(f"Erro: Item de fatura com ID {self.id} não encontrado.")
            return None
        self.id, self.invoice_id, self.product_id, self.quantidade, self.valor_produto = dados_invoice_item
        print(f"Item da fatura encontrado: {self.id}, {self.invoice_id}, {self.product_id}, {self.quantidade}, {self.valor_produto}")       
        return dados_invoice_item

    def excluir(self, id: int):
        self._excluir_do_banco(config.DB_FILE_INVOICE_ITEMS, config.TABLE_NAME_INVOICE_ITEMS, id)   
