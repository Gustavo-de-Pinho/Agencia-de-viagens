from DAOs.dao import DAO
from model.passeio_turistico import PasseioTuristico

class PasseioTuristicoDAO(DAO):
    def __init__(self):
        super().__init__('passeioturistico.pkl')

    def add(self, passeio_turistico: PasseioTuristico):
        if((passeio_turistico is not None) and isinstance(passeio_turistico, PasseioTuristico) and isinstance(passeio_turistico.nome, str)):
            novo_id = super().generate_next_id()
            passeio_turistico.id = novo_id
            super().add(novo_id, passeio_turistico)

    def update(self, passeio_turistico: PasseioTuristico):
        if((passeio_turistico is not None) and isinstance(passeio_turistico, PasseioTuristico) and isinstance(passeio_turistico.nome, str)):
            super().update(passeio_turistico.id, passeio_turistico)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)