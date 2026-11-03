sabores_pizza = ["Mussarela", "Calabresa", "Pepperoni", "Quatro queijos", "Frango com Catupiry"]
print("Faça seu pedido (digite 'sair' para encerrar): ") 
pizza = "" # Aqui ficará armazenado a pizza do cliente

# Enquanto o sair não for digitado, o while continuará sendo executado.
while pizza.capitalize() != "Sair":
    pizza = input("Escolha um sabor: ").capitalize()  
    if pizza in sabores_pizza:
        print(f'{pizza} foi adicionado ao seu pedido.')
    elif pizza.capitalize() == "Sair":
        print("Pedido encerrado!")
    else:
        print("Esse sabor não está no cardápio. Escolha outro: ")




# sabores_pizza = ["Mussarela", "Calabresa", "Pepperoni", "Quatro queijos", "Frango com Catupiry"]
# print("Faça seu pedido (digite 'sair' para encerrar): ") 
# pizza = "" # Aqui ficará armazenado a pizza do cliente

# # Enquanto o sair não for digitado, o while continuará sendo executado.
# while pizza.lower() != "sair":
#     pizza = input("Escolha um sabor: ")
#     if pizza in sabores_pizza:
#         print(f'{pizza} foi adicionado ao seu pedido.')
#     elif pizza.lower() == "sair":
#         print("Pedido encerrado!")
#     else:
#         print("Esse sabor não está no cardápio. Escolha outro: ")
        


