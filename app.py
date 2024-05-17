from login import Login
from usuario import CriarConta
import os

def limpar_console():
    """
    Limpa o console
    """
    os.system('cls')


contas = {}
def opcoes_do_programa():
    """
    Exibe as opções do programa

    Outpt: Opções
    """
    print('\n1 - Criar conta')
    print('2 - Fazer login\n')
    print('━' * 69)

def registrar_conta(usuario, senha):
    """
    Registra as contas que são criadas
    """
    global contas
    contas[usuario] = [usuario, senha]

def selecionar_opcoes():
    """
    Selecionar as opções 
    """
    opcao_escolhida = int(input('\nEscolha a opção desejada: '))

    if opcao_escolhida == 1:
        criar_conta()
    else:
        # Vai tentar fazer o login
        try:
            fazer_login()
        except:
             limpar_console()
             input('\nErro! Parace que você está tentando fazer o login sem ter uma conta. Aperte uma tecla qualquer para continuar: ')
             main()

def fazer_login():
    """
    Faz o login
    """
    for usuario, credenciais in contas.items():
        nome = credenciais[0]
        senha = credenciais[1]

    usuario_login = Login(nome, senha)
    usuario_login.validar_conta()

def criar_conta():
    """
    Cria uma conta

    Input: Usuário e senha
    """
    usuario = input('\nQual será seu nome de usuário: ')
    senha = input('Qual será a senha do usuário: ')
    registrar_conta(usuario, senha)
    usuario_registrado = CriarConta(usuario, senha)
    limpar_console()
    main()
    

def titulo_do_programa():
    """
    Título

    Output: título
    """
    print("""
███████╗██╗░░░░░███████╗████████╗██████╗░░█████╗░███╗░░██╗██╗░█████╗░
██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██║██╔══██╗
█████╗░░██║░░░░░█████╗░░░░░██║░░░██████╔╝██║░░██║██╔██╗██║██║██║░░╚═╝
██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══██╗██║░░██║██║╚████║██║██║░░██╗
███████╗███████╗███████╗░░░██║░░░██║░░██║╚█████╔╝██║░╚███║██║╚█████╔╝
╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░╚════╝░

        ██████╗░░█████╗░██╗░░░░░░█████╗░░█████╗░███████╗
        ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝
        ██████╔╝███████║██║░░░░░███████║██║░░╚═╝█████╗░░
        ██╔═══╝░██╔══██║██║░░░░░██╔══██║██║░░██╗██╔══╝░░
        ██║░░░░░██║░░██║███████╗██║░░██║╚█████╔╝███████╗
        ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝
""")
    
    print('━' * 69)

def main():
    """
    Execuução do programa
    """
    titulo_do_programa()
    opcoes_do_programa()
    selecionar_opcoes()

if __name__ == '__main__':
    main()