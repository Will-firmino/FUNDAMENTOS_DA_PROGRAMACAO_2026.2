# Comandos principais do Python
print() -> Exibe informações no terminal.
input() -> Exibe e/ou recebe informação.
f""" """ ->  f-string. Concatena variáveis e textos.

# Cases utilizados nas linguagens de programacão
NOME DO USUARIO
1. cammelCase. Ex: nomeDoUsuario 
2. PascalCase. Ex: NomeDoUsuario
3. ``snake_case. Ex: nome_do_usuario``
4. kebab-case. Ex: nome-do-usuario

# Python não tem constante, mas tem boa prática.
CPF = 123456 # Constante, boa prática.

# Operadores matemáticos
+ -> Adição
- -> Subtração
* -> multiplicação
/ -> divisão
// -> divisão inteira
% -> resto da divisão (módulo)
** -> exponenciação (potência)

# Operadores lógicos
and -> Retorna True se ambos forem verdadeiros
or -> Retorna True se um ou ambos forem verdadeiros
not -> Inverte o valor lógico

# Operadores de comparação
== -> igual a
!= -> diferente de
< -> menor que
> -> maior que
<= -> menor ou igual a 
>= -> maior ou igual a 

# Escopo global x Escopo local
> global:
- Pode ser acessada por qualquer parte do sistema. No entanto, em Python ela escapa. O valor da variável global é modificado em alguma estrutura e o valor fica sendo o último usado nessa estrutura.
> local: 
- Ela é criada dentro de uma estrutura. Ela vale somente naquela estrutura e se em um outro nível ela ser utilizada, ela escapa porém pode ser reutilizada.


# Funções [def]
-> é um objeto guardado numva variável, que contém um bloco de código ainda não executado.
Quando você a chama, o python cria um espaço de nomes novos e temporários.
[def] -> Palavra-chave que inicia a declaração da função.
[nome_funcao] -> Identificador - utilizando o padrão ``snake_case``.
[parâmetros] -> Dados de entrada entre parênteses. 
[argumentos] -> Valores que ocupam o lugar dos parâmetros.
[docstring] -> Documentação entre aspas duplas.
[corpo] -> Bloco identado contendo a lógica da função.
[return] -> Valor retornado, se a def não tiver o return, o padrão é none.





# Exercício - Sistema de Matrícula em curso.
> Contexto: 
- Uma escola está analisando se um aluno pode ser matricular em um curso profissionalizante. Para isso, o sistema precisa verificar algumas informações antes de aprovar ou negar a matrícula.
O programa deverá utilizar estruturas condicionais para tomar decisões.

> Objetivo do exercício:
- Criar um programa em python que:
1. Receba a idade do aluno;
2. Receba a nota da prova;
3. Receba a frequência escolar (em %);
4. Analise se a matrícula pode ser aprovada;
4. Exiba o resultado na tela.

> Regras do sistema:
- A matrícula será aprovada se:
1. a `idade` for maior ou igual a 18 anos;
2. a `nota` for maior ou igual a 6;
3. a `frequência` for maior ou igual a 75%;
> Regras especiais:
1. Se a `nota` for maior ou igual a 9 -> a matrícula será aprovada automaticamente.
2. Se a `idade` for menor que 18 anos -> a matrícula será negada automaticamente.