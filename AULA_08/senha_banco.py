"""
Crie um sistema que peça o usuário para digitar uma senha para acessar sua conta bancária. Ele tem  **apenas 3 tentativas** para acertar a senha. 
Se ele errar as 3 tentativas, o sistema bloqueia a conta.
- A senha correta 1234;
- O usuário tem 3 tentativas input();
- Se errar 3 vezes. conta bloqueada.
"""
# Variáveis no escopo global
SENHA_CORRETA = "1234" # Constante, boa prática em python.
tentativas = 3 # Uma variável contadora, pode ser i ou j.

while tentativas > 0:
    senha = input("Digite a sua senha: ") # variável no escopo local
    if senha == SENHA_CORRETA:
        print("🔓 Acesso Permitido! ")   
        break # Comando que finaliza o loop 
    else:
        tentativas -= 1  # tentativas = tentativas -1 
        print(f'Senha incorreta. Tentativas restantes: {tentativas}')   

    if tentativas == 0:
        print("❌ Conta bloqueada.")
