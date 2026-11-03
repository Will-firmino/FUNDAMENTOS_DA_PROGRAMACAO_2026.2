# Estruturas condicionais permitem que o programa execute blocos de código diferentes dependendo de uma condição. A condição é sempre avaliada como True(Verdadeiro) False(Falso).

# Se o usuário tiver a idade maior que 18, ele poderá entrar.
# if -> Verifica uma condição e executa o bloco de código associado se a condição for verdadeira.
idade_usuario = 21 # Hardcode
# if idade_usuario > 18:
#     print("O usuário pode acessar o local.")

# else -> Permite executar o bloco de código se a condição if for falsa.
# if idade_usuario > 18:
#     print(" 🎟️ O usuário pode acessar o local.")
# else:
#     print(" 🔞 Entrada proibida!")

# elif -> Abreviação (else if) é usado para testas várias condições. Ele só será exibido se todas as condições anteriores forem falsas.
nota = int(input("Digite a nota do aluno: "))
# nota maior ou igual a 90, "Aprovado com nota excelente."
# nota for maior ou igual a 70, "Aprovado."
# qualquer outra nota, será exibido "Reprovado."

if nota >= 90:
    print("🎆 Aprovado com nota excelente.")
elif nota >= 70:
    print("✅ Aprovado.")
else:
    print("❌ Reprovado.")





