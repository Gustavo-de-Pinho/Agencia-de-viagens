from view.pagamento_tela import PagamentoTela
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
            grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(dados["codigo"])
            pessoa_em_grupo = self.__sistema_controlador.grupo_controlador.pessoa_em_grupo(pessoa, grupo)

            if pessoa is not None and grupo is not None and pessoa_em_grupo:
                self.__pagamentos.append(Pix(pessoa, grupo, dados["valor"], dados["cpf_pagador"]))
                self.__tela.mostrar_mensagem("PAGAMENTO REALIZADO")
            else:
                self.__tela.mostrar_mensagem("PESSOA OU GRUPO NÃO RELACIONADOS")
        else:
            self.__tela.mostrar_mensagem("DADOS INVÁLIDOS")
        
    def pagamento_cartao(self):
        dados = self.__tela.pagamento_cartao()

        if dados is not None:
            pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(dados["cpf_membro"])
            grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(dados["codigo"])
            pessoa_em_grupo = self.__sistema_controlador.grupo_controlador.pessoa_em_grupo(pessoa, grupo)

            if pessoa is not None and grupo is not None and pessoa_em_grupo:
                self.__pagamentos.append(CartaoCredito(pessoa, grupo, dados["valor"], dados["bandeira"]))
                self.__tela.mostrar_mensagem("PAGAMENTO REALIZADO")
            else:
                self.__tela.mostrar_mensagem("PESSOA OU GRUPO NÃO RELACIONADOS")
        else:
            self.__tela.mostrar_mensagem("DADOS INVÁLIDOS")

    def pagamento_dinheiro(self):
        dados = self.__tela.pagamento_dinheiro()

        if dados is not None:
            pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(dados["cpf_membro"])
            grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(dados["codigo"])
            pessoa_em_grupo = self.__sistema_controlador.grupo_controlador.pessoa_em_grupo(pessoa, grupo)

            if pessoa is not None and grupo is not None and pessoa_em_grupo:
                self.__pagamento.append(Dinheiro(pessoa, grupo, dados["valor"]))
                self.__tela.mostrar_mensagem("PAGAMENTO REALIZADO")
            else:
                self.__tela.mostrar_mensagem("PESSOA OU GRUPO NÃO RELACIONADOS")
        else:
            self.__tela.mostrar_mensagem("DADOS INVÁLIDOS")

    def listar_pagamentos(self):
        cpf = self.__tela.pegar_cpf_lista()
        pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(cpf)

        for pagamento in self.__pagamentos:
            if pagamento.pessoa == pessoa:
                if isinstance(pagamento, Pix):
                    pagamento_dict = {pagamento.pessoa,
                                    pagamento.grupo,
                                    pagamento.valor,
                                    pagamento.cpf_pagador,
                                    }
                elif isinstance(pagamento, CartaoCredito):
                    pagamento_dict = {pagamento.pessoa,
                                    pagamento.grupo,
                                    pagamento.valor,
                                    pagamento.numero_cartao,
                                    pagamento.bandeira_cartao}
                    
                else:
                    pagamento_dict = {pagamento.pessoa, pagamento.grupo, pagamento.valor}

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

            elif opcao == 4:
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

            elif opcao == 4:
                break

            else:
                self.__tela.mostrar_mensagem("OPÇÃO INVÁLIDA")