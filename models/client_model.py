from connections import config
from .model import Model

def getUpdate():
        try:
            id = input("Digite o Id do item que deseja alterar: ")
            id = int(id)
        except ValueError as e:
            print("ERROR DIGITE APENAS NÚMERO INTEIROS", e)
            return None
        dados = str(input("Digite o novo nome, email, telefone, endereco: [Não esqueça de separar por virgula]")).split(',')
        dados = [item.strip() for item in dados]
        if len(dados) != 4:
            print("Error: Você deve inserir 4 dados!!")
            return None
        
        if any(not item for item in dados):
            print("Erro: Nenhum dado pode ser vazio!")
            return None
        dados.append(id)
        return dados

class Client(Model):
    def __init__(self, nome : str, email : str, telefone : str, endereço: str, id : int = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereço

    def salvar(self):     
        sql = f"INSERT INTO {config.TABLE_NAME_CLIENT} (nome, email, telefone, endereco) VALUES(?, ?, ?, ?)"
        dados = [self.nome, self.email, self.telefone, self.endereco]
        return self._salvar_no_banco(config.DB_FILE_CLIENT, sql, dados)
    

    
    def atualizar(self, dados: list):
        if dados is None:
            print("Erro ao atualizar dados. Operação cancelada.")
            return 
        sql = 'UPDATE Client SET nome = ?, email = ?, telefone = ?, endereco = ? WHERE id = ?'

        return self._salvar_no_banco(config.DB_FILE_CLIENT,sql, dados)

    def consultar(self, id: int):
        self._consultar_por_id_banco(config.DB_FILE_CLIENT,config.TABLE_NAME_CLIENT, id)


    def excluir(self, id: int):
        self._excluir_do_banco(config.DB_FILE_CLIENT,config.TABLE_NAME_CLIENT,id)   
