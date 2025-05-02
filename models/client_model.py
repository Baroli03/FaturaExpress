from connections import config
from .model import Model

def solicitar_id():
    try:
        id = int(input("Digite o Id do item que deseja alterar: "))
        return id
    except ValueError:
        print("Erro: Digite apenas números inteiros.")
        return None

def solicitar_dados():
    entrada = input("Digite o novo nome, email, telefone, endereco (separados por vírgula): ")
    dados = [item.strip() for item in entrada.split(',')]
    
    if len(dados) != 4:
        print("Erro: Você deve inserir exatamente 4 dados.")
        return None
    
    if any(not item for item in dados):
        print("Erro: Nenhum campo pode estar vazio.")
        return None

    return dados

def get_update_client():
    id = solicitar_id()
    if id is None:
        return None

    dados = solicitar_dados()
    if dados is None:
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
        return self._salvar_no_banco(config.DB_FILE_CLIENT, sql, dados, config.TABLE_NAME_CLIENT, "nome", self.nome)
    


    def atualizar(self):
        dados = [self.nome, self.email, self.telefone,self.endereco, self.id]
        if self.id is None:
            print("Erro: ID do cliente não está definido. Não é possível consultar.")
            return None
        sql = f'UPDATE {config.TABLE_NAME_CLIENT} SET nome = ?, email = ?, telefone = ?, endereco = ? WHERE id = ?'
        return self._atualizar_banco(config.DB_FILE_CLIENT, sql, dados)

    def consultar(self):
        if self.id is None:
            print("Erro: ID do cliente não está definido. Não é possível consultar.")
            return None
        dados_cliente = self._consultar_por_id_banco(config.DB_FILE_CLIENT, config.TABLE_NAME_CLIENT, self.id)
        if dados_cliente is None:
            print(f"Erro: Cliente com id {self.id} não encontrado.")
            return None
        self.id, self.nome, self.email, self.telefone, self.endereco = dados_cliente
        print(f"Cliente: {self.id}, {self.nome}, {self.email}, {self.telefone}, {self.endereco}")       
        return dados_cliente
    
    @staticmethod
    def consultar_geral_client():
        # Chama a função para consultar todos os registros na tabela client
        return Client._consultar_geral(config.DB_FILE_CLIENT, config.TABLE_NAME_CLIENT)

    def excluir(self):
        self._excluir_do_banco(config.DB_FILE_CLIENT,config.TABLE_NAME_CLIENT,self.id)
