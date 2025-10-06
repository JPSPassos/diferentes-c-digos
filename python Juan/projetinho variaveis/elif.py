#Atividade 1
pagamento = input('Escolha o método de pagamento: ')

if pagamento == 'cartão':
    print('Pagamento com cartão')
elif pagamento == 'boleto':
    print('Gerando boleto')
else:
    print('Método de pagamento inválido')

#Atividade 2
idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Criança')
elif idade > 13 and idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade <= 59:
    print('Adulto')
else:
    print('Idoso')

#Atividade 3
entrega = input('Escolha o método de entrega: ')

if entrega == 'padrão':
    print('Entrega padrão selecionada. Preço R$ 10,00')
elif entrega == 'express':
    print('Entrega expressa selecionada. Preço R$ 20,00')
else:
    print('Método de entrega inválido')