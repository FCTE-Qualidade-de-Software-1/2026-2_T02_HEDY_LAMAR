# Plano de Medição e Acompanhamento (PSM/CID)

## 1. Objetivo

Este documento reúne as métricas utilizadas para acompanhar o
desenvolvimento do projeto, com foco no cumprimento dos prazos, na
distribuição das contribuições registradas no repositório e no tempo
necessário para integrar Pull Requests à branch `main`.

A coleta e a consolidação dos dados usam arquivos versionados em
`dados/psm/` e scripts em `scripts/`, que consultam o histórico e os
registros do GitHub. Os resultados são atualizados a cada coleta,
mantendo a rastreabilidade entre os indicadores apresentados e os dados
de origem. As medições, suas interpretações e as decisões de gestão
decorrentes estão registradas nas páginas de cada métrica e no
[registro de decisões](decisoes.md).

## 2. Escopo e coleta dos dados

As métricas deste documento são:

-   **[Antecedência de conclusão](metrica-1-metodo.md):** verifica se as
    entregas foram concluídas antes do prazo combinado.
-   **[Distribuição de esforço por commits](metrica-2-metodo.md):**
    apresenta como os commits estão distribuídos entre os integrantes da
    equipe.
-   **[Tempo médio de resolução de Pull Requests](metrica-3-metodo.md):**
    mede quanto tempo os Pull Requests permanecem abertos até serem
    integrados à branch `main`.

Cada métrica está associada a uma das categorias do modelo PSM/CID
exigidas para o acompanhamento do projeto:

| Categoria PSM/CID | Métrica | Justificativa |
|---|---|---|
| Calendário e Progresso | Métrica 1: Antecedência de conclusão | Compara a data combinada com a data efetiva de conclusão de cada entrega. |
| Recursos e Custos | Métrica 2: Distribuição de esforço por commits | Os commits são o indicador disponível do esforço da equipe, que é o principal recurso do projeto. |
| Desempenho dos Processos | Métrica 3: Tempo médio de resolução de Pull Requests | Mede a rapidez com que o fluxo de revisão e integração do repositório conclui as alterações. |

Os dados de cada métrica ficam em `dados/psm/` e os gráficos são
gerados por scripts em `scripts/` a partir desses arquivos. A coleta dos
Pull Requests e dos commits e a geração dos gráficos são executadas
automaticamente por um workflow do GitHub Actions, descrito no
[procedimento de atualização](decisoes.md#62-procedimento-de-atualizacao).
Os resultados numéricos e os gráficos de cada métrica estão nas páginas
de resultados, listadas abaixo.

!!! note "Nota sobre interpretação"
    A quantidade de commits é utilizada como um indicador indireto da
    distribuição das contribuições registradas. Embora ela seja uma boa
    aproximação do esforço geral dos integrantes, ela não representa,
    isoladamente, a complexidade ou a qualidade do trabalho de cada
    integrante e não considera o trabalho no LaTeX.

### 2.1. Resumo dos resultados

Quadro 1: Resumo dos resultados por métrica (dados de 11/11/2026).

| Métrica | Categoria PSM/CID | Resultado | Classificação | Páginas |
|---|---|---|---|---|
| 1. Antecedência de conclusão | Calendário e Progresso | Entrega 1: 0 dia de antecedência (Entrega 2 pendente) | **Aceitável** | [Método](metrica-1-metodo.md) · [Resultados](metrica-1-resultados.md) |
| 2. Distribuição de commits | Recursos e Custos | 40,0% / 40,0% / 15,0% / 5,0% / 0,0% dos 40 commits, por integrante | 1 integrante **Ideal**; 4 **Ruim** | [Método](metrica-2-metodo.md) · [Resultados](metrica-2-resultados.md) |
| 3. Tempo médio de resolução de PRs | Desempenho dos Processos | 1,14 dia (média) e 0,80 dia (mediana), 6 Pull Requests | **Ideal** | [Método](metrica-3-metodo.md) · [Resultados](metrica-3-resultados.md) |

### 2.2. Como navegar

Cada métrica tem duas páginas: **Método**, com objetivo, definição,
cálculo e coleta; e **Resultados e análise**, com o resultado, o gráfico,
a interpretação e a decisão decorrente. As decisões de todas as métricas
estão reunidas em [Decisões de gestão](decisoes.md), junto com o
procedimento de atualização, as considerações finais e o histórico de
versões.
