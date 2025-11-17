from DAOs.dao import DAO
from model.pacote import Pacote


class PacoteDAO(DAO):
    def __init__(self):
        super().__init__("pacote.pkl")

    def add(self, pacote):
        if isinstance(pacote, Pacote):
            novo_id = super().generate_next_id()
            pacote.id = novo_id
            super().add(novo_id, pacote)

    def update(self, pacote):
        if isinstance(pacote, Pacote):
            super().update(pacote.id, pacote)

    def get(self, id):
        if isinstance(id, int):
            return super().get(id)
        
    def remove(self, id):
        if isinstance(id, int):
            return super().remove(id)