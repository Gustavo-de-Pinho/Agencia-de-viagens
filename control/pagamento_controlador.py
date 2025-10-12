from view.pagamento_tela import PagamentoTela
from model.pagamento import Pagamento
from model.cartao_credito import CartaoCredito
from model.pix import Pix
from model.dinheiro import Dinheiro

class PagamentoControlador:
    def __init__(self, sistema_controlador):
        self.__pagamentos = []
        self.__tela = PagamentoTela()
        self.__sistema_controlador = sistema_controlador

    def pagamento_pix(self):
        dados = self.__tela.pagamento_pix()
        if dados is not None:
            pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(dados["cpf_membro"])

            if pessoa is not None:
                self.__pagamentos.append(Pix(pessoa, dados["valor"], dados["cpf_pagador"]))
                self.__tela.mostrar_mensagem("PAGAMENTO REALIZADO")
            else:
                self.__tela.mostrar_mensagem("PESSOA NÃO EXISTE")
        else:
            self.__tela.mostrar_mensagem("DADOS INVÁLIDOS")
        