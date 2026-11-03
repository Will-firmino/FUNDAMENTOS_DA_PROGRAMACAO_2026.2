# Perguntas a serem feitas ao cliente
# pizza pequena = 19,90
# pizza média = 29,90
# pizza grande = 39,90

FRETE = 2
dia_semana = "sabado"

print(f"""
        ==================================
        Seja bem-vindo a pizzaria Sabores
        ==================================
    """)
nome_cliente = input(f"""
           💁 Digite o seu nome:
        """)
pizza_sabor = input(f"""
        🍕 Escolha uma das opções abaixo: 
            1- frango com requeijão
            2- calabresa
            3- mussarela
            4- banana com chocolate
        """)
pizza_tamanho = input(f"""
        🔢 Escolha o tamanho da pizza:
            1- pequena
            2- média
            3- grande
""")
forma_entrega = input(f"""
        🏍️ Escolha a forma de entrega:
            1- consumo no local
            2- entrega na residência

""")

# Estrutura condicional para promoção:
# Comprando qualquer pizza e qualquer tamanho no sábado, o refri é gratuito
# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.
# Comprando uma pizza de calabresa tamanho médio, em qualquer dia, o frete é gratuito.
if dia_semana == "sabado":
    print(f" 🍕 Pedido aceito com sucesso!")
    print(f" 🥤 O refri hoje é por conta da casa!")
elif dia_semana == "domingo":
    print(f" 🍕 Pedido aceito com sucesso!")
    print(f" 🏍️🥤 O frete e o refri hoje é por conta da casa!")
elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
    print(f" 🍕 Pedido aceito com sucesso!")
    print(f" 🏍️ O frete hoje é por conta da casa!")


# print(f"""
#         ==================================
#               🧾 Resumo do pedido
#             Nome do cliente: {nome_cliente}
#             Sabor da pizza: {pizza_sabor}
#             Tamanho da pizza: {pizza_tamanho}
#             Forma de entrega: {forma_entrega}
#         ==================================
# """)
