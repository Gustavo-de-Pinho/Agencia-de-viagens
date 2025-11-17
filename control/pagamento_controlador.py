from view.pagamento_tela import PagamentoTela
from model.cartao_credito import CartaoCredito
from model.pix import Pix
from model.dinheiro import Dinheiro
from DAOs.pagamento_dao import PagamentoDAO
from datetime import datetime


class PagamentoControlador:
    def __init__(self, sistema_controlador):
        self.__pagamento_DAO = PagamentoDAO()
        self.__tela = PagamentoTela()
        self.__sistema_controlador = sistema_controlador

    def pagamento_padrao(self, dados: dict):
        pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(dados["cpf_membro"])
        grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(dados["codigo"])
        pacote = self.__sistema_controlador.pacote_controlador.pacote_grupo(grupo)
        data_pagamento = datetime.today()

        if pacote is not None:
            if data_pagamento < pacote.data_viagem:
                pacote.valor_pago += dados["valor"]

                if pacote.valor_pago >= pacote.valor_total:
                    pacote.pago = True

                return {"pessoa": pessoa, "grupo": grupo}
            else:
                self.__tela.mostrar_mensagem("VIAGEM JÁ ACONTECEU")
            return None
        else:
            self.__tela.mostrar_mensagem("PACOTE NÃO EXISTE OU JÁ FOI PAGO")

    def pagamento_pix(self):
        dados = self.__tela.pagamento_pix()
        pagamento = self.pagamento_padrao(dados)
        
        if pagamento is not None:
            self.__pagamento_DAO.add(Pix(pagamento["pessoa"], pagamento["grupo"], dados["valor"], dados["cpf_pagador"]))

    def pagamento_cartao(self):
        dados = self.__tela.pagamento_cartao()
        pagamento = self.pagamento_padrao(dados)

        if pagamento is not None:
            self.__pagamento_DAO.add(CartaoCredito(pagamento["pessoa"], pagamento["grupo"], dados["valor"], dados["numero_cartao"], dados["bandeira"]))

    def pagamento_dinheiro(self):
        dados = self.__tela.pagamento_dinheiro()
        pagamento = self.pagamento_padrao(dados)

        if pagamento is not None:
            self.__pagamento_DAO.add(Dinheiro(pagamento["pessoa"], pagamento["grupo"], dados["valor"]))

    def listar_pagamentos(self):
        cpf = self.__tela.pegar_cpf_lista()
        pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(cpf)

        for pagamento in self.__pagamento_DAO.get_all():
            if pagamento.pessoa == pessoa:
                if isinstance(pagamento, Pix):
                    pagamento_dict = {"pessoa": pagamento.pessoa.nome,
                                    "codigo_grupo": pagamento.grupo.codigo,
                                    "valor": pagamento.valor,
                                    "cpf_pagador": pagamento.cpf_pagador,
                                    "tipo": "PIX"}
                elif isinstance(pagamento, CartaoCredito):
                    pagamento_dict = {"pessoa": pagamento.pessoa.nome,
                                    "codigo_grupo": pagamento.grupo.codigo,
                                    "valor": pagamento.valor,
                                    "numero_cartao": pagamento.numero_cartao,
                                    "bandeira_cartao": pagamento.bandeira,
                                    "tipo": "Cartão de Crédito"}
                    
                else:
                    pagamento_dict = {"pessoa": pagamento.pessoa.nome, "codigo": pagamento.grupo.codigo, "valor": pagamento.valor, "tipo": "Dinheiro"}

                self.__tela.listar_pagamentos(pagamento_dict)

    def pagamentos_tela(self):
        opcoes = {
            1: self.pagamento_pix,
            2: self.pagamento_cartao,
            3: self.pagamento_dinheiro,
        }

        continua = True

        while continua:
            opcao = self.__tela.realizar_pagamento()

            if opcao is not None and opcao in opcoes:
                opcoes[opcao]()

            elif opcao == 0:
                break
            
            else:
                self.__tela.mostrar_mensagem("OPÇÃO INVÁLIDA")
                
    def abre_tela(self):
        opcoes = {
            1: self.pagamentos_tela,
            2: self.listar_pagamentos,
        }

        continua = True

        while continua:
            opcao = self.__tela.mostrar_opcoes()

            if opcao is not None and opcao in opcoes:
                opcoes[opcao]()

            elif opcao == 0:
                break

            else:
                self.__tela.mostrar_mensagem("OPÇÃO INVÁLIDA")