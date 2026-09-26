# 📋 Pesquisa de Satisfação – Atendimento ao Cliente (TudoWeb)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge)
![Atendimento](https://img.shields.io/badge/Tema-Satisfação%20do%20Cliente%20📋-2E8B57?style=for-the-badge)

## 🎯 Objetivo

Programa desenvolvido para a empresa de marketing **TudoWeb**, com o objetivo de realizar uma **pesquisa de opinião** com seus clientes e medir o grau de satisfação no atendimento prestado. O sistema solicita o nome, a idade e a opinião de cada entrevistado e, ao final da coleta, exibe um **resumo com a quantidade de respostas** em cada categoria de avaliação. 📊

## 📏 Regras de negócio

| Opção digitada | Avaliação | Contador atualizado |
|---|---|---|
| 1 | 🌟 EXCELENTE | `qtd_excelente` |
| 2 | 👍 BOM | `qtd_bom` |
| 3 | 👎 RUIM | `qtd_ruim` |

| Validação | Condição usada | Operador lógico |
|---|---|---|
| Idade inválida | `idade < 0 or idade > 120` | OR |
| Opinião inválida | `opiniao != 1 and opiniao != 2 and opiniao != 3` | AND |

A pesquisa é realizada com **50 entrevistados** por padrão (`TOTAL_ENTREVISTADOS`), sendo possível reduzir esse número para validar o funcionamento do programa em testes.

## 🐍 Tecnologias e conceitos utilizados

- **Python 3** (nenhuma biblioteca externa é necessária).
- Conceitos aplicados: `input()`, conversão de tipos com `int()`, estrutura de repetição `for` (quantidade definida de entrevistados), estrutura de repetição `while` com operadores lógicos `and`/`or` (validação de entradas), estrutura condicional `if / elif / else` e `print()`.
- Código comentado no modelo **"Ato por Ato"**, explicando o programa na ordem real em que ele é executado (do Ato 0 ao Ato 3), incluindo a repetição do Ato 2 para cada entrevistado.

## ▶️ Como executar o programa

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/pesquisa-satisfacao-tudoweb.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd pesquisa-satisfacao-tudoweb
   ```
3. Execute o script com Python 3:
   ```bash
   python3 app.py
   ```
4. Informe o nome, a idade e a opinião de cada entrevistado quando solicitado, e veja o resumo final da pesquisa. ✅

> 💡 Para testar o programa sem precisar digitar 50 respostas manualmente, abra o `app.py` e altere temporariamente `TOTAL_ENTREVISTADOS = 50` para `TOTAL_ENTREVISTADOS = 10`.

## 📁 Estrutura do projeto

```
pesquisa-satisfacao-tudoweb/
├── app.py        # Script principal com a lógica da pesquisa
└── README.md     # Documentação do projeto
```

## 🚀 Melhorias futuras

- Permitir salvar as respostas de cada entrevistado em um arquivo, para consulta posterior.
- Calcular também o percentual de cada categoria de avaliação em relação ao total de entrevistados.
- Adicionar uma opção para o entrevistador encerrar a pesquisa antes de atingir o total definido.

## 👨‍💻 Autor

Projeto desenvolvido como atividade prática de lógica de programação em Python, com foco em estruturas de repetição e satisfação do cliente. 💙

---

⭐ Se este projeto foi útil, deixe uma estrela no repositório!
