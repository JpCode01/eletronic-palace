class CriarConta:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def __str__(self):
        return f'Login: {self.login} | Senha: {self.senha}'
        