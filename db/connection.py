from connections import config


sql_client = (f'CREATE TABLE IF NOT EXISTS {config.TABLE_NAME_CLIENT}'
'('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT NOT NULL,'
    'email TEXT NOT NULL UNIQUE,'
    'telefone TEXT NOT NULL,'
    'endereco TEXT NOT NULL UNIQUE'
')')

sql_product = (f'CREATE TABLE IF NOT EXISTS {config.TABLE_NAME_PRODUCT}'
'('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT NOT NULL UNIQUE,'
    'precoUnitario REAL NOT NULL,'
    'unidade TEXT NOT NULL'
')')

sql_invoice = (f'CREATE TABLE IF NOT EXISTS {config.TABLE_NAME_INVOICE}'
'('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'client_id INTEGER NOT NULL,'
    'dataEmissao INTEGER NOT NULL,'
    'valorTotal REAL NOT NULL,'
    'status TEXT CHECK(status IN ("Paga", "Pendente", "Vencida", "Cancelada")) NOT NULL,'
    'FOREIGN KEY (client_id) REFERENCES client(id)'
')')

sql_invoice_items = (f'CREATE TABLE IF NOT EXISTS {config.TABLE_NAME_INVOICE_ITEMS}'
'('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'invoice_id INTEGER NOT NULL,'
    'product_id INTEGER NOT NULL,'
    'quantidade INTEGER NOT NULL,'
    'subtotal REAL NOT NULL,'
    'FOREIGN KEY (invoice_id) REFERENCES invoice(id),'
    'FOREIGN KEY (product_id) REFERENCES product(id)'
')')

tables = {
    config.DB_FILE_CLIENT: sql_client,
    config.DB_FILE_PRODUCT: sql_product, 
    config.DB_FILE_INVOICE: sql_invoice,
    config.DB_FILE_INVOICE_ITEMS: sql_invoice_items
}

for db, sql in tables.items():
    config.create_table(db, sql)
