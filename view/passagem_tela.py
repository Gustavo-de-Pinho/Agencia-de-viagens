from model.passagem import Passagem

class PassagemTela:
    def mostra_opcoes(self):
        print("====== OPÇÕES ======")
        print("> (1) Cadastrar Passagem")
        print("> (2) Listar Passagens")
        print("> (3) Mostrar dado Passagem")
        print("> (0) Sair")
        print("=====================")
        print()

        opcao = input("Escolha uma opção: ")

        #Tenta converter o input em inteiro. Se falhar retorna None
        try:
            opcao = int(opcao)
            return opcao
        except:
            return None

    def obter_dados_nova_passagem(self) -> dict:
        print("\n--- Cadastro de Nova Passagem ---")
        dados = {
            "nome_pessoa": input("Nome do passageiro: "),
            "cpf_pessoa": input("CPF do passageiro: "),
            "tipo_transporte": input("Tipo de transporte (Ex: Ônibus, Avião): "),
            "empresa_transporte": input("Empresa de transporte: "),
            "cidade_origem_nome": input("Cidade de origem: "),
            "cidade_destino_nome": input("Cidade de destino: "),
        }
        return dados

    def mostrar_passagem(self, passagem: Passagem):
        print("\n--- Detalhes da Passagem ---")
        print(f"Passageiro: {passagem.pessoa.nome} (CPF: {passagem.pessoa.cpf})")
        print(f"Origem: {passagem.cidade_origem.nome}")
        print(f"Destino: {passagem.cidade_destino.nome}")
        print(f"Transporte: {passagem.transporte.tipo} ({passagem.transporte.empresa})")
        print(f"Valor Calculado: R$ {passagem.valor:.2f}") # Informa que o valor é calculado
        print("----------------------------\n")

    def mostrar_lista_passagens(self, passagens: list[Passagem]):
        print("\n--- Lista de Passagens Cadastradas ---")
        if not passagens:
            print("Nenhuma passagem cadastrada.")
        else:
            for i, passagem in enumerate(passagens, 1):
                print(f"{i}. {passagem.pessoa.nome} -> {passagem.cidade_destino.nome} (R$ {passagem.valor:.2f})")
        print("--------------------------------------\n")