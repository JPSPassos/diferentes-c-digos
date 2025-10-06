#Atividade 1
sequencia = 0
while sequencia <= 10:
    print (sequencia)
    sequencia += 1

#Atividade 2
Digite_nomes = input
while True:
    nome = Digite_nomes("Digite um nome ou 'sair' para encerrar: ")
    if nome == "sair":
        break
    print("Você digitou:", nome)

pares = 0
while pares <= 20:
    if pares % 2 == 0:
        print(pares)
    pares += 1

#Atividade 3
chamada = 0
while chamada <= 10:
    chamada += 1
    if chamada == 5:
        print('Aluno de atestado')
        continue
    print('Aluno presente', chamada)

# Atividade 4
tentativas = 0
while tentativas < 3:
    senha = input('Coloque a senha: ')
    if senha == "1234":
        print('Acesso permitido')
        break
    tentativas += 1
    if tentativas == 3:
        print('Acesso bloqueado')