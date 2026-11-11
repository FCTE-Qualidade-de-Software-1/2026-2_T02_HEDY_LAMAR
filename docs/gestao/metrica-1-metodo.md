# Métrica 1 - Antecedência de conclusão: método

**Categoria PSM/CID:** Calendário e Progresso.

Esta página descreve o objetivo, a definição, o cálculo e a coleta. Os resultados e a análise estão em [Resultados e análise](metrica-1-resultados.md).

## 3.1. Objetivo

Avaliar se as entregas do projeto foram concluídas antes dos prazos
previamente combinados pela equipe.

## 3.2. Definição

A métrica considera a diferença entre a data combinada para a conclusão
de uma entrega e a data em que ela foi efetivamente concluída.

Um resultado positivo indica que a entrega foi concluída antes do prazo;
um resultado igual a zero indica conclusão no prazo; e um resultado
negativo indica atraso.

| Classificação | Critério (antecedência em dias) |
|---|---|
| Ideal | 2 dias ou mais |
| Aceitável | De 0 (no prazo) até menos de 2 dias |
| Ruim | Menor que 0 (entrega com atraso) |

A antecedência é medida em dias corridos entre datas de calendário, e as
datas são consideradas no horário de Brasília (UTC−3), fuso em que os
prazos da disciplina são definidos.

## 3.3. Forma de cálculo

Para cada entrega:

**Antecedência (em dias) = data do prazo combinado − data de conclusão**

Também é calculada a proporção de entregas concluídas
antecipadamente:

**Percentual de entregas antecipadas = (quantidade de entregas
concluídas antes do prazo / quantidade total de entregas avaliadas) ×
100**

## 3.4. Fonte dos dados e coleta

-   **Fonte do prazo:** especificação do trabalho final da disciplina
    (Entrega 1: 26/10/2026) e cronograma da disciplina (Entrega 2,
    entrega final do trabalho: 22/11/2026).
-   **Fonte da conclusão:** data e hora de publicação da Release da
    entrega no GitHub (Release v1.0.0, "Entrega 1"), que é o produto de
    trabalho exigido para cada entrega.
-   **Registro:** os prazos e as conclusões estão em
    [`dados/psm/entregas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/dados/psm/entregas.csv).
    O script `scripts/gerar_grafico_entregas.py` calcula a antecedência
    e gera a Figura 1. A cada nova entrega, basta incluir o prazo e a
    data de publicação da Release no arquivo, que é preenchido
    manualmente. O gráfico é regenerado na próxima execução do workflow
    descrito no [procedimento de
    atualização](decisoes.md#62-procedimento-de-atualizacao).
