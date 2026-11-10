def calcular_preco_pizza(sabor, tamanho, borda_recheada=False):
  "Calcula o preço final de uma pizza com opções."
  tabela = {
    "P": 25.0,
    "M": 35.0,
    "G": 45.0
  }
  
  preco = tabela[tamanho]
  if borda_recheada:
    preco += 8.0
  print(f"""A pizza é de {sabor} 
        o tamanho é {tamanho} 
        a borda é recheada? {borda_recheada}
        Preço total: R${preco}
        """)  
    
calcular_preco_pizza("Frango","G")


#   return preco, sabor
  
