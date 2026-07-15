import os
import subprocess
import sys


descricoes_receitas = [
    "Salário",
    "Freelancer",
    "Venda de produto",
    "Venda de curso",
    "Comissão",
    "13º salário",
    "Bonificação",
    "Reembolso",
    "Presente",
    "Rendimento de investimentos"
]

descricoes_despesas = [
    "Mercado",
    "Aluguel",
    "Conta de luz",
    "Conta de água",
    "Internet",
    "Telefone",
    "Gasolina",
    "Transporte",
    "Academia",
    "Farmácia",
    "Restaurante",
    "Lazer",
    "Streaming",
    "Compras",
    "Educação",
    "Impostos",
    "Manutenção",
    "Presente",
    "Outros"
]

movimentacoes = []


def limpar_tela():
    subprocess.run(
        "cls" if os.name == "nt" else "clear",
        shell=True
    )


def exibir_nome_do_programa():
    print("=" * 70)
    print("      Seja muito bem vindo ao nosso Sistema de Controle Financeiro")
    print("=" * 70)
    input("\n- Pressione ENTER para acessar o menu...")


def mostrar_menu():
    print("\nSelecione uma das opções abaixo:\n")

    print("[1]  Adicionar receita")
    print("[2]  Adicionar despesa")
    print("[3]  Ver saldo")
    print("[4]  Listar movimentações")
    print("[5]  Excluir movimentação")
    print("[6]  Resumo financeiro")
    print("[7]  Sair")


def exibir_subtitulo(texto):
    limpar_tela()
    print(texto)
    print("-" * 45)


def voltar_menu():
    input("\nPressione ENTER para voltar ao menu principal...")


def processar_opcao():

    try:
        opcao = int(input("Escolha: "))

        if opcao == 1:
            adicionar_receita()

        elif opcao == 2:
            adicionar_despesa()

        elif opcao == 3:
            mostrar_saldo()

        elif opcao == 4:
            listar_movimentacoes()

        elif opcao == 5:
            excluir_movimentacao()
        
        elif opcao == 6:
            resumo_financeiro()
        
        elif opcao == 7:
            finalizar()

        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()


def escolher_descricao_receita():

    print("\nEscolha uma descrição:\n")

    for index, descricao in enumerate(descricoes_receitas, start=1):
        print(f"[{index}] {descricao}")

    try:
        opcao = int(input("\nEscolha: "))

        if 1 <= opcao <= len(descricoes_receitas):
            return descricoes_receitas[opcao - 1]

        else:
            print("Opção inválida!")
            return escolher_descricao_receita()

    except ValueError:
        print("Digite apenas números!")
        return escolher_descricao_receita()


def escolher_descricao_despesa():

    print("\nEscolha uma descrição:\n")

    for index, despesa in enumerate(descricoes_despesas, start=1):
        print(f"[{index}] {despesa}")

    try:
        opcao = int(input("\nEscolha: "))

        if 1 <= opcao <= len(descricoes_despesas):
            return descricoes_despesas[opcao - 1]

        else:
            print("Opção inválida!")
            return escolher_descricao_despesa()

    except ValueError:
        print("Digite apenas números!")
        return escolher_descricao_despesa()


def adicionar_receita():

    exibir_subtitulo("ADICIONAR RECEITA")

    print("Cadastre uma nova entrada de dinheiro.")
    print("-" * 41)

    descricao = escolher_descricao_receita()

    print(f"\n Descrição: {descricao}")

    try:
        valor = float(input(" Valor (R$): "))

        if valor <= 0:
            print("O valor precisa ser maior que zero.")
            voltar_menu()
            return

    except ValueError:
        print(" Digite um valor válido.")
        voltar_menu()
        return
    
    movimentacoes.append({
        "tipo": "receita",
        "descricao": descricao,
        "valor": valor
    })

    print("\nReceita cadastrada com sucesso!")
    

    voltar_menu()


def adicionar_despesa():

    exibir_subtitulo("ADICIONAR DESPESA")

    print("Cadastre uma nova saída de dinheiro.")
    print("-" * 41)

    descricao = escolher_descricao_despesa()

    print(f"\nDescrição: {descricao}")

    try:
        valor = float(input(" Valor (R$): "))

        if valor <= 0:
            print(" O valor precisa ser maior que zero.")
            voltar_menu()
            return

    except ValueError:
        print("Digite um valor válido.")
        voltar_menu()
        return

    movimentacoes.append({
        "tipo": "despesa",
        "descricao": descricao,
        "valor": valor
})

    print("\n Despesa cadastrada com sucesso!")

    voltar_menu()


def mostrar_saldo():

    exibir_subtitulo("SALDO ATUAL")

    saldo = 0

    for movimentacao in movimentacoes:

        if movimentacao["tipo"] == "receita":
            saldo += movimentacao["valor"]

        elif movimentacao["tipo"] == "despesa":
            saldo -= movimentacao["valor"]

    print(f"Seu saldo atual é: R$ {saldo:.2f}")

    voltar_menu()

def listar_movimentacoes():

    exibir_subtitulo("HISTÓRICO DE MOVIMENTAÇÕES")

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação cadastrada.")

    else:


        for index, movimentacao in enumerate(movimentacoes, start=1):

            print(f"\n{index}º Movimentação")
            print(f"Tipo: {movimentacao['tipo'].capitalize()}")
            print(f"Descrição: {movimentacao['descricao']}")
            print(f"Valor: R$ {movimentacao['valor']:.2f}")
            print("-" * 30)
    
    voltar_menu()

#====================================
#  Excluir movimentação
#====================================
def excluir_movimentacao():

    exibir_subtitulo("EXCLUIR MOVIMENTAÇÃO")

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação cadastrada.")
        voltar_menu()
        return

    for index, movimentacao in enumerate(movimentacoes, start=1):
        print(f"\n[{index}] {movimentacao['tipo'].capitalize()}")
        print(f"Descrição: {movimentacao['descricao']}")
        print(f"Valor: R$ {movimentacao['valor']:.2f}")

    print("-" * 45)

    try:
        escolha = int(input("Digite o número da movimentação que deseja excluir: "))

        if 1 <= escolha <= len(movimentacoes):

            removida = movimentacoes.pop(escolha - 1)

            print("\n Movimentação excluída com sucesso!")
            print(f"Descrição: {removida['descricao']}")
            print(f"Valor: R$ {removida['valor']:.2f}")

        else:
            print("\n Número inválido!")

    except ValueError:
        print("\n Digite apenas números!")

    voltar_menu()


def resumo_financeiro():

    exibir_subtitulo(" RESUMO FINANCEIRO")

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação cadastrada.")
        voltar_menu()
        return

    total_receitas = 0
    total_despesas = 0
    quantidade_receitas = 0
    quantidade_despesas = 0

    for movimentacao in movimentacoes:

        if movimentacao["tipo"] == "receita":
            total_receitas += movimentacao["valor"]
            quantidade_receitas += 1

        elif movimentacao["tipo"] == "despesa":
            total_despesas += movimentacao["valor"]
            quantidade_despesas += 1

    saldo = total_receitas - total_despesas

    print(f"Total de receitas:      R$ {total_receitas:.2f}")
    print(f"Total de despesas:     R$ {total_despesas:.2f}")
    print("-" * 45)
    print(f"Saldo atual:           R$ {saldo:.2f}")
    print("-" * 45)
    print(f" Receitas cadastradas:  {quantidade_receitas}")
    print(f"Despesas cadastradas:  {quantidade_despesas}")
    print(f"Total de movimentações: {len(movimentacoes)}")

    voltar_menu()


def finalizar():
    exibir_subtitulo("Encerrando o sistema")

    print("Obrigado por utilizar o nosso sistema de controle financeiro!")
    print("Até a próxima.\n")

    sys.exit()


def opcao_invalida():

    print("\nOpção inválida!")
    print("Escolha uma opção entre 1 e 7.")

    voltar_menu()


def main():

    limpar_tela()
    exibir_nome_do_programa()

    while True:
        mostrar_menu()
        processar_opcao()

if __name__ == "__main__":
    main()







