# Oportunidades de melhoria

## 1. Introdução

A identificação das oportunidades de melhoria foi realizada com base nos resultados das métricas de avaliação do Sua Grade UnB e nos respectivos julgamentos de qualidade. O objetivo é identificar aspectos que podem ser aprimorados no produto ou no processo de desenvolvimento, considerando as evidências coletadas e o impacto potencial de cada oportunidade.

As oportunidades foram priorizadas conforme a relevância dos resultados, a existência de evidências e a viabilidade de execução de uma ação de melhoria.

## 2. Oportunidades identificadas

### 2.1. Implementação da exclusão de grades salvas localmente

**Métrica relacionada:** M1 — Completude funcional.

**Evidência:** Foram identificadas 11 funcionalidades planejadas, das quais 10 estão implementadas, resultando em uma completude funcional de 90,91%. A funcionalidade ausente corresponde ao requisito R9, que prevê a exclusão de uma grade horária salva localmente diretamente pelo produto.

**Oportunidade:** Disponibilizar uma funcionalidade que permita ao usuário excluir grades salvas localmente pela própria interface do sistema, sem depender da exclusão manual de arquivos pelo sistema operacional.

**Impacto esperado:** Completar o conjunto de funcionalidades planejadas e oferecer maior autonomia ao usuário no gerenciamento de suas grades.

**Tipo de ação:** Protótipo de alta fidelidade.

**Prioridade:** Alta.

### 2.2. Aprimoramento do processo de revisão de Pull Requests

**Métrica relacionada:** Métrica 3 do PSM/CID — Tempo médio de resolução de Pull Requests.

**Evidência:** A coleta mais recente considerou dez Pull Requests integrados, com tempo médio de resolução de 3,01 dias e mediana de 0,80 dia. A média ultrapassou o limite de três dias estabelecido para a classificação Ideal, sendo influenciada principalmente pelo PR #7, que levou 17,55 dias para ser integrado.

**Oportunidade:** Melhorar o acompanhamento dos Pull Requests pendentes, estabelecendo responsáveis pela revisão e prazos internos para análise e integração.

**Impacto esperado:** Reduzir períodos prolongados de espera, melhorar a previsibilidade das integrações e facilitar o acompanhamento das atividades da equipe.

**Tipo de ação:** Proposta de processo.

**Prioridade:** Média.

### 2.3. Ampliação da cobertura dos testes de avaliação

**Métricas relacionadas:** M2 a M7 — Métricas de avaliação do produto.

**Evidência:** Embora as métricas tenham apresentado resultados favoráveis nos cenários avaliados, algumas coletas utilizaram amostras limitadas, como cinco disciplinas na verificação de correção funcional, quatro cenários de maturidade e seis ambientes de navegação na avaliação de adaptabilidade.

**Oportunidade:** Ampliar gradualmente a quantidade e a diversidade dos cenários utilizados nas avaliações, incluindo mais disciplinas, situações de uso e ambientes de navegação.

**Impacto esperado:** Aumentar a abrangência das avaliações e reduzir as limitações decorrentes de amostras pequenas.

**Tipo de ação:** Template técnico para registro padronizado de cenários, resultados e evidências.

**Prioridade:** Média.

### 2.4. Melhoria da rastreabilidade das contribuições

**Métrica relacionada:** Métrica 2 do PSM/CID — Distribuição de esforço por commits.

**Evidência:** A distribuição dos commits apresentou diferenças entre os integrantes. Além disso, parte das atividades realizadas na elaboração do artigo não estava representada no histórico do Git, pois o código-fonte LaTeX ainda não estava versionado no repositório.

**Oportunidade:** Manter os materiais técnicos do trabalho versionados e utilizar registros complementares para documentar contribuições que não são adequadamente representadas pela quantidade de commits.

**Impacto esperado:** Melhorar a rastreabilidade das atividades e permitir uma interpretação mais completa da participação dos integrantes.

**Tipo de ação:** Proposta de processo.

**Prioridade:** Baixa.

## 3. Priorização

As oportunidades foram organizadas considerando a evidência disponível, o impacto potencial e a viabilidade de execução.

| Prioridade | Oportunidade | Métrica | Tipo de ação |
|:---:|---|---|---|
| Alta | Implementar a exclusão de grades salvas localmente | M1 | Protótipo de alta fidelidade |
| Média | Aprimorar a revisão de Pull Requests | PSM 3 | Proposta de processo |
| Média | Ampliar a cobertura dos testes | M2 a M7 | Template técnico |
| Baixa | Melhorar a rastreabilidade das contribuições | PSM 2 | Proposta de processo |

## 4. Oportunidade selecionada para execução

A oportunidade selecionada para a execução da ação de melhoria é a implementação conceitual da exclusão de grades salvas localmente, correspondente ao requisito R9.

A escolha foi motivada pelo resultado da M1, que identificou uma funcionalidade planejada ainda não disponível no produto. A ausência dessa funcionalidade representa uma oportunidade objetiva de evolução, com impacto direto na capacidade de gerenciamento das grades pelo usuário.

Como o repositório de avaliação não contém o código-fonte oficial do Sua Grade UnB, a ação será realizada por meio de um protótipo de alta fidelidade, demonstrando o fluxo de exclusão de uma grade local, incluindo a confirmação da operação e o retorno visual ao usuário.

O protótipo será apresentado como entrega técnica da Fase 4 e servirá como referência para uma possível implementação futura no produto.

## 5. Considerações finais

A análise identificou oportunidades relacionadas tanto às funcionalidades do produto quanto aos processos de desenvolvimento e avaliação. A ausência da exclusão de grades locais foi considerada a oportunidade prioritária por apresentar evidência direta e impacto funcional claro.

As demais oportunidades representam possibilidades de aprimoramento contínuo, especialmente no acompanhamento das integrações e na ampliação da abrangência das avaliações. A execução da ação selecionada permitirá demonstrar uma melhoria concreta fundamentada nos resultados obtidos.
