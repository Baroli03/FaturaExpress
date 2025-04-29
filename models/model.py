# Superclasse Base (Model)

# A superclasse pode ter os métodos que gerenciam a interação com o banco de dados, como:

#     salvar_no_banco(): Insere ou atualiza os dados no banco.

#     excluir(): Remove o registro do banco.

#     atualizar(): Atualiza os dados do registro no banco.

#     consultar_por_id(): Recupera um registro a partir de seu ID.

#     E outros métodos que possam ser comuns a todos os modelos.
# Subclasses (Cliente, Produto, Fatura, etc.)

# As subclasses (como Cliente, Produto, etc.) herdam essas funcionalidades da superclasse,
# e podem personalizar ou estender se necessário.
# Elas terão os atributos específicos de cada entidade (cliente, produto, fatura),
# mas o processo de persistência será tratado pela superclasse.
from abc import ABC, abstractmethod
import sqlite3
from pathlib import Path


class Model(ABC):
    def _excluir_do_banco(self, db_file: Path,table: str, id: int):
        """Método interno. Não utilize diretamente, use métodos específicos nas subclasses."""
        tabelas_permitidas = {"client", "invoice", "invoice_items", "product"}
        if table not in tabelas_permitidas:
            raise ValueError("Tabela não permitida!")
        sql = f"DELETE FROM {table} WHERE id = ?"
        with sqlite3.connect(db_file) as connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM {table} WHERE id = ?", (id,))
                cliente = cursor.fetchone() 
                # fetchone Retorna o primeiro registro referente ao comando do cursor.execute
                # fetchall retorna todos os resultados
                if cliente:
                    resposta = input(f'Você tem certeza que deseja excluir este {table}? [1] = sim // [2] = não: ')
                    while resposta not in ('1', '2'):  # Verifica se a resposta é válida
                        resposta = input('Opção inválida. Escolha [1] para sim e [2] para não: ')
                    if int(resposta) == 1:
                        cursor.execute(sql, (id,))
                        connection.commit() 
                        print(f"{table} {id} excluído com sucesso.")
                    else:
                        print("Código não salvo")
                else:
                    print(f"{table} com id {id} não encontrado.")
    

    def _atualizar_banco(self, db_file: Path, sql: str, lista_de_dados: list):
        try:
            with sqlite3.connect(db_file) as connection:
                cursor = connection.cursor()
                cursor.execute(sql, lista_de_dados)  # Usando execute para um único conjunto de dados
                connection.commit()
        except sqlite3.Error as e:
            print("Erro ao atualizar banco:", e)

    def _consultar_por_id_banco(self, db_file: Path, table: str, id: int):
        tabelas_permitidas = {"client", "invoice", "invoice_items", "product"}
        if table not in tabelas_permitidas:
            raise ValueError("Tabela não permitida!")
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table} WHERE id = ?", (id,))
            current_table = cursor.fetchone() 
            if current_table:
                return current_table 
            else:
                print(f"{table} com id {id} não encontrado.")
                return None 

    # Sql será criado via classe filha no caso 'Client' ou 'Product'
    #Salvar_no_banco Recebe arquivo para abrir o connect (onde está a url do banco)  

    def _salvar_no_banco(self, db_file: Path, sql: str, lista_de_dados: list, table: str, coluna: str, resposta: str ):
        colunas_permitidas = {"nome", "client_id", "invoice_id"}
        if coluna not in colunas_permitidas:
            raise ValueError("coluna não permitida!")
        """Método interno. Não utilize diretamente, use métodos específicos nas subclasses.""" 
        try:
            with sqlite3.connect(db_file) as connection:
                cursor = connection.cursor()

                # Executando a consulta para inserir os dados
                if isinstance(lista_de_dados[0], (list, tuple)):
                    cursor.executemany(sql, lista_de_dados)
                else:
                    cursor.execute(sql, lista_de_dados)

                # Obtendo o ID gerado automaticamente para a última inserção
                self.id = cursor.lastrowid

                if self.id is None:
                    raise ValueError(f"Erro ao salvar o {table}. ID não foi atribuído.")

                # Confirmando a inserção no banco
                connection.commit()
                return  self.id

        except sqlite3.IntegrityError as e:
            # Tentar buscar o ID manualmente
            with sqlite3.connect(db_file) as conn:
                cur = conn.cursor()
                cur.execute(f"SELECT id FROM {table} WHERE {coluna} = ?", (resposta,))
                row = cur.fetchone()
                if row:
                    self.id = row[0]
                else:
                    print("Erro: registro já existia mas não foi possível encontrar ID.")
        except Exception as e:
            print("Erro ao salvar no banco:", e)


    @abstractmethod
    def salvar(self):
        pass
    
    @abstractmethod
    def atualizar(self, id: int):
        pass
    
    @abstractmethod
    def consultar(self, id: int):
        pass
    
    @abstractmethod
    def excluir(self, id: int):
        pass

