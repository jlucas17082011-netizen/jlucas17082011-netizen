# Sistema de Cadastro de Pessoas
# Trabalho: Desenvolvimento de um aplicativo utilizando funções em Python
# O programa funciona no terminal e armazena os cadastros durante a execução.

def exibir_menu():
    """Mostra as opções disponíveis para o usuário."""
    print("\n" + "=" * 40)
    print("       SISTEMA DE CADASTRO DE PESSOAS")
    print("=" * 40)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas cadastradas")
    print("3 - Buscar pessoa pelo nome")
    print("4 - Remover pessoa")
    print("5 - Sair")
    print("=" * 40)


def cadastrar_pessoa(pessoas):
    """Recebe os dados de uma pessoa e adiciona à lista de cadastros."""
    print("\n--- NOVO CADASTRO ---")
    nome = input("Nome completo: ").strip()
    if nome == "":
        print("O nome não pode ficar vazio.")
        return

    idade_texto = input("Idade: ").strip()
    if not idade_texto.isdigit():
        print("Idade inválida. Digite somente números.")
        return

    idade = int(idade_texto)
    if idade < 0:
        print("A idade não pode ser negativa.")
        return

    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    pessoa = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email
    }

    pessoas.append(pessoa)
    print(f"Cadastro de {nome} realizado com sucesso!")


def listar_pessoas(pessoas):
    """Exibe todos os registros armazenados."""
    print("\n--- PESSOAS CADASTRADAS ---")
    if len(pessoas) == 0:
        print("Ainda não existem pessoas cadastradas.")
    else:
        for numero, pessoa in enumerate(pessoas, start=1):
            print(f"\nCadastro {numero}")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']} anos")
            print(f"Telefone: {pessoa['telefone']}")
            print(f"E-mail: {pessoa['email']}")


def buscar_pessoa(pessoas, nome_procurado):
    """Procura uma pessoa pelo nome e retorna o cadastro encontrado."""
    for pessoa in pessoas:
        if pessoa["nome"].lower() == nome_procurado.lower():
            return pessoa
    return None


def remover_pessoa(pessoas, nome_procurado):
    """Remove o cadastro correspondente ao nome informado."""
    pessoa = buscar_pessoa(pessoas, nome_procurado)
    if pessoa is not None:
        pessoas.remove(pessoa)
        print(f"Cadastro de {pessoa['nome']} removido com sucesso!")
    else:
        print("Pessoa não encontrada.")


def executar_sistema():
    """Controla o menu e a execução das funcionalidades."""
    pessoas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pessoa(pessoas)
        elif opcao == "2":
            listar_pessoas(pessoas)
        elif opcao == "3":
            nome = input("Digite o nome que deseja buscar: ").strip()
            resultado = buscar_pessoa(pessoas, nome)
            if resultado is not None:
                print("\nPessoa encontrada:")
                print(f"Nome: {resultado['nome']}")
                print(f"Idade: {resultado['idade']} anos")
                print(f"Telefone: {resultado['telefone']}")
                print(f"E-mail: {resultado['email']}")
            else:
                print("Pessoa não encontrada.")
        elif opcao == "4":
            nome = input("Digite o nome da pessoa que deseja remover: ").strip()
            remover_pessoa(pessoas, nome)
        elif opcao == "5":
            print("Sistema encerrado. Obrigado por utilizar!")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")


# Inicia o programa.
if __name__ == "__main__":
    executar_sistema()
