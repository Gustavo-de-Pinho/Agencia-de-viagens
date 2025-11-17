from DAOs.dao import DAO
from model.pagamento import Pagamento
from model.cartao_credito import CartaoCredito
from model.pix import Pix
from model.dinheiro import Dinheiro


class PagamentoDAO(DAO):
    def __init__(self):
        super().__init__("pagamento.pkl")

    def add(self, pagamento):
        if isinstance(pagamento, (CartaoCredito, Pix, Dinheiro)):
            novo_id = super().generate_next_id()
            super().add(novo_id, pagamento)

    def remove(self, id):
        if isinstance(id, int):
            super().remove(id)

    def get(self, id):
        if isinstance(id, int):
            return super().get(id)