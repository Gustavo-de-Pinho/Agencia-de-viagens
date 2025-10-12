from model.pessoa import Pessoa
from model.cidade import Cidade
from model.transporte import Transporte
from model.passagem import Passagem

from view.passagem_tela import PassagemTela

class PassagemControlador:
    def __init__(self, sistema_controlador):
        self.sistema_controlador = sistema_controlador
        self.view = PassagemTela()
        self.passagens_cadastradas = []
        self.cidades_disponiveis = {
            "são paulo": Cidade(nome="São Paulo"),
            "rio de janeiro": Cidade(nome="Rio de Janeiro"),
            "florianópolis": Cidade(nome="Florianópolis"),
        }


    def _calcular_valor_passagem(self, dados_transporte: Transporte, cidade_origem: Cidade, cidade_destino: Cidade) -> float:
        valor_base = 150.0  
        
        #regra imaginárias aqui
        
        return valor_base

    def run(self):
        while True:
            opcao = self.view.mostra_opcoes()
            if opcao == '1':
                self.criar_nova_passagem()
            elif opcao == '2':
                self.listar_todas_passagens()
            elif opcao == '0':
                self.view.mostrar_mensagem("Retornando ao menu principal...")
                break
            else:
                self.view.mostrar_mensagem("Opção inválida. Tente novamente.")

    def criar_nova_passagem(self):
        try:
            # 1. View coleta os dados (sem o valor)
            dados_brutos = self.view.obter_dados_nova_passagem()

            # 2. Controller aplica REGRA DE NEGÓCIO de validação
            if dados_brutos["cidade_origem_nome"].lower() == dados_brutos["cidade_destino_nome"].lower():
                self.view.mostrar_mensagem("Erro: A cidade de origem não pode ser igual à de destino.")
                return

            # 3. Controller cria os objeto necessários
            pessoa = Pessoa(dados_brutos["nome_pessoa"], dados_brutos["cpf_pessoa"])
            transporte = Transporte(dados_brutos["tipo_transporte"], dados_brutos["empresa_transporte"])
            
            # Usando sua classe Cidade
            # Para um sistema real, aqui buscaríamos a cidade em um banco de dados
            # ou criaríamos uma nova se não existisse.
            cidade_origem = self.cidades_disponiveis.get(dados_brutos["cidade_origem_nome"].lower(), Cidade(nome=dados_brutos["cidade_origem_nome"]))
            cidade_destino = self.cidades_disponiveis.get(dados_brutos["cidade_destino_nome"].lower(), Cidade(nome=dados_brutos["cidade_destino_nome"]))

            # 4. Controller executa a REGRA DE NEGÓCIO para calcular o valor
            valor_calculado = self._calcular_valor_passagem(transporte, cidade_origem, cidade_destino)

            # 5. Controller cria o objeto Passagem principal com o valor calculado
            nova_passagem = Passagem(
                pessoa=pessoa,
                valor=valor_calculado,
                transporte=transporte,
                cidade_origem=cidade_origem,
                cidade_destino=cidade_destino
            )

            # 6. Armazena o resultado
            self.passagens_cadastradas.append(nova_passagem)

            # 7. View exibe o sucesso
            self.view.mostrar_mensagem("Passagem cadastrada com sucesso!")
            # Opcional: mostrar os detalhes da passagem recém-criada
            self.view.mostrar_passagem(nova_passagem)

        except Exception as e:
            self.view.mostrar_mensagem(f"Ocorreu um erro inesperado: {e}")

    def listar_todas_passagens(self):
        self.view.mostrar_lista_passagens(self.passagens_cadastradas)