from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent / 'Data'
ROOT_DIR.mkdir(exist_ok=True)
DBNAME_CLIENT = 'client.sqlite3'
DB_FILE_CLIENT = ROOT_DIR / DBNAME_CLIENT
TABLE_NAME_CLIENT = 'client'

# Criando bd de produto
TABLE_NAME_PRODUCT = 'product'
DBNAME_PRODUCT = 'product.sqlite3'
DB_FILE_PRODUCT = ROOT_DIR / DBNAME_PRODUCT

# Criando bd de Faturas
TABLE_NAME_INVOICE = 'invoice'
DBNAME_INVOICE = 'invoice.sqlite3'
DB_FILE_INVOICE = ROOT_DIR / DBNAME_INVOICE

# Criando bd de itens da Faturas
TABLE_NAME_INVOICE_ITEMS = 'invoice_items'
DBNAME_INVOICE_ITEMS = 'invoiceitems.sqlite3'
DB_FILE_INVOICE_ITEMS = ROOT_DIR / DBNAME_INVOICE_ITEMS
