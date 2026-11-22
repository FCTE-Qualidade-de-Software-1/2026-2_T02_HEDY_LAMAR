# Julgamento final da qualidade

## 1. Introdução

Esta página apresenta o julgamento final da qualidade do **Sua Grade UnB** para as três características avaliadas: Adequação Funcional, Confiabilidade e Portabilidade. O julgamento usa os resultados registrados em [Métricas de avaliação](Metricas.md) e os níveis definidos em [Critérios de julgamento](../fase-2/criterios.md), e responde aos objetivos G1, G2 e G3 de [Objetivos, questões e hipóteses](../fase-2/objetivos.md).

O julgamento também é relacionado ao propósito da avaliação, estabelecido na Fase 1 em [Propósito da avaliação](../fase-1/proposito.md): identificar pontos de melhoria em Adequação Funcional, Confiabilidade e Portabilidade para apoiar a priorização de correções e evoluções pela equipe mantenedora, que é a requisitante da avaliação.

## 2. Método de julgamento

**Nível por métrica.** Cada métrica (M1 a M7) é classificada em Insuficiente, Satisfatório, Bom ou Excelente, conforme os limites de [Critérios de julgamento](../fase-2/criterios.md). Os limites não foram alterados em função dos resultados.

**Nível por característica.** Os critérios da Fase 2 definem níveis por métrica, mas não definem como combiná-los em um nível por característica. Para esta página, a equipe adotou a seguinte regra: o nível de uma característica é o **menor nível** entre as suas métricas. A escolha é conservadora: uma característica não é julgada melhor do que o aspecto mais fraco que foi medido, o que combina com o propósito de apontar pontos de melhoria.

**Situação do julgamento.** Quando uma métrica depende de confirmação indicada em [Critérios de julgamento](../fase-2/criterios.md), o julgamento da característica é marcado como **provisório**, em vez de ser tratado como definitivo.

**Alcance.** Todos os julgamentos valem para o produto em produção, avaliado externamente (caixa-preta), no estado de 17/10/2026, para as amostras e ambientes efetivamente testados.

## 3. Resultados e níveis por métrica

<font size="3"><p style="text-align: left">Tabela 1: Resultado e nível de cada métrica</p></font>

| Métrica | Característica | Resultado | Amostra | Nível | Situação |
| :--- | :--- | :---: | :--- | :--- | :--- |
| M1 — Completude funcional | Adequação Funcional | 100% | 11 de 11 funções | Excelente | Confirmado |
| M2 — Correção funcional | Adequação Funcional | 100% | 15 de 15 atributos (5 disciplinas) | Excelente | Confirmado |
| M3 — Adequação às tarefas | Adequação Funcional | 100% | 5 de 5 tarefas | Excelente | Provisório |
| M4 — Maturidade | Confiabilidade | 100% | 4 de 4 cenários | Excelente | Confirmado |
| M5 — Disponibilidade observada | Confiabilidade | 100% | 15 de 15 verificações | Excelente | Provisório |
| M6 — Tolerância a falhas | Confiabilidade | 100% | 5 de 5 situações | Excelente | Confirmado |
| M7 — Adaptabilidade | Portabilidade | 100% | 6 de 6 ambientes | Excelente | Confirmado |

Fonte: [Métricas de avaliação](Metricas.md) e [Critérios de julgamento](../fase-2/criterios.md).

<font size="3"><p style="text-align: left">Autor(es): [João Vitor](https://github.com/Jauzimm), 2026.</p></font>

Notas sobre as situações provisórias e sobre as revisões da M1 e da M6:

- **M1:** o nível Excelente exige pelo menos 10 das 11 funções. As 11 funções estão implementadas. A exclusão de uma grade salva localmente (R9), registrada antes como ausente, foi verificada na coleta complementar de 18 e 19/11/2026 e está disponível no produto (ver a revisão em [Métricas de avaliação](Metricas.md)).
- **M3:** [Critérios de julgamento](../fase-2/criterios.md) condiciona a classificação à confirmação de que cada tarefa foi atendida segundo condições de aceitação definidas antes da coleta. Em [Métricas de avaliação](Metricas.md), a coleta registra a relação de cada tarefa com o objetivo do produto, sem evidência por tarefa.
- **M5:** depende da conferência dos registros das 15 verificações. Pelos nomes dos arquivos de evidência, alguns horários de captura ficaram fora das janelas definidas no Plano de Avaliação (por exemplo, 12h13 e 23h40).
- **M6:** as cinco situações da tabela de testes são os cinco testes definidos no Plano de Avaliação (seção 2.6), cada um com evidência da coleta original. O texto de coleta citava apenas quatro e foi completado na revisão de 21/11/2026 (ver [Métricas de avaliação](Metricas.md#m6-tolerancia-a-falhas)). O julgamento passa a confirmado.

## 4. Julgamento por característica

### 4.1. Adequação Funcional (objetivo G1)

**Nível: Excelente (provisório).** Menor nível entre M1, M2 e M3, todos Excelente. O julgamento é provisório por causa da M3.

- **Q1 — Completude funcional (H1):** as 11 funções previstas no *story map* estão implementadas. A hipótese H1 prevê que ela seria contrariada se alguma função estivesse ausente; portanto, **H1 não foi contrariada**.
- **Q2 — Corretude funcional (H2):** professor, local e horário das cinco disciplinas verificadas coincidiram com o SIGAA. H2 foi sustentada para essa amostra. A M2 compara atributos das turmas; a parte da Q2 sobre grades geradas sem conflito de horário ou disciplinas repetidas não tem métrica própria, de modo que H2 não foi verificada nesse aspecto.
- **Q3 — Adequação às tarefas (H3):** as cinco tarefas avaliadas foram consideradas atendidas, de forma provisória, conforme a nota da M3.

**Resposta ao objetivo G1:** nos aspectos medidos, o produto oferece as funções necessárias à tarefa principal e exibe dados coerentes com o SIGAA. Nas 11 funções contadas na M1, não foi identificada ausência. A exportação em PDF, tratada como saída do produto na Fase 1, não consta entre as 11 funções contadas na M1.

### 4.2. Confiabilidade (objetivo G2)

**Nível: Excelente (provisório).** Menor nível entre M4, M5 e M6, todos Excelente. O julgamento é provisório por causa da M5.

- **Q4 — Maturidade (H4):** os quatro cenários (repetição das operações, persistência das grades, uso contínuo e acesso em sessões diferentes) foram concluídos sem falhas observáveis. H4 foi sustentada nas condições testadas. [Métricas de avaliação](Metricas.md) não anexa evidências a esses cenários.
- **Q5 — Disponibilidade (H5):** as 15 verificações, em cinco dias, foram bem-sucedidas. H5 foi sustentada para os horários observados, sem permitir concluir sobre disponibilidade contínua.
- **Q6 — Tolerância a falhas (H6):** nas cinco situações avaliadas, o produto identificou o problema e exibiu aviso. Todas as situações são entradas inválidas ou condições impeditivas de uso. A Q6 também trata de falhas em dependências externas (login Google, dados do SIGAA), que não foram testadas; para esse aspecto, H6 não foi verificada. A M6 mede identificação e comunicação, não recuperação nem preservação de dados.

**Resposta ao objetivo G2:** nas condições testadas, não foram observadas falhas operacionais nem indisponibilidade, e as entradas inválidas avaliadas foram tratadas com aviso. O resultado não cobre falhas de serviços externos nem períodos fora das janelas observadas.

### 4.3. Portabilidade (objetivo G3)

**Nível: Excelente.** Determinado pela M7, confirmada.

- **Q7 — Adaptabilidade (H7):** o produto funcionou nos seis ambientes avaliados: Firefox, Opera GX, Brave e Edge em Windows 11, e Chrome e DuckDuckGo em Android. H7 foi sustentada para esses ambientes.
- **Alcance:** os ambientes cobrem dois sistemas operacionais (Windows e Android) e dois formatos de tela (computador e celular). O objetivo G3 menciona sistemas operacionais e tamanhos de tela em geral; macOS, Linux, iOS e outros navegadores não foram avaliados. Instalabilidade foi retirada do escopo na Fase 2, por se tratar de aplicação web.

**Resposta ao objetivo G3:** nos ambientes testados, as funções principais continuam operacionais, sem necessidade de instalação. O resultado não permite afirmar compatibilidade fora da matriz avaliada.

## 5. Coerência com o propósito da Fase 1

O propósito da Fase 1 prevê três decisões da equipe mantenedora, listadas na Tabela 1 de [Propósito da avaliação](../fase-1/proposito.md). A Tabela 2 relaciona cada decisão ao que os resultados permitem concluir.

<font size="3"><p style="text-align: left">Tabela 2: Apoio dos resultados às decisões da equipe mantenedora</p></font>

| Nº | Decisão a apoiar | Evidência prevista na Fase 1 | O que os resultados mostram | Apoio |
| :---: | :--- | :--- | :--- | :---: |
| 1 | Quais divergências de dados e conflitos de horário corrigir primeiro | Comparação dos dados com o SIGAA e verificação das grades geradas | Nenhuma divergência na amostra de 15 atributos (M2). O produto avisa o usuário ao tentar inserir turma em conflito (M6). A ausência de conflito nas grades geradas automaticamente não foi verificada | Parcial |
| 2 | Se a atualização dos dados de turmas deve ser automatizada ou monitorada | Defasagem observada dos dados e falhas durante o uso normal | Os dados conferiam com o SIGAA no dia da verificação (M2), e não houve falhas nos cenários de uso (M4). A defasagem ao longo do tempo e o processo de atualização não foram medidos | Não apoia diretamente |
| 3 | Quais navegadores, sistemas e telas passam a ser suportados e testados | Matriz de funcionamento por ambiente | Funcionamento em seis ambientes, em Windows 11 e Android (M7). Outros sistemas, navegadores e tamanhos de tela não foram avaliados | Parcial |

Fonte: [Propósito da avaliação](../fase-1/proposito.md), [Métricas de avaliação](Metricas.md).

<font size="3"><p style="text-align: left">Autor(es): [João Vitor](https://github.com/Jauzimm), 2026.</p></font>

**Síntese.** O propósito era identificar pontos de melhoria para apoiar a priorização de correções. Nos aspectos medidos, a avaliação não encontrou deficiência objetiva; a ausência da exclusão de grades salvas localmente, apontada na primeira versão, foi revista após a verificação complementar. Os resultados favoráveis apoiam as decisões 1 e 3 de forma parcial e não permitem apoiar a decisão 2 com dados: o resultado da M2 mostra que os dados estavam corretos na data da coleta, mas não informa se a atualização manual deve ser automatizada. Essas lacunas são tratadas como limitações na seção 6 e como oportunidades na página de oportunidades de melhoria.

## 6. Limitações

- **Amostras pequenas:** cinco disciplinas, quatro cenários, cinco situações de falha e seis ambientes. Os resultados não se generalizam para toda a oferta da UnB nem para todos os usuários.
- **Data de referência:** o produto foi observado no estado de 17/10/2026, com coletas entre 19 e 24/10/2026. Alterações posteriores no produto ou no SIGAA não estão refletidas.
- **Avaliação externa:** a abordagem é de caixa-preta, pela interface em produção. Os resultados indicam o que foi observado, não as causas internas.
- **Métricas com julgamento provisório:** M3 e M5, conforme a seção 3. O julgamento de Adequação Funcional e de Confiabilidade pode mudar após a confirmação.
- **Aspectos sem métrica:** conflito de horário em grades geradas, defasagem dos dados, falha de dependências externas e ambientes fora da matriz avaliada.
- **Avaliadores:** a avaliação foi feita pela própria equipe, sem participantes externos.
- **Níveis por característica:** a regra do menor nível é uma escolha da equipe, não uma regra dos critérios da Fase 2. Como todas as métricas ficaram em Excelente, outra regra de combinação não alteraria o nível de nenhuma característica.

## 7. Conclusão

<font size="3"><p style="text-align: left">Tabela 3: Julgamento final por característica</p></font>

| Característica | Objetivo | Nível | Situação |
| :--- | :---: | :--- | :--- |
| Adequação Funcional | G1 | Excelente | Provisório (M3) |
| Confiabilidade | G2 | Excelente | Provisório (M5) |
| Portabilidade | G3 | Excelente | Confirmado |

<font size="3"><p style="text-align: left">Autor(es): [João Vitor](https://github.com/Jauzimm), 2026.</p></font>

Nas condições e amostras avaliadas, o Sua Grade UnB atende aos critérios da Fase 2 nas três características. A qualidade observada é adequada ao uso pretendido de apoiar a equipe mantenedora na priorização de melhorias, com a ressalva de que a avaliação não cobre a atualização dos dados, as grades geradas automaticamente e os ambientes fora da matriz.

## Bibliografia

> 1. RAMOS, Cristiane Soares. *Processo de Avaliação de Produto de Software*. Material da disciplina Qualidade de Software 1. Universidade de Brasília (UnB), 2026.

> 2. ISO/IEC 25010:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. 2011.

## Histórico de Versão

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :----: | :--- | :--- | :---: | :--- | :---: |
| 1.0 | Versão inicial do julgamento final da qualidade | [João Victor Marques](https://github.com/jmarquees) | 15/11/2026 | | |
| 1.1 | Adição dos tópicos 3 e 4 | [João Victor Marques](https://github.com/jmarquees) | 15/11/2026 | | |
| 1.2 | Adição dos tópicos 5 e 6 | [João Victor Marques](https://github.com/jmarquees) | 15/11/2026 | | |
| 1.3 | Adição da conclusão e bibliografia | [João Victor Marques](https://github.com/jmarquees) | 15/11/2026 | | |
| 1.4 | Revisão da M1 (R9 implementada, 11/11) e dos trechos que dependiam dela | [Cauã Clemente](https://github.com/CauaoClemente) | 19/11/2026 | | |
| 1.5 | Confirmação da M6 (cinco situações conforme o Plano de Avaliação) e dos trechos que dependiam dela | [Cauã Clemente](https://github.com/CauaoClemente) | 21/11/2026 | | |