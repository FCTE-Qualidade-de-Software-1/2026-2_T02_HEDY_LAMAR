# Critérios de julgamento

## 1. Objetivo

Este documento estabelece os níveis de pontuação e os critérios de julgamento utilizados para interpretar os resultados das métricas de avaliação da qualidade do Sua Grade UnB.

Os critérios foram definidos para permitir uma interpretação objetiva e consistente dos resultados obtidos, relacionando os valores calculados a níveis de qualidade previamente estabelecidos. Cada métrica possui critérios próprios, considerando sua definição, sua fórmula e a quantidade de observações utilizadas na avaliação.

As métricas são classificadas em quatro níveis: **Insuficiente, Satisfatório, Bom e Excelente**. O nível atribuído depende do resultado calculado e dos limites estabelecidos para a respectiva métrica.

Os critérios deste documento complementam as definições, os procedimentos de coleta e os resultados apresentados em `metricas.md`.

## 2. Níveis de pontuação

Os níveis de pontuação são definidos conforme os seguintes princípios:

| Nível | Interpretação |
| :--- | :--- |
| Insuficiente | O resultado indica que a característica avaliada apresenta desempenho abaixo do mínimo estabelecido para uma avaliação satisfatória. |
| Satisfatório | O resultado atende parcialmente ao nível esperado, mas apresenta limitações relevantes. |
| Bom | O resultado demonstra atendimento consistente ao aspecto avaliado, embora ainda existam limitações. |
| Excelente | O resultado atende integralmente ou de maneira muito elevada ao critério estabelecido para a métrica. |

Para métricas expressas em porcentagem, os intervalos são definidos de forma que cada resultado pertença a um único nível, sem sobreposição entre as faixas.

## 3. Critérios de julgamento por métrica

### 3.1. M1 — Completude funcional

**Objetivo do julgamento:** avaliar a proporção das funcionalidades previstas no *story map* que estão implementadas no Sua Grade UnB.

A métrica é calculada pela proporção entre as funcionalidades implementadas e o total de funcionalidades planejadas.

| Nível | Resultado | Critério de julgamento |
| :--- | :--- | :--- |
| Insuficiente | Menor que 63,64% | Menos de 7 das 11 funcionalidades planejadas estão implementadas. |
| Satisfatório | De 63,64% a 81,81% | Entre 7 e 8 funcionalidades estão implementadas, indicando lacunas relevantes em relação ao planejamento. |
| Bom | De 81,82% a 89,99% | 9 das 11 funcionalidades estão implementadas, com poucas funcionalidades ausentes. |
| Excelente | De 90% a 100% | Pelo menos 10 das 11 funcionalidades estão implementadas. |

**Resultado obtido:** 90,91%.

**Julgamento:** Excelente. O produto apresenta 10 das 11 funcionalidades planejadas implementadas. A ausência da operação de exclusão de uma grade salva localmente não chega a impedir que o resultado alcance o nível Excelente conforme os limites estabelecidos.

### 3.2. M2 — Correção funcional

**Objetivo do julgamento:** avaliar a proporção dos atributos das informações acadêmicas exibidas pelo Sua Grade UnB que correspondem às informações registradas no SIGAA, considerando professor, local e horário das disciplinas verificadas.

A classificação considera o número de atributos corretos em relação ao total de atributos verificados. Para as cinco disciplinas avaliadas, foram verificados 15 atributos (três por disciplina).

| Nível | Resultado | Critério de julgamento |
| :--- | :--- | :--- |
| Insuficiente | Menor que 70% | Menos de 11 dos 15 atributos correspondem às informações do SIGAA. |
| Satisfatório | De 70% a 84,99% | Entre 11 e 12 atributos correspondem às informações do SIGAA. |
| Bom | De 85% a 94,99% | Entre 13 e 14 atributos correspondem às informações do SIGAA. |
| Excelente | De 95% a 100% | Os 15 atributos correspondem às informações do SIGAA. |

**Resultado obtido:** 100%.

**Julgamento:** Excelente. Todos os 15 atributos verificados — professor, local e horário das cinco disciplinas — corresponderam às informações registradas no SIGAA. Esse julgamento se limita às disciplinas e aos atributos efetivamente avaliados, não representando garantia de que absolutamente todas as informações acadêmicas exibidas pelo sistema estejam corretas.

### 3.3. M3 — Adequação às tarefas dos usuários

**Objetivo do julgamento:** avaliar a proporção das tarefas selecionadas que são adequadamente atendidas pelas funcionalidades disponíveis e permitem alcançar seus objetivos.

| Nível | Resultado | Critério de julgamento |
| :--- | :--- | :--- |
| Insuficiente | Menor que 60% | Menos de 3 das 5 tarefas avaliadas são adequadamente atendidas. |
| Satisfatório | De 60% a 79,99% | 3 das 5 tarefas são adequadamente atendidas. |
| Bom | De 80% a 99,99% | 4 das 5 tarefas são adequadamente atendidas. |
| Excelente | 100% | Todas as 5 tarefas avaliadas são adequadamente atendidas. |

**Resultado registrado:** 100%.

**Julgamento provisório:** Excelente, conforme o resultado registrado em `metricas.md`.

A classificação definitiva depende da confirmação de que cada tarefa foi efetivamente atendida pelo produto segundo condições de aceitação previamente estabelecidas. A simples relação de uma tarefa com o objetivo principal do sistema não é suficiente para demonstrar seu atendimento adequado.

### 3.4. M4 — Maturidade

**Objetivo do julgamento:** avaliar a proporção dos cenários de teste de confiabilidade concluídos sem falhas observáveis.

| Nível | Resultado | Critério de julgamento |
| :--- | :--- | :--- |
| Insuficiente | Menor que 50% | Menos da metade dos cenários é concluída sem falhas observáveis. |
| Satisfatório | De 50% a 74,99% | Pelo menos metade dos cenários é concluída sem falhas, mas existem falhas em parte relevante dos testes. |
| Bom | De 75% a 99,99% | Pelo menos 3 dos 4 cenários são concluídos sem falhas observáveis. |
| Excelente | 100% | Os 4 cenários são concluídos sem falhas observáveis. |

**Resultado obtido:** 100%.

**Julgamento:** Excelente. Todos os quatro cenários registrados foram concluídos sem falhas observáveis. O resultado indica comportamento satisfatório nas condições testadas, sem garantir ausência de falhas em situações não avaliadas.

### 3.5. M5 — Disponibilidade observada

**Objetivo do julgamento:** avaliar a proporção das verificações programadas em que o produto está acessível e permite executar a operação funcional selecionada.

Considerando as 15 verificações previstas, os níveis são definidos da seguinte forma:

| Nível | Resultado | Critério de julgamento |
| :--- | :--- | :--- |
| Insuficiente | Menor que 80% | Menos de 12 das 15 verificações são bem-sucedidas. |
| Satisfatório | De 80% a 86,66% | 12 das 15 verificações são bem-sucedidas. |
| Bom | De 86,67% a 99,99% | Entre 13 e 14 verificações são bem-sucedidas. |
| Excelente | 100% | As 15 verificações são bem-sucedidas. |

**Resultado registrado:** 100%.

**Julgamento provisório:** Excelente. O resultado registrado indica que o produto esteve acessível em todas as verificações realizadas. A classificação definitiva depende da conferência dos registros de coleta e das evidências correspondentes às 15 verificações.

Esse julgamento se refere à disponibilidade observada nos horários avaliados e não implica que o sistema tenha permanecido continuamente disponível durante todo o período.

### 3.6. M6 — Tolerância a falhas

**Objetivo do julgamento:** avaliar a proporção das situações de falha em que o sistema identifica o problema e apresenta um aviso adequado ao usuário.

A classificação considera a quantidade de situações de falha tratadas adequadamente em relação ao total de situações avaliadas.

| Nível | Resultado | Critério de julgamento |
| :--- | :--- | :--- |
| Insuficiente | Menor que 60% | Menos de 3 das 5 situações avaliadas são identificadas e comunicadas adequadamente. |
| Satisfatório | De 60% a 79,99% | 3 das 5 situações são identificadas e comunicadas adequadamente. |
| Bom | De 80% a 99,99% | 4 das 5 situações são identificadas e comunicadas adequadamente. |
| Excelente | 100% | Todas as 5 situações são identificadas e comunicadas adequadamente. |

**Resultado registrado:** 100%.

**Julgamento provisório:** Excelente, caso seja confirmado que as cinco situações apresentadas na tabela de testes correspondem ao conjunto efetivamente avaliado e que todas foram tratadas adequadamente.

A métrica considera a identificação e a comunicação das situações de falha. Não avalia, por si só, recuperação automática, continuidade do serviço após erros ou prevenção de perda de dados.

### 3.7. M7 — Adaptabilidade em ambientes avaliados

**Objetivo do julgamento:** avaliar a proporção dos ambientes de navegação selecionados em que o produto pode ser utilizado sem modificações específicas.

| Nível | Resultado | Critério de julgamento |
| :--- | :--- | :--- |
| Insuficiente | Menor que 66,67% | Menos de 4 dos 6 ambientes avaliados apresentam funcionamento adequado. |
| Satisfatório | De 66,67% a 83,32% | 4 dos 6 ambientes apresentam funcionamento adequado. |
| Bom | De 83,33% a 99,99% | 5 dos 6 ambientes apresentam funcionamento adequado. |
| Excelente | 100% | Os 6 ambientes avaliados apresentam funcionamento adequado. |

**Resultado obtido:** 100%.

**Julgamento:** Excelente. O produto funcionou corretamente nos seis ambientes de navegação registrados, incluindo navegadores utilizados em computadores e dispositivos móveis. A conclusão é restrita aos ambientes efetivamente testados e não garante compatibilidade com todos os navegadores, dispositivos ou sistemas operacionais.

## 4. Procedimento de aplicação dos critérios

Para garantir a consistência do julgamento, devem ser seguidos os seguintes passos:

1. Obter os dados brutos e as evidências referentes à métrica avaliada.
2. Verificar se a coleta foi realizada conforme o procedimento definido em `metricas.md`.
3. Confirmar o total de observações válidas e a quantidade de resultados que atendem às condições estabelecidas.
4. Calcular o resultado utilizando a fórmula correspondente à métrica.
5. Comparar o resultado com os intervalos definidos neste documento.
6. Atribuir o nível de pontuação correspondente, sem alterar os limites em função do resultado observado.
7. Registrar o resultado, o nível atribuído e a justificativa do julgamento.

Quando os dados forem insuficientes, inconsistentes ou não permitirem verificar as condições de avaliação, o julgamento deverá ser identificado como pendente de confirmação, em vez de se atribuir automaticamente um nível de qualidade.

## 5. Limitações e rastreabilidade

Os julgamentos devem ser interpretados considerando as condições, os cenários e os ambientes efetivamente avaliados. Resultados elevados em uma métrica não demonstram, isoladamente, que todas as dimensões da qualidade do produto apresentam o mesmo nível de qualidade.

Os dados brutos, as evidências e os cálculos devem permanecer disponíveis no repositório do projeto, permitindo verificar a relação entre cada medição e seu respectivo julgamento.

Antes da consolidação dos resultados, devem ser conferidas eventuais divergências entre as quantidades descritas nos procedimentos de coleta, nas tabelas de testes e nos cálculos apresentados em `metricas.md`.

## 6. Histórico de versões

| Versão | Descrição | Autor | Data |
| :---: | :--- | :--- | :--- |
| 1.0 | Versão inicial dos critérios de julgamento e dos níveis de pontuação das métricas. | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 22/10/2026 |
| 1.1 | Atualização de correção funcional. | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 24/10/2026 |
