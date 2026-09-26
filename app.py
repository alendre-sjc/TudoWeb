# ===============================================================
# COMO ESTE PROGRAMA FUNCIONA — explicado na ordem em que executa
# ===============================================================
# Este arquivo é comentado "Ato" por "Ato", seguindo a ORDEM DE
# EXECUÇÃO real do programa. O Python lê e executa este script de
# cima para baixo, mas aqui existe uma REPETIÇÃO: o Ato 2 (coleta
# de dados de um entrevistado) se repete várias vezes, controlado
# por uma estrutura de repetição FOR.
#
# Resumo da peça inteira:
#   Ato 0 -> Exibe o cabeçalho da pesquisa
#   Ato 1 -> Inicializa os contadores de respostas (antes do laço)
#   Ato 2 -> Repete a coleta de dados para cada entrevistado (FOR)
#     Ato 2.1 -> Pergunta nome e idade do entrevistado
#     Ato 2.2 -> Valida a idade digitada (WHILE + OR)
#     Ato 2.3 -> Pergunta e valida a opinião (WHILE + AND)
#     Ato 2.4 -> Classifica a opinião e atualiza o contador (IF/ELIF/ELSE)
#   Ato 3 -> Exibe o resultado final da pesquisa, após o laço terminar
# ===============================================================

# ---------------------------------------------------------------
# Ato 0: Exibição do cabeçalho
# ---------------------------------------------------------------
# print() mostra um texto na tela. Aqui é só a "moldura" visual
# do programa, para o entrevistador saber que está usando o
# sistema de pesquisa de satisfação da TudoWeb.
print("=======================================================")
print("   📋 TUDOWEB - PESQUISA DE SATISFAÇÃO NO ATENDIMENTO 📋")
print("=======================================================")

# ---------------------------------------------------------------
# Ato 1: Inicialização dos contadores e da quantidade de entrevistas
# ---------------------------------------------------------------
# Esses contadores começam em zero e serão incrementados dentro do
# laço de repetição, conforme cada entrevistado responder.
# TOTAL_ENTREVISTADOS define quantas vezes o Ato 2 vai se repetir.
# Para os testes da atividade, basta trocar o valor para 10.
TOTAL_ENTREVISTADOS = 10

qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

# ---------------------------------------------------------------
# Ato 2: Repetição da coleta de dados (estrutura FOR)
# ---------------------------------------------------------------
# A estrutura FOR é usada aqui porque já sabemos, antecipadamente,
# exatamente quantas vezes a coleta deve se repetir
# (TOTAL_ENTREVISTADOS). range(1, TOTAL_ENTREVISTADOS + 1) gera os
# números de 1 até o total definido, e a variável "i" controla em
# qual entrevistado o programa está a cada volta do laço.
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")

    # Ato 2.1: Solicitação do nome e da idade do entrevistado
    # input() pausa o programa e espera o entrevistador digitar.
    # float()/int() convertem o texto digitado em número, para que
    # seja possível fazer comparações (<, >, etc.) mais adiante.
    nome = input("Digite o nome do entrevistado: ")
    idade = int(input("Digite a idade do entrevistado: "))

    # Ato 2.2: Validação da idade (estrutura WHILE + operador OR)
    # A estrutura WHILE é usada aqui porque não sabemos, de
    # antemão, quantas vezes o entrevistador vai errar a digitação.
    # A repetição continua enquanto a condição for verdadeira, e só
    # para quando uma idade válida é informada. O operador lógico
    # OR faz o laço repetir se QUALQUER uma das duas condições de
    # erro for verdadeira (idade negativa OU maior que 120).
    while idade < 0 or idade > 120:
        print("Idade inválida! Digite um valor entre 0 e 120.")
        idade = int(input("Digite a idade do entrevistado: "))

    # Ato 2.3: Solicitação e validação da opinião (WHILE + operador AND)
    opiniao = int(input("Avalie o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): "))

    # Aqui o operador lógico AND faz o laço continuar repetindo
    # somente enquanto TODAS as comparações forem verdadeiras, ou
    # seja, enquanto a opção digitada for diferente de 1 E diferente
    # de 2 E diferente de 3 (nenhuma opção válida foi digitada).
    while opiniao != 1 and opiniao != 2 and opiniao != 3:
        print("Opção inválida! Digite 1, 2 ou 3.")
        opiniao = int(input("Avalie o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): "))

    # Ato 2.4: Classificação da opinião (estrutura IF/ELIF/ELSE)
    # A estrutura if/elif/else testa as condições NA ORDEM em que
    # aparecem e executa apenas o primeiro bloco verdadeiro. Como a
    # validação do Ato 2.3 já garantiu que opiniao só pode ser 1, 2
    # ou 3, o "else" final cobre com segurança o valor 3 (RUIM).
    if opiniao == 1:
        avaliacao = "EXCELENTE"
        qtd_excelente += 1
    elif opiniao == 2:
        avaliacao = "BOM"
        qtd_bom += 1
    else:
        avaliacao = "RUIM"
        qtd_ruim += 1

    print(f"Registrado: {nome}, {idade} anos, avaliação: {avaliacao}")

# ---------------------------------------------------------------
# Ato 3: Exibição do resultado final da pesquisa
# ---------------------------------------------------------------
# Este bloco só é executado DEPOIS que o FOR do Ato 2 terminar
# todas as suas voltas (ou seja, depois que os 50 entrevistados
# já tiverem sido registrados). Por fim, o programa mostra o
# total de respostas em cada categoria, usando os contadores que
# foram atualizados dentro do laço.
print("\n===== RESULTADO FINAL DA PESQUISA =====")
print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostas BOM: {qtd_bom}")
print(f"Quantidade de respostas RUIM: {qtd_ruim}")
print("========================================")

# ===============================================================
# Para fixar:
#   - Por que a estrutura FOR foi escolhida para repetir a coleta
#     dos 50 entrevistados, e não a estrutura WHILE?
#   - Por que as validações de idade e opinião (Atos 2.2 e 2.3)
#     usam WHILE em vez de FOR?
#   - O que aconteceria se a validação da opinião (Ato 2.3) usasse
#     o operador OR no lugar do AND? O laço se comportaria da
#     mesma forma?
#   - Os contadores (qtd_excelente, qtd_bom, qtd_ruim) são
#     definidos ANTES do laço FOR. O que aconteceria se eles fossem
#     definidos DENTRO do laço, a cada volta?
# ===============================================================
