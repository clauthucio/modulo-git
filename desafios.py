"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Bem-vindo ao Desafio de Git!"
    """
    mensagem = "Bem-vindo ao Desafio de Git!"
    return mensagem

def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    comandos = [
        "git init",
        "git add",
        "git commit",
        "git status",
        "git push",
    ]
    return comandos


def criar_mensagem_commit(funcao_nome):
    """
    Recebe o nome de uma função e retorna uma mensagem de commit padronizada.
    Exemplo:
    criar_mensagem_commit("listar_comandos_git_basicos") ->
    "Implementa função listar_comandos_git_basicos"
    """
    pass


def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    pass


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    pass

def menu():
    """
    Exibe um menu simples para testar o programa.
    Dica: use um while True e input() para ler opções do usuário.
    """
    while True:
        print("\n--- MENU TO-DO ---")
        print("1 - Mostrar mensagem inicial")
        print("2 - Listar comandos Git básicos")
        print("3 - Criar mensagem de commit")
        print("4 - Verificar tag válida")
        print("5 - Gerar relatório final")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print(mostrar_mensagem_inicial())
        elif opcao == "2":
            print(listar_comandos_git_basicos())
        elif opcao == "3":
            funcao_nome = int(input("Nome da função: "))
            criar_mensagem_commit(funcao_nome)
        elif opcao == "4":
            tag = int(input("Validar tag: "))
            verificar_tag_valida(tag)
        elif opcao == "5":
            funcoes_concluidas = input("Listar funções implementadas: ")
            gerar_relatorio_final(funcoes_concluidas)
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
if __name__ == "__main__":
    menu()