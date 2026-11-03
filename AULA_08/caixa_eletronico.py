"""
Crie um programa que simule um caixa eletrônico. O usuário pode sacar valores até que o saldo disponível acabe ou até ele digitar 'sair'.
- Comece com saldo inicial de R$500.
- Peça ao usuário digitar um valor para saque.
- Se o valor for maior que o saldo, avise que não há saldo suficiente.
- Se o usuário digitar 'sair', encerre o programa.
"""
saldo = 500

while saldo > 0: #Irá continuar até ser False(acabar o saldo) ou digitar 'sair'
    print(f' \n 💰Saldo disponível: R${saldo:.2f}') #\n quebra a linha
    saque = input("Digite o valor para sacar ou 'sair' para encerrar: ")

    if saque.lower() == "sair": # o método lower() transforma a string em minúscula.
        print("🏧 Operação encerrada.")
        break

    saque = float(saque)
    if saque > saldo:
        print("❌ Saldo insuficiente!")
    else:
        # saldo = saldo - saque
        saldo -= saque 
        print(f"Saque de R${saque:.2f} realizado com sucesso!")