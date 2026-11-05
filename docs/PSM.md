# Plano de Medição e Acompanhamento (PSM/CID)

## 1. Objetivo

Este documento reúne as métricas utilizadas para acompanhar o
desenvolvimento do projeto, com foco no cumprimento dos prazos, na
distribuição das contribuições registradas no repositório e no tempo
necessário para integrar Pull Requests à branch `main`.

A coleta e a consolidação dos dados serão realizadas por meio de
automatizações que consultam o histórico e os registros do GitHub. Os
resultados poderão ser atualizados periodicamente, mantendo a
rastreabilidade entre os indicadores apresentados e os dados de origem.

## 2. Escopo e coleta dos dados

As métricas deste documento são:

-   **Antecedência de conclusão:** verifica se as entregas foram
    concluídas antes do prazo combinado.
-   **Distribuição de esforço por commits:** apresenta como os commits
    estão distribuídos entre os integrantes da equipe.
-   **Tempo médio de resolução de Pull Requests:** mede quanto tempo os
    Pull Requests permanecem abertos até serem integrados à branch
    `main`.

A coleta será automatizada a partir dos dados disponíveis no repositório
GitHub. Os resultados numéricos e os gráficos serão inseridos após a
execução da rotina de coleta.

> **Nota sobre interpretação:** a quantidade de commits é utilizada como
> um indicador indireto da distribuição das contribuições registradas.
> Embora ela seja uma boa aproximação do esforço geral dos integrantes,
> ela não representa, isoladamente, a complexidade ou a
> qualidade do trabalho de cada integrante e não considera o trabalho no LaTeX.

------------------------------------------------------------------------

## 3. Métrica 1 --- Antecedência de conclusão

### 3.1. Objetivo

Avaliar se as entregas do projeto foram concluídas antes dos prazos
previamente combinados pela equipe.

### 3.2. Definição

A métrica considera a diferença entre a data combinada para a conclusão
de uma entrega e a data em que ela foi efetivamente concluída.

Um resultado positivo indica que a entrega foi concluída antes do prazo;
um resultado igual a zero indica conclusão no prazo; e um resultado
negativo indica atraso.

| Classificação | Critério |
|---|---|
| Ideal | 2 dias ou mais |
| Aceitável | Até 1 dia |
| Ruim | Menor que 0 |

### 3.3. Forma de cálculo

Para cada entrega:

**Antecedência (em dias) = data do prazo combinado − data de conclusão**

No futuro, também poderá ser calculada a proporção de entregas concluídas
antecipadamente:

**Percentual de entregas antecipadas = (quantidade de entregas
concluídas antes do prazo / quantidade total de entregas avaliadas) ×
100**

### 3.4. Fonte dos dados e coleta

*INSERIR AQUI FONTE APÓS AUTOMATIZAÇÂO, CASO ESSA PARTE NÂO SEJA AUTOMATIZADA, PODEMOS CITAR A ENTREGA NO APRENDER OU SO APAGAR MESMO*

### 3.5. Resultado

-   Quantidade de entregas avaliadas: @
-   Quantidade de entregas concluídas antes do prazo: @
-   Quantidade de entregas concluídas no prazo: @
-   Quantidade de entregas concluídas após o prazo: @
-   Percentual de entregas antecipadas: @
-   Antecedência média das entregas concluídas antes do prazo: @ dias

### 3.6. Visualização dos resultados

**\[ESPAÇO RESERVADO PARA GRÁFICO\]**

*Não sei se vai ter grafico considerando que ate agora foi so uma entrega, mas aqui é pra inserir 
gráfico comparando, para cada entrega, a data combinada e a
data efetiva de conclusão. Se pertinente, incluir também a distribuição
das entregas antecipadas, concluídas no prazo e atrasadas.*

### 3.7. Análise

Até agora a única entrega foi realizada no mesmo dia do prazo, tendo um resultado aceitável.
Deveríamos tentar fazer a próxima entrega com dias de sobra.

*o slide ta falando "Duas entregas seguidas fora do verde: adiantar o prazo interno em 2 dias e redistribuir tarefas."
acabei deixando isso passar mas n entendi, é todas as entregas do grupo? achei que era so a entrega 1 e 2 do projeto final*

------------------------------------------------------------------------

## 4. Métrica 2 --- Distribuição de esforço por commits

### 4.1. Objetivo

Observar como as contribuições registradas por meio de commits estão
distribuídas entre os integrantes da equipe durante o desenvolvimento do
projeto.

### 4.2. Definição

A métrica calcula a participação percentual de cada integrante no total
de commits considerados no período de acompanhamento.

Para evitar atribuições incorretas, a automatização deverá identificar
os autores dos commits e associar seus registros às respectivas pessoas
da equipe. Quando houver mais de uma identidade GitHub ou endereço de
e-mail associado à mesma pessoa, essas identidades deverão ser
consolidadas.

| Classificação | Critério |
|---|---|
| Ideal | 12% a 28% |
| Aceitável | 8% a 12% ou 28% a 35% |
| Ruim | Fora dos critérios |

### 4.3. Forma de cálculo

**Participação por integrante = (quantidade de commits do integrante /
quantidade total de commits considerados) × 100**

O cálculo deverá considerar o mesmo intervalo de tempo e os mesmos
critérios de inclusão para todos os integrantes.

### 4.4. Fonte dos dados e coleta

-   **Fonte:** histórico de commits do repositório GitHub.
-   **Coleta:** uma rotina automatizada deverá consultar os commits do
    período, identificar seus autores e contabilizar as contribuições
    por integrante.
-   **Tratamento:** commits duplicados ou registros associados a
    identidades diferentes da mesma pessoa deverão ser tratados para
    evitar contagem duplicada.

Um commit pode representar uma alteração
pequena ou extensa; portanto, os percentuais devem ser interpretados
como distribuição das contribuições registradas no Git.

### 4.5. Resultado

-   Período analisado: @
-   Total de commits considerados: @
-   Integrante 1: @ commits --- @%
-   Integrante 2: @ commits --- @%
-   Integrante 3: @ commits --- @%
-   \[Adicionar ou remover linhas conforme a composição da equipe.\]

### 4.6. Visualização dos resultados

**\[ESPAÇO RESERVADO PARA GRÁFICO\]**

*Inserir gráfico de barras ou de setores mostrando a participação
percentual de cada integrante no total de commits.*

### 4.7. Análise

\[Inserir análise da distribuição observada. Considerar que diferenças
na quantidade de commits não significam necessariamente diferenças
equivalentes no esforço real, pois as tarefas podem variar em tamanho e
complexidade.\]

------------------------------------------------------------------------

## 5. Métrica 3 --- Tempo médio de resolução de Pull Requests

### 5.1. Objetivo

Mensurar o tempo médio durante o qual um Pull Request permanece aberto,
desde sua criação até sua integração à branch `main`.

### 5.2. Definição

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

### 5.3. Forma de cálculo

Para cada Pull Request integrado:

**Tempo de resolução = data e hora da integração − data e hora de
criação**

O tempo médio de resolução será calculado por:

**Tempo médio de resolução = soma dos tempos de resolução dos Pull
Requests integrados / quantidade de Pull Requests integrados**

O resultado será apresentado em dias.

### 5.4. Fonte dos dados e coleta

-   **Fonte:** registros de Pull Requests do GitHub.
-   **Coleta:** uma rotina automatizada deverá recuperar, para cada Pull
    Request, a data e hora de criação e a data e hora de integração à
    branch `main`.
-   **Critério de inclusão:** considerar Pull Requests efetivamente
    integrados à branch `main` dentro do período definido para a
    análise.
-   **Tratamento:** Pull Requests fechados sem integração deverão ser
    registrados separadamente, mas não incluídos no cálculo do tempo
    médio de integração.
-   **Atualização:** a automatização deverá atualizar os dados quando
    novos Pull Requests forem integrados.

### 5.5. Resultado

-   Período analisado: @
-   Quantidade de Pull Requests integrados considerados: @
-   Tempo médio de resolução: @
-   Menor tempo de resolução observado: @
-   Maior tempo de resolução observado: @

### 5.6. Visualização dos resultados

**\[ESPAÇO RESERVADO PARA GRÁFICO\]**

*Inserir gráfico mostrando o tempo de resolução de cada Pull Request
integrado e, se útil, uma linha de referência para o tempo médio.*

### 5.7. Evidências da coleta

*PREENCHER*

### 5.8. Análise

*PREENCHER MAS DO QUE EU VI ERA 0,8*

------------------------------------------------------------------------

## 6. Considerações finais

As três métricas permitem acompanhar dimensões distintas do
desenvolvimento: cumprimento dos prazos combinados, distribuição das
contribuições registradas no Git e tempo de integração das alterações à
branch `main`.

Os resultados deverão ser interpretados considerando o período de
coleta, os critérios de inclusão e as limitações de cada indicador. Em
particular, a quantidade de commits não deve ser tratada como medida
direta de esforço, e o tempo de integração de Pull Requests não deve ser
interpretado isoladamente como medida de produtividade ou qualidade.

## 7. Histórico de atualização  

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1.0 | Criação da documentação das métricas PSM/CID. | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 22/10/2026 |   |  |
