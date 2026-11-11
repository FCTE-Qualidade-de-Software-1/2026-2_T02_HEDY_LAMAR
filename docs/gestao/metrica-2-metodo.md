# Métrica 2 - Distribuição de esforço por commits: método

**Categoria PSM/CID:** Recursos e Custos.

Esta página descreve o objetivo, a definição, o cálculo e a coleta. Os resultados e a análise estão em [Resultados e análise](metrica-2-resultados.md).

## 4.1. Objetivo

Observar como as contribuições registradas por meio de commits estão
distribuídas entre os integrantes da equipe durante o desenvolvimento do
projeto.

## 4.2. Definição

A métrica calcula a participação percentual de cada integrante no total
de commits considerados no período de acompanhamento.

Para evitar atribuições incorretas, a coleta identifica os autores dos
commits e associa seus registros às respectivas pessoas da equipe.
Quando há mais de uma identidade GitHub ou endereço de e-mail associado
à mesma pessoa, essas identidades são consolidadas.

| Classificação | Critério |
|---|---|
| Ideal | 12% a 28% |
| Aceitável | 8% a 12% ou 28% a 35% |
| Ruim | Fora dos critérios |

A classificação é aplicada à participação individual de cada integrante.

## 4.3. Forma de cálculo

**Participação por integrante = (quantidade de commits do integrante /
quantidade total de commits considerados) × 100**

O cálculo deverá considerar o mesmo intervalo de tempo e os mesmos
critérios de inclusão para todos os integrantes.

## 4.4. Fonte dos dados e coleta

-   **Fonte:** histórico de commits da branch `main` do repositório
    GitHub (referência `origin/main`). Os commits coletados estão em
    [`dados/psm/commits.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/dados/psm/commits.csv)
    e a relação entre identidades e integrantes está em
    [`dados/psm/integrantes.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/dados/psm/integrantes.csv).
-   **Coleta:** o script `scripts/coletar_commits.py` lista os commits
    com `git log`, identifica o autor de cada um e o associa a um
    integrante. O script `scripts/gerar_grafico_commits.py` calcula as
    participações e gera a Figura 2.
-   **Critérios de inclusão:** são considerados os commits da branch
    `main`, de 07/10/2026 (primeiro commit do repositório) até a data da
    coleta. Commits de *merge*, gerados pelo GitHub ao integrar Pull
    Requests e sem alteração autoral, são excluídos. Commits ainda não
    integrados à `main` não são contados.
-   **Tratamento:** cada commit é identificado por seu *hash*, o que
    evita contagem duplicada. As identidades da mesma pessoa foram
    consolidadas em `integrantes.csv`: João Vitor S. (e-mail pessoal e
    e-mail *noreply* do GitHub), Pablo R., Leonardo R. e Cauã C. O
    integrante João Victor M. não possui identidade com commits na
    `main` e é mantido na análise com 0 commits, para que sua
    participação apareça na distribuição.

Um commit pode representar uma alteração
pequena ou extensa; portanto, os percentuais devem ser interpretados
como distribuição das contribuições registradas no Git.
