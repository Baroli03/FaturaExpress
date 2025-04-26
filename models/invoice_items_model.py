from connections import config
from .model import Model
from .invoice_model import Invoice
from .product_model import Product


# sql_invoice_items = (f'CREATE TABLE IF NOT EXISTS {config.TABLE_NAME_INVOICE_ITEMS}'
# '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'invoice_id INTEGER NOT NULL,'
#     'product_id INTEGER NOT NULL,'
#     'quantidade INTEGER NOT NULL,'
#     'subtotal REAL NOT NULL,'
#     'FOREIGN KEY (invoice_id) REFERENCES invoice(id),'
#     'FOREIGN KEY (product_id) REFERENCES product(id)'
# ')')

def getUpdate_InvoiceItems():
        try:
            id = input("Digite o Id do item que deseja alterar: ")
            id = int(id)
        except ValueError as e:
            print("ERROR DIGITE APENAS NÚMERO INTEIROS", e)
            return None
        
        while True:
            dados = input("Digite novos valores para invoice_id (INTEGER), product_id (INTEGER), quantidade (INTEGER), subtotal (REAL): [Não esqueça de separar por virgula]").split(',')
            dados = [item.strip() for item in dados]

            if len(dados) != 4:
                print("Error: Você deve inserir 4 dados!!")
                continue
        
            if any(not item for item in dados):
                print("Erro: Nenhum dado pode ser vazio!")
                continue
            

            try:
                invoice_id = int(dados[0])    
                product_id = int(dados[1])  
                quantidade = int(dados[2]) 
                subtotal = float(dados[3])            
                break
            except(ValueError, IndexError):
                print('Valores Incorretos, tente novamente')

        dados.append(id)
        print(f"Salvando invoice_id = {invoice_id}, product_id = {product_id}, quantidade = {quantidade}, subtotal = {subtotal} no id {id}")
        return [invoice_id, product_id, quantidade, subtotal]




class InvoiceItems(Model):
    def __init__(self, invoice_id: Invoice, product_id: Product, quantidade: int, subtotal: float, id: int = None):
        self.invoice_id = invoice_id.id
        self.product_id = product_id.id
        self.quantidade = quantidade
        self.subtotal = subtotal
        self.id = id
    

    def salvar(self):     
        sql = f"INSERT INTO {config.TABLE_NAME_INVOICE_ITEMS} (invoice_id, product_id, quantidade, subtotal) VALUES(?, ?, ?, ?)"
        dados = [self.invoice_id, self.product_id, self.quantidade, self.subtotal]
        return self._salvar_no_banco(config.DB_FILE_INVOICE_ITEMS, sql, dados, config.TABLE_NAME_INVOICE_ITEMS)
    
    def atualizar(self, dados: list):
        if dados is None:
            print("Erro ao atualizar dados. Operação cancelada.")
            return 
        sql = f'UPDATE {config.TABLE_NAME_INVOICE_ITEMS} SET invoice_id = ?, product_id = ?, quantidade = ?, subtotal = ? WHERE id = ?'
        return self._salvar_no_banco(config.DB_FILE_INVOICE_ITEMS,sql, dados)
    
    def consultar(self, id: int):
        self._consultar_por_id_banco(config.DB_FILE_INVOICE_ITEMS,config.TABLE_NAME_INVOICE_ITEMS, id)


    def excluir(self, id: int):
        self._excluir_do_banco(config.DB_FILE_INVOICE_ITEMS,config.TABLE_NAME_INVOICE_ITEMS,id)   
