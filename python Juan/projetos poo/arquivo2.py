#AT 1
import arquivo1 as a1

livro = a1.livro("1984", "George Orwell")
usuario = a1.usuario("Alice", 12345)
print(livro.exibir_info())
print(usuario.exibir_info())

#AT 2
jogador = a1.jogador("Bob")
jogador.adicionar_pontos(10)
print(jogador.exibir_info())