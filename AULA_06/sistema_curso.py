# Entrada de dados
idade = int(input("Idade: "))
nota = float(input("Nota: "))
frequencia = float(input("Frequência (%): "))

# Análise da matricula/ exibir resultado na tela:
if idade < 18:
    print("Matrícula negada. Aluno menor de idade.")
elif nota >= 9:
    print("Matrícula aprovada automaticamente.")
elif idade >= 18 and nota >= 6 and frequencia >= 75:
    print("Matrícula aprovada.")
else:
    print("Matrícula negada.")




# Verifico se a idade é menor que 18, negado.
# Verifico se a nota é maior ou igual a 9,aprovo
# idade é maior que 18, nota maior ou igual a 6, e freq maior ou igual a 75
# Se não, negado.
