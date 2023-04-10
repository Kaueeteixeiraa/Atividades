lista_de_compras = []

def adicionar_item():
    item = input("Digite o nome do item que vai adicionar: ")
    lista_de_compras.append(item)
    print(f"O item '{item}' foi adicionado à lista.")

def remover_item():
    item = input("Digite o nome do item que vai remover: ")
    try:
        lista_de_compras.remove(item)
        print(f"O item '{item}' foi removido da lista.")
    except ValueError:
        print(f"O item '{item}' não está na lista.")

def listar_itens():
    print("Itens na lista de compras:")
    for item in lista_de_compras:
        print(item)

while True:
    print("\n=== Lista de Compras ===")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        remover_item()
    elif opcao == "3":
        listar_itens()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
