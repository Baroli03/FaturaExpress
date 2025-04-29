from models.client_model import Client
from models.product_model import Product
from models.invoice_model import Invoice
from models.invoice_items_model import InvoiceItems


# Criação e salvamento do cliente
cliente2 = Client("joaquim", "eduardoaaa@hotmail.com", "2232313", "av são jogse")
cliente2.salvar()
cliente2.consultar()

# Criação e salvamento do produto
produto = Product("pudim", 5.00, "Unitario")
produto.salvar()
produto.consultar()

# Criação da fatura
fatura = Invoice(cliente2, "Pendente", 0.0)  # Passando "Pendente" como status válido
fatura.salvar()  # Salva a fatura no banco, o ID será gerado automaticamente
fatura.consultar()  # Agora a consulta deve funcionar corretamente, pois a fatura foi salva

# Agora cria o item da fatura
fatura_item = InvoiceItems(fatura, produto, 10)  # Criando o item da fatura com quantidade 10
fatura_item.salvar()  # Salva o item no banco
fatura_item.consultar()  # Consulta o item da fatura, deve funcionar agora
