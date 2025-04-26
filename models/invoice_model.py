from connections import config
from .model import Model
from .client_model import Client



# sql_invoice = (f'CREATE TABLE IF NOT EXISTS {config.TABLE_NAME_INVOICE}'
# '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'client_id INTEGER NOT NULL,'
#     'dataEmissao INTEGER NOT NULL,'
#     'valorTotal REAL NOT NULL,'
#     'status TEXT CHECK(status IN ("Paga", "Pendente", "Vencida", "Cancelada")) NOT NULL,'
#     'FOREIGN KEY (client_id) REFERENCES client(id)'
# ')')


# @abstractmethod
# def salvar(self, db_file: Path):
#     pass

# @abstractmethod
# def atualizar(self, db_file: Path, id: int):
#     pass

# @abstractmethod
# def consultar(self, id: int):
#     pass

# @abstractmethod
# def excluir(self, id: int):
#     pass

def getUpdate_Invoice():
        try:
            id = input("Digite o Id do item que deseja alterar: ")
            id = int(id)
        except ValueError as e:
            print("ERROR DIGITE APENAS NÚMERO INTEIROS", e)
            return None
        
        while True:
            dados = input("Digite novos valores para client_id, dataEmissao, valorTotal, status: [Não esqueça de separar por virgula]").split(',')
            dados = [item.strip() for item in dados]

            if len(dados) != 4:
                print("Error: Você deve inserir 4 dados!!")
                continue
        
            if any(not item for item in dados):
                print("Erro: Nenhum dado pode ser vazio!")
                continue
            

            try:
                client_id = int(dados[0])    
                data_emissao = int(dados[1])  
                valor_total = float(dados[2]) 
                status = dados[3]            
                break
            except(ValueError, IndexError):
                print('Valor de Data de emissão ou valor total invalido, Aceito apenas números')

        dados.append(id)
        print(f"Salvando Client_Id = {client_id}, Data de emissão = {data_emissao}, Valor total = {valor_total}, Status = {status} no id {id}")
        return [client_id, data_emissao, valor_total, status]

class Invoice(Model):
    def __init__(self, client_id: Client, dataEmissao: int, valorTotal: float, status: str, id: int = None):
        status_esperado = ["Paga", "Pendente", "Vencida", "Cancelada"]
        if status not in status_esperado:
            raise ValueError(f'Status inválido: "{status}". Deve ser um dos: {", ".join(status_esperado)}')
        self.id = id
        self.client_id = client_id.id
        self.dataEmissao = dataEmissao
        self.valorTotal = valorTotal
        self.status = status
    

    def salvar(self):     
        sql = f"INSERT INTO {config.TABLE_NAME_INVOICE} (client_id, dataEmissao, valorTotal, status) VALUES(?, ?, ?, ?)"
        dados = [self.client_id, self.dataEmissao, self.valorTotal, self.status]
        return self._salvar_no_banco(config.DB_FILE_INVOICE, sql, dados, config.TABLE_NAME_INVOICE)


    def atualizar(self, dados: list):
        if dados is None:
            print("Erro ao atualizar dados. Operação cancelada.")
            return 
        sql = f'UPDATE {config.TABLE_NAME_INVOICE} SET client_id = ?, dataEmissao = ?, valorTotal = ?, status = ? WHERE id = ?'
        return self._salvar_no_banco(config.DB_FILE_INVOICE,sql, dados)
    
    def consultar(self, id: int):
        self._consultar_por_id_banco(config.DB_FILE_INVOICE,config.TABLE_NAME_INVOICE, id)


    def excluir(self, id: int):
        self._excluir_do_banco(config.DB_FILE_INVOICE,config.TABLE_NAME_INVOICE,id)   
