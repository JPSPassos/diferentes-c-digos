def mostrar_menu():
    print("\n== PIZZARIA TERMINAL ===")
    print("1 - Ver Menu")
    print("2 - Fazer Pedido")
    print("3 - Cancelar Pedido")
    print("0 - Sair")

def ver_menu():
    print("\n--- Menu de Pizzas ---")
    print("Pizzas:")
    print("1 - Margherita - R$ 20,00")
    print("2 - Pepperoni - R$ 25,00")
    print("3 - Quatro Queijos - R$ 30,00")
    print("4 - Calabresa - R$ 22,00")
    print("Tamanhos:")
    print("1 - Pequena")
    print("2 - Média")
    print("3 - Grande")
    print("Bebidas:")
    print("1 - Refrigerante - R$ 5,00")
    print("2 - Suco - R$ 7,00")
    print("3 - Água - R$ 3,00")

def fazer_pedido(pedidos):
    print("\n--- Fazer Pedido ---")
    pizzas = {1: "Margherita", 2: "Pepperoni", 3: "Quatro Queijos", 4: "Calabresa"}
    tamanhos = {"P": "Pequena", "M": "Média", "G": "Grande"}
    bebidas = {1: "Refrigerante", 2: "Suco", 3: "Água"}

    pizza = int(input("Escolha a pizza (1-4): "))
    tamanho = input("Escolha o tamanho (P/M/G): ").upper()
    bebida = int(input("Escolha a bebida (1-3): "))

    if pizza in pizzas and tamanho in tamanhos and bebida in bebidas:
        pedidos.append((pizza, tamanho, bebida))
        print("Pedido realizado com sucesso!")
    else:
        print("Pedido inválido.")
        return

    print(f"{bebidas[bebida]} adicionado ao pedido.")
    print(f"Pizza {pizzas[pizza]} tamanho {tamanhos[tamanho]} com {bebidas[bebida]} adicionada ao pedido.")

def cancelar_pedido(pedidos):
    if pedidos:
        pedidos.pop()
        print("Último pedido cancelado com sucesso!")
    else:
        print("Não há pedidos para cancelar.")

def main():
    pedidos = []
    while True:
        mostrar_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            ver_menu()
        elif opcao == 2:
            fazer_pedido(pedidos)
            print("Encerrando o sistema. Obrigado pelo seu pedido!")
            break 
        elif opcao == 3:
            cancelar_pedido(pedidos)
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()