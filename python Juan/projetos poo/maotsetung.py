#ATT 1
class carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Ano: {self.ano}"
    
    def apresentar(self):
        return f"Este carro é um {self.marca} do ano {self.ano}."

kwid = carro("Renault", 2020)
print(kwid.exibir_informacoes())
print(kwid.apresentar())

#ATT 2
class usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        mostrar_login = self.login
        mostrar_senha = self.senha
        print(f"Login: {mostrar_login}, Senha: {mostrar_senha}")
usuario1 = usuario("maotsetung", "12345")

#ATT 3
class desconto:
    desconto = 20
    def __init__(self, nome):
        self.preco = nome
    def __init__(self, saldo):
        self.saldo = saldo

    saldo = 100
    print(f"Saldo com desconto: {saldo - (saldo * desconto / 100)}")

#ATT 4
class compra:
    valor_compra = 100
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    def valor_final(self):
        return self.valor - (self.valor * 0.20)
compra1 = compra("maotsetung", 100)
print(f"Valor final da compra: {compra1.valor_final()}")

#ATT 5
