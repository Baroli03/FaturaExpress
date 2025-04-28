from models.client_model import Client
from models.product_model import Product
from models.invoice_model import Invoice
from models.invoice_items_model import InvoiceItems




cliente = Client("Fulano", "fulano@email.com", "12345", "Rua 1")
cliente.salvar()
cliente.consultar()

p = Product("leite", 2.45, "unitario")
p.salvar()
p.consultar()

i = Invoice(cliente, 20, 3.4, "Paga", 12)
i.consultar()



j = Invoice(cliente, 3, 4.4, "Pendente", 12)
j.consultar()