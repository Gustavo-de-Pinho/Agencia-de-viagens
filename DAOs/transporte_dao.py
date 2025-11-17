from DAOs.dao import DAO
from model.transporte import Transporte
from model.empresa import Empresa

class TransporteDAO(DAO):
    def __init__(self):
        super().__init__('transporte.pkl')

    def add(self, transporte: Transporte):
        if((transporte is not None) and isinstance(transporte, Transporte) and isinstance(transporte.empresa, Empresa)):
            novo_id = super().generate_next_id()
            transporte.id = novo_id
            super().add(novo_id, transporte)

    def update(self, transporte: Transporte):
        if((transporte is not None) and isinstance(transporte, Transporte) and isinstance(transporte.empresa, Empresa)):
            super().update(transporte.id, transporte)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)