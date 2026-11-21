# Conclusões e sugestões de melhoria

## 1. Introdução

Esta página apresenta as conclusões da avaliação do Sua Grade UnB e as sugestões de melhoria dirigidas à equipe mantenedora do produto, que é a requisitante da avaliação, conforme [Propósito da avaliação](../fase-1/proposito.md).

As conclusões partem do [Julgamento final da qualidade](julgamento-final.md), que classifica cada métrica e cada característica pelos níveis de [Critérios de julgamento](../fase-2/criterios.md). As sugestões partem da lista priorizada de [Oportunidades de melhoria](oportunidades-de-melhoria.md), das [Relações entre as características](relacoes-caracteristicas.md) e da [Ação de melhoria](acao-de-melhoria.md) executada pela equipe.

Cada sugestão indica o resultado que a justifica e a [decisão da Fase 1](#tabela-2) que ela apoia. Das quatro sugestões, a equipe de avaliação executou apenas a [S1](#s1); as demais ficam registradas como recomendações. A decisão de implementar cada uma é da equipe mantenedora.

## 2. Conclusões da avaliação

### 2.1. Julgamento final

<font size="3"><p style="text-align: left"><a id="tabela-1"></a>Tabela 1: Julgamento final por característica</p></font>

| Característica | Objetivo | Métricas | Nível | O que o nível significa para o requisitante |
| :--- | :---: | :--- | :--- | :--- |
| Adequação Funcional | G1 | M1, M2 e M3 | Excelente | As 11 funções do *story map* estão implementadas, os 15 atributos verificados coincidem com o SIGAA e as 5 tarefas avaliadas são atendidas |
| Confiabilidade | G2 | M4, M5 e M6 | Excelente | Sem falhas nos 4 cenários, acessível nas 15 verificações e com aviso nas 5 situações de entrada inválida |
| Portabilidade | G3 | M7 | Excelente | Funcionou nos 6 ambientes avaliados, em Windows 11 e Android |

Fonte: [Julgamento final da qualidade](julgamento-final.md) e [Critérios de julgamento](../fase-2/criterios.md).

<font size="3"><p style="text-align: left">Autor(es): [João Vitor](https://github.com/Jauzimm), 2026.</p></font>

Os níveis foram atribuídos pelos limites definidos na Fase 2, sem alteração em função dos resultados, e o nível de cada característica é o menor nível entre as suas métricas ([seção 2 do Julgamento final](julgamento-final.md#2-metodo-de-julgamento)). Os julgamentos das sete métricas estão confirmados pela equipe.

### 2.2. Conclusões

<a id="c1"></a>

#### C1. O produto atende aos critérios da Fase 2

As sete métricas ficaram em 100% e no nível Excelente ([Tabela 1](#tabela-1)), e nenhuma das hipóteses H1 a H7 foi contrariada nos aspectos medidos. O resultado vale para o produto em produção no estado de 17/10/2026 e para as amostras avaliadas: cinco disciplinas, cinco tarefas, quatro cenários de maturidade, quinze verificações de disponibilidade, cinco situações de falha e seis ambientes.

<a id="c2"></a>

#### C2. A avaliação não encontrou deficiência objetiva

A única ausência registrada na primeira versão, a exclusão de grades salvas localmente (R9), foi revista na coleta complementar de 18 e 19/11/2026. A função existe no produto desde dezembro de 2023 ([Relações entre as características, seção 3.2](relacoes-caracteristicas.md#32-funcoes-da-m1-no-celular)), e a M1 passou de 90,91% para 100%, sem mudança de nível. Por isso, as sugestões da [seção 3](#3-sugestoes-de-melhoria-ao-requisitante) tratam de riscos e de lacunas que os resultados deixaram expostos, e nenhuma corrige um defeito medido.

<a id="c3"></a>

#### C3. O maior risco está na atualização dos dados de turmas

A M2 mostra que os dados estavam corretos na data da coleta, mas nenhuma métrica mediu a defasagem dos dados ao longo do tempo. O [README do Sua Grade UnB](https://github.com/unb-mds/2023-2-SuaGradeUnB#-atualização-do-banco-de-dados) informa que a atualização é manual, e a alteração mais recente do produto, de fevereiro de 2026, corrigiu uma falha na coleta dos dados do SIGAA ([Oportunidades de melhoria, seção 2.1](oportunidades-de-melhoria.md#21-indicacao-da-data-da-ultima-atualizacao-dos-dados-do-sigaa)). O [comando de atualização do banco](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/main/api/api/management/commands/updatedb.py) não guarda a data da última atualização bem-sucedida e, quando a coleta no SIGAA falha, apenas imprime uma mensagem no terminal. Se a atualização falhar ou deixar de ser executada, nem o estudante nem a equipe mantenedora são avisados. Por isso a [Decisão 2](#tabela-2) do propósito ficou sem apoio dos resultados ([Julgamento final, seção 5](julgamento-final.md#5-coerencia-com-o-proposito-da-fase-1)).

<a id="c4"></a>

#### C4. Falhas de dependências externas não foram testadas

As cinco situações da M6 são entradas inválidas ou condições impeditivas de uso, e o produto exibiu aviso em todas, no computador e no celular. A indisponibilidade do login Google, da API ou do SIGAA ficou fora dos testes, e a parte da Q6 sobre dependências externas não foi verificada ([Relações entre as características, seção 4.5](relacoes-caracteristicas.md#45-dependencias-externas)).

<a id="c5"></a>

#### C5. A Portabilidade vale para a matriz avaliada

O produto funcionou em Firefox, Opera GX, Brave e Edge no Windows 11 e em Chrome e DuckDuckGo no Android. No Chrome do Android, as 11 funções e os cenários de M4 e M6 também foram repetidos com o mesmo resultado. macOS, Linux, iOS e o Safari não foram avaliados.

### 2.3. Resposta ao propósito da avaliação

O propósito da Fase 1 era identificar pontos de melhoria para apoiar a priorização de correções e evoluções pela equipe mantenedora, por meio de [três decisões](../fase-1/proposito.md#214-como-os-resultados-serao-utilizados).

<font size="3"><p style="text-align: left"><a id="tabela-2"></a>Tabela 2: Conclusão sobre cada decisão da equipe mantenedora</p></font>

| Nº | Decisão da Fase 1 | Conclusão da avaliação | Sugestões |
| :---: | :--- | :--- | :--- |
| 1 | Quais divergências de dados e conflitos de horário corrigir primeiro | Não há divergência a corrigir na amostra (M2). O produto impede conflitos nos pares testados (M6, T4) | — |
| 2 | Se a atualização dos dados deve ser automatizada ou monitorada | Os resultados não medem a defasagem, e uma falha na atualização não é registrada nem comunicada ([C3](#c3)). A recomendação é monitorar primeiro e automatizar depois | [S1](#s1), [S2](#s2) e [S3](#s3) |
| 3 | Quais navegadores, sistemas e telas suportar e testar | Os seis ambientes da M7 podem ser declarados como suportados. Os demais precisam de teste antes | [S4](#s4) |

Fonte: [Propósito da avaliação](../fase-1/proposito.md#214-como-os-resultados-serao-utilizados), [Julgamento final da qualidade](julgamento-final.md) e [seção 2.2](#22-conclusoes) desta página.

<font size="3"><p style="text-align: left">Autor(es): [João Vitor](https://github.com/Jauzimm), 2026.</p></font>

## 3. Sugestões de melhoria ao requisitante

A equipe de avaliação decidiu trabalhar apenas com a [S1](#s1), executada como protótipo de alta fidelidade na [Ação de melhoria](acao-de-melhoria.md). A escolha segue a [seção 4 de Oportunidades de melhoria](oportunidades-de-melhoria.md#4-oportunidade-selecionada-para-execucao): a S1 responde à [Decisão 2](#tabela-2) do propósito, que os resultados não conseguiram apoiar, e trata o risco descrito em [C3](#c3). As sugestões [S2 a S4](#32-sugestoes-nao-executadas-pela-equipe) não foram executadas pela equipe e ficam registradas como recomendações para a equipe mantenedora.

### 3.1. Ação executada pela equipe

<a id="s1"></a>

#### S1. Indicar a data da última atualização dos dados do SIGAA

Prioridade alta. A proposta é gravar a data e a hora de cada execução bem-sucedida do comando de atualização, por período letivo, devolver esse registro junto com os dados de turmas e exibir a data na tela inicial e na busca de matéria. Quando a última atualização passar do limite definido pela equipe mantenedora, a interface mostra um alerta.

A justificativa está em [C3](#c3): a M2 só vale para a data da coleta, e hoje o estudante não tem como saber se as turmas exibidas estão atualizadas. A equipe entregou o protótipo, o caminho de implementação e os critérios de aceitação em [Ação de melhoria, seções 3 a 5](acao-de-melhoria.md#3-prototipo). A conclusão da S1 pode ser verificada pelos critérios CA1 a CA5 da [seção 5 da Ação de melhoria](acao-de-melhoria.md#5-criterios-de-aceitacao).

### 3.2. Sugestões não executadas pela equipe

<a id="s2"></a>

#### S2. Registrar as falhas do comando de atualização

Prioridade alta. Quando a coleta dos dados no SIGAA falhar, o comando deve registrar a falha em um local que a equipe consiga consultar (por exemplo, um log) e terminar indicando erro. Hoje a falha só aparece no terminal de quem executa o comando, e nenhum monitoramento consegue detectá-la ([C3](#c3) e [C4](#c4)). A S2 também é necessária para o [critério CA2](acao-de-melhoria.md#5-criterios-de-aceitacao) da [S1](#s1): uma atualização que falha não pode alterar a data exibida.

Para verificar, basta simular a indisponibilidade do SIGAA em ambiente de desenvolvimento: o comando deve indicar erro, a falha deve ficar registrada e a data exibida pela [S1](#s1) deve continuar a da última atualização bem-sucedida.

<a id="s3"></a>

#### S3. Agendar a atualização dos dados

Prioridade média. A atualização passaria a ser executada de forma agendada, com aviso à equipe quando falhar. A sugestão responde à [Decisão 2](#tabela-2) do propósito e a [C3](#c3): segundo o README do produto, a atualização é feita manualmente.

A S3 depende da [S2](#s2), porque automatizar sem detectar falhas só repetiria a falha silenciosa com mais frequência. Para verificar, a data exibida pela [S1](#s1) não deve passar do limite definido pela equipe mantenedora durante o período de matrícula.

<a id="s4"></a>

#### S4. Publicar a matriz de ambientes suportados

Prioridade baixa. A documentação do produto declararia como suportados os seis ambientes verificados na M7, e o Safari no iOS e no macOS seria testado antes de entrar na lista. A sugestão responde à [Decisão 3](#tabela-2) do propósito e a [C5](#c5): os seis ambientes funcionaram (M7, 100%), mas os sistemas da Apple não foram avaliados.

A S4 está concluída quando a lista de ambientes suportados estiver publicada na documentação do produto, com uma evidência de teste para cada ambiente.

### 3.3. Síntese

<font size="3"><p style="text-align: left"><a id="tabela-3"></a>Tabela 3: Síntese das sugestões ao requisitante</p></font>

| Nº | Ação | Resultado que justifica | [Decisão da Fase 1](#tabela-2) | Prioridade | Executada pela equipe |
| :---: | :--- | :--- | :---: | :---: | :---: |
| [S1](#s1) | Indicar a data da última atualização dos dados | M2 válida só na data da coleta; atualização sem registro de data ([C3](#c3)) | [2](#tabela-2) | Alta | Sim (protótipo) |
| [S2](#s2) | Registrar as falhas do comando de atualização | Falha na atualização apenas impressa no terminal ([C3](#c3) e [C4](#c4)) | [2](#tabela-2) | Alta | Não |
| [S3](#s3) | Agendar a atualização dos dados | Atualização manual, segundo o README do produto ([C3](#c3)) | [2](#tabela-2) | Média | Não |
| [S4](#s4) | Publicar a matriz de ambientes suportados | 6 de 6 ambientes funcionaram; sistemas da Apple não avaliados (M7 e [C5](#c5)) | [3](#tabela-2) | Baixa | Não |

Fonte: [seções 2](#2-conclusoes-da-avaliacao) e [3](#3-sugestoes-de-melhoria-ao-requisitante) desta página.

<font size="3"><p style="text-align: left">Autor(es): [João Vitor](https://github.com/Jauzimm), 2026.</p></font>

## 4. Limitações

- A equipe de avaliação não mantém o código do produto. A [S1](#s1) foi executada como protótipo, sem implementação no produto, e as sugestões [S2 a S4](#32-sugestoes-nao-executadas-pela-equipe) são recomendações.
- A equipe mantenedora é a requisitante por premissa da avaliação, já que não há requisitante formal ([Propósito da avaliação, seção 2.1.3](../fase-1/proposito.md#213-para-quem-avaliar)). As sugestões não foram validadas com ela.
- [S1](#s1), [S2](#s2) e [S3](#s3) partem de um risco documentado pelo próprio produto. A avaliação não observou dados desatualizados.
- As conclusões valem para as amostras, os ambientes e a data de referência descritos na [seção 6 do Julgamento final](julgamento-final.md#6-limitacoes).

## 5. Considerações finais

Nas amostras e nos ambientes testados, o Sua Grade UnB atende aos critérios da Fase 2 nas três características. O ponto que mais preocupa é a atualização manual dos dados, que hoje não é registrada nem monitorada. A equipe executou a [S1](#s1) para que o estudante veja a data da atualização, e recomenda à equipe mantenedora registrar as falhas ([S2](#s2)) antes de agendar a atualização ([S3](#s3)).

## Bibliografia

> 1. RAMOS, Cristiane Soares. *Processo de Avaliação de Produto de Software*. Material da disciplina Qualidade de Software 1. Universidade de Brasília (UnB), 2026.

> 2. ISO/IEC 25010:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE) System and software quality models*. 2011.

> 3. UNB-MDS. *Sua Grade UnB*: código-fonte. GitHub, 2023-2026. Disponível em: <https://github.com/unb-mds/2023-2-SuaGradeUnB>. Acesso em: 21 nov. 2026.

## Histórico de Versão

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :----: | :--- | :--- | :---: | :--- | :---: |
| 1.0 | Versão inicial das conclusões e das sugestões de melhoria ao requisitante | [João Vitor](https://github.com/Jauzimm) | 21/11/2026 | | |
| 1.1 | Links internos para as tabelas, as conclusões, as sugestões e as seções citadas | [João Vitor](https://github.com/Jauzimm) | 21/11/2026 | | |
