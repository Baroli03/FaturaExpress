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