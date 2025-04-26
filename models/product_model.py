from connections import config
from .model import Model


# sql_product = (f'CREATE TABLE IF NOT EXISTS {config.TABLE_NAME_PRODUCT}'
# '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'nome TEXT NOT NULL UNIQUE,'
#     'precoUnitario REAL NOT NULL,'
#     'unidade TEXT NOT NULL'
# ')')


def getUpdate_Product():
    try:
        id = input("Digite o Id do item que deseja alterar: ")
        id = int(id)
    except ValueError as e:
        print("ERROR DIGITE APENAS NÚMERO INTEIROS", e)
        return None
    dados = str(input("Novo Produto Digite nome, precoUnitario (Numérico), unidade: [Não esqueça de separar por virgula]")).split(',')
    dados = [item.strip() for item in dados]
    while True:
        try:
            float(dados[1])
            break  
        except (ValueError, IndexError):
            print("Preço unitário inválido, tente novamente.")
            dados = input("Novo Produto: Digite nome, precoUnitario (Numérico), unidade: [Separados por vírgula]\n").split(',')
            dados = [item.strip() for item in dados]

    if len(dados) != 3:
        print("Error: Você deve inserir 4 dados!!")
        return None
    
    if any(not item for item in dados):
        print("Erro: Nenhum dado pode ser vazio!")
        return None
    dados.append(id)
    return dados

class Product(Model):
    def __init__(self, nome: str, precoUnitario: float, unidade: str, id: int = None):
        self.id = id
        self.nome = nome
        self.precoUnitario = precoUnitario
        self.unidade = unidade

    
    def salvar(self):     
        sql = f"INSERT INTO {config.TABLE_NAME_PRODUCT} (nome, precoUnitario, unidade) VALUES(?, ?, ?)"
        dados = [self.nome, self.precoUnitario, self.unidade]
        return self._salvar_no_banco(config.DB_FILE_PRODUCT, sql, dados, config.TABLE_NAME_PRODUCT)

    def atualizar(self, dados: list):
        if dados is None:
            print("Erro ao atualizar dados. Operação cancelada.")
            return 
        sql = f'UPDATE {config.TABLE_NAME_PRODUCT} SET nome = ?, precoUnitario = ?, unidade = ? WHERE id = ?'

        return self._salvar_no_banco(config.DB_FILE_PRODUCT,sql, dados)

    def consultar(self, id: int):
        self._consultar_por_id_banco(config.DB_FILE_PRODUCT,config.TABLE_NAME_PRODUCT, id)


    def excluir(self, id: int):
        self._excluir_do_banco(config.DB_FILE_PRODUCT,config.TABLE_NAME_PRODUCT,id)   
