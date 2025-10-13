class PassagemTela:
    def mostra_opcoes(self) -> int:
        print("========== PASSAGENS ==========")
        print("> (1) Emitir Nova Passagem")
        print("> (2) Alterar Passagem")
        print("> (3) Listar Passagens Emitidas")
        print("> (4) Cancelar Passagem")
        print("-----------------------------")
        print("> (0) Retornar")
        print("================================")
        print()
        
        return int(input("Escolha uma opção: "))
    
    def mostra_mensagem(self, msg: str):
        print(msg)
    
    def seleciona_pessoa_por_cpf(self) -> str:
        return input("Digite o CPF do passageiro: ")
        
    def seleciona_transporte_por_id(self) -> int:
        return int(input("Digite o ID (índice) do transporte: "))

    def seleciona_cidade(self, tipo: str) -> str:
        return input(f"Digite o nome da cidade de {tipo}: ")
        
    def pega_valor_passagem(self) -> float:
        return float(input("Digite o valor da passagem (ex: 250.75): "))

    def mostra_passagem(self, dados: dict):
        print(f"\n--- PASSAGEM ID: {dados['id']} ---")
        print(f"  Passageiro: {dados['passageiro']} (CPF: {dados['cpf']})")
        print(f"  Rota: {dados['origem']} -> {dados['destino']}")
        print(f"  Transporte: {dados['transporte']}")
        print(f"  Valor: R$ {dados['valor']:.2f}")

    def pega_dados_para_alterar(self, dados_atuais: dict) -> dict:
        """Solicita novos dados para a passagem, mostrando os atuais."""
        print("\n--- ALTERANDO DADOS DA PASSAGEM ---")
        print("(Deixe em branco e pressione Enter para manter o valor atual)")
        
        novo_cpf = input(f"CPF do Passageiro ({dados_atuais['cpf']}): ")
        novo_id_transporte = input(f"ID do Transporte ({dados_atuais['id_transporte']}): ")
        nova_origem = input(f"Cidade de Origem ({dados_atuais['origem']}): ")
        nova_destino = input(f"Cidade de Destino ({dados_atuais['destino']}): ")
        novo_valor = input(f"Valor ({dados_atuais['valor']}): ")

        return {
            "cpf": novo_cpf or dados_atuais['cpf'],
            "id_transporte": int(novo_id_transporte) if novo_id_transporte else dados_atuais['id_transporte'],
            "origem": nova_origem or dados_atuais['origem'],
            "destino": nova_destino or dados_atuais['destino'],
            "valor": float(novo_valor) if novo_valor else dados_atuais['valor'],
        }
    
    def seleciona_passagem_por_id(self) -> int:
        return int(input("Digite o ID da passagem que deseja cancelar: "))