from connections import config
from .model import Model


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

