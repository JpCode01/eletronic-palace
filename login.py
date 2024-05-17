from usuario import CriarConta
import os
import json

class Login(CriarConta):
    def __init__(self, login, senha):
        super().__init__(login, senha)

    def validar_conta(self):
        """
        Método para logar na conta 

        Input: Login e senha
        """
        continuar = True
        while continuar:
            input_login = input('Digite o seu login: ')
            input_senha = input('Digte a sua senha: ')
            
            if input_login == self.login and input_senha == self.senha:
                os.system('cls')
                print('Bem vindo a sua conta!')
                visualizar_eletronicos = input('Deseja visualizar os eletrônicos disponíveis na loja (s/n): ')
                if visualizar_eletronicos == 's':
                    eletronicos()
                    input('Pressione uma tecla qualquer: ')
                    limpar_console()
                    print('Obrigado por acessar o nosso site! 😉')
                else:
                    limpar_console()
                    print('Obrigado por acessar o nosso site! 😉')
                break

            else:
                os.system('cls')
                print('Usuário ou senha inválidos!')
                input_login = 0
                input_senha = 0
                continue
                

def limpar_console():
    os.system('cls')

def eletronicos():
    """
    Acessar o nome e o preço dos produtos disponíveis 
    """
    with open("dados.json") as dados_loja:
        dados_json = json.load(dados_loja)

    nomes = []
    precos = []

    for item in dados_json:
        nomes.append(item['name'])
        precos.append(item['price'])
    
    print('')

    for i in range(0, len(nomes), 1):
        print(f'{nomes[i].ljust(23)} | R${precos[i]}\n')

