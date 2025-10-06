#AT 1
class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor      
    def exibir_info(self):
        return f"{self.titulo}, escrito por {self.autor}."
class usuario:
    def __init__(self, nome, código):
        self.nome = nome
        self.código = código
    def exibir_info(self):
        return f"Usuário: {self.nome}, Código: {self.código}."
    
#AT 2
class jogador:
    def __init__(self, nome, pontos = 0):
        self.nome = nome
        self.pontos = pontos
    def exibir_info(self):
        return f"Jogador: {self.nome}, Pontos: {self.pontos}."
    def adicionar_pontos(self, pontos):
        self.pontos += pontos
        self.exibir_info()