from models.client_model import Client
from models.product_model import Product
from models.invoice_model import Invoice
from models.invoice_items_model import InvoiceItems




cliente = Client("Fulano", "fulano@email.com", "12345", "Rua 1")
cliente.salvar()
cliente.consultar()
