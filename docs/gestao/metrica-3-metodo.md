# Métrica 3 - Tempo médio de resolução de Pull Requests: método

**Categoria PSM/CID:** Desempenho dos Processos.

Esta página descreve o objetivo, a definição, o cálculo e a coleta. Os resultados e a análise estão em [Resultados e análise](metrica-3-resultados.md).

## 5.1. Objetivo

Mensurar o tempo médio durante o qual um Pull Request permanece aberto,
desde sua criação até sua integração à branch `main`.

## 5.2. Definição

O tempo de resolução corresponde ao intervalo entre a data e hora de
criação de um Pull Request e a data e hora em que ele é integrado
(*merged*) à branch `main`.

Nesta métrica, considera-se como resolução a integração efetiva do Pull
Request à branch `main`, e não apenas seu fechamento. Pull Requests
fechados sem integração não devem ser contabilizados como integrados.

| Classificação | Critério |
|---|---|
| Ideal | Até 3 dias |
| Aceitável | Até 7 dias |
| Ruim | Mais que 7 dias |

A classificação é aplicada ao tempo médio de resolução do período. Os
tempos individuais de cada Pull Request são apresentados na [seção 5.6](metrica-3-resultados.md#56-visualizacao-dos-resultados)
para permitir a identificação de casos fora do critério.

## 5.3. Forma de cálculo

Para cada Pull Request integrado:

**Tempo de resolução = data e hora da integração − data e hora de
criação**

O tempo médio de resolução será calculado por:

**Tempo médio de resolução = soma dos tempos de resolução dos Pull
Requests integrados / quantidade de Pull Requests integrados**

O resultado será apresentado em dias.

O tempo de resolução é calculado em horas e convertido para dias
dividindo por 24, com o resultado expresso em dias decimais e
arredondado em duas casas.

Como indicador complementar, também é registrada a mediana dos tempos de
resolução, que reduz a influência de valores extremos. A mediana não é
classificada pela tabela de critérios.

## 5.4. Fonte dos dados e coleta

-   **Fonte:** registros de Pull Requests do GitHub, campos de data e
    hora de criação (`createdAt`) e de integração (`mergedAt`), em UTC.
    Os dados coletados estão no arquivo
    [`dados/psm/prs.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/dados/psm/prs.csv)
    do repositório.
-   **Coleta:** o script `scripts/coletar_prs.py` consulta o GitHub
    (por meio do GitHub CLI) e recupera, para cada Pull Request, a data
    e hora de criação e a data e hora de integração à branch `main`,
    registrando a data e hora da coleta no próprio arquivo. O arquivo
    guarda todos os Pull Requests como dado bruto; o cálculo e o gráfico
    usam somente os integrados. O script é executado automaticamente
    pelo workflow descrito no [procedimento de
    atualização](decisoes.md#62-procedimento-de-atualizacao), e o arquivo
    só é regravado quando os dados dos Pull Requests mudam; portanto, a
    data registrada é a da última atualização que alterou os dados.
-   **Critério de inclusão:** considerar Pull Requests efetivamente
    integrados à branch `main` dentro do período definido para a
    análise. O período analisado vai de 19/10/2026 (criação do primeiro
    Pull Request) até a data da coleta, registrada na [seção 5.5](metrica-3-resultados.md#55-resultado).
-   **Tratamento:** Pull Requests fechados sem integração são
    registrados separadamente, mas não incluídos no cálculo do tempo
    médio de integração.
-   **Pull Requests abertos:** Pull Requests ainda abertos na data da
    coleta não são considerados nesta métrica, pois ainda não possuem
    data de integração.
