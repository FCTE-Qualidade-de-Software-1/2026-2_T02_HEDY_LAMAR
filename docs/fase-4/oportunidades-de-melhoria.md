# Oportunidades de melhoria

## 1. Introdução

A identificação das oportunidades de melhoria foi realizada com base nos resultados das métricas de avaliação do Sua Grade UnB, nos respectivos julgamentos de qualidade e nas limitações registradas no [Julgamento final](julgamento-final.md). O objetivo é identificar aspectos que podem ser aprimorados no produto ou no processo de avaliação, considerando as evidências coletadas e o impacto potencial de cada oportunidade.

As oportunidades foram priorizadas conforme a relação com o [propósito da avaliação](../fase-1/proposito.md), a existência de evidências e a viabilidade de execução de uma ação de melhoria.

**Revisão (19/11/2026).** A primeira versão desta página selecionava a implementação da exclusão de grades salvas localmente (R9). A verificação complementar de 18 e 19/11/2026 confirmou que essa função já está implementada no produto, e a M1 foi revisada para 11/11, conforme [Métricas de avaliação](Metricas.md). As oportunidades foram então revisadas. As oportunidades sobre o processo da equipe (revisão de Pull Requests e rastreabilidade das contribuições) continuam tratadas nas [decisões de gestão](../gestao/decisoes.md) D2 e D3 do PSM.

## 2. Oportunidades identificadas

### 2.1. Indicação da data da última atualização dos dados do SIGAA

**Relação com a avaliação:** M2 — Correção funcional; Decisão 2 do [propósito da avaliação](../fase-1/proposito.md).

**Evidência:**

1. **Decisão em aberto.** O propósito da avaliação definiu que os resultados apoiariam a Decisão 2: se a atualização dos dados de turmas, feita manualmente, deve ser automatizada ou monitorada. O [Julgamento final](julgamento-final.md) (seção 5) registra que os resultados não permitem apoiar essa decisão com dados.
2. **Risco documentado pelo produto.** O [README do Sua Grade UnB](https://github.com/unb-mds/2023-2-SuaGradeUnB#-atualização-do-banco-de-dados) informa que o banco de dados precisa ser atualizado com certa frequência e que as requisições ao SIGAA ainda são feitas de forma manual. A alteração mais recente do produto, de fevereiro de 2026, corrigiu uma falha justamente na coleta dos dados do SIGAA ([PR #250](https://github.com/unb-mds/2023-2-SuaGradeUnB/pull/250)).
3. **Lacuna das métricas.** A M2 mostrou que os dados exibidos correspondiam ao SIGAA (100%), mas apenas na data da coleta. O Julgamento final (seção 6) lista a defasagem dos dados entre os aspectos sem métrica. Hoje, nem a avaliação nem o usuário conseguem saber, pelo produto, se as turmas exibidas estão atualizadas.
4. **Impacto no usuário.** O propósito da avaliação registra que uma turma errada ou desatualizada leva o estudante a planejar o semestre sobre informação incorreta.
5. **Falha silenciosa no código do produto.** No [comando de atualização do banco](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/main/api/api/management/commands/updatedb.py), uma falha na coleta apenas imprime uma mensagem no terminal de quem executa o comando ("Houve um erro na atualização do banco de dados"). O produto não guarda a data da última atualização bem-sucedida e não exibe nenhuma informação sobre a atualização na interface. Se a atualização falhar ou deixar de ser executada, o estudante continua vendo os dados antigos sem nenhum aviso.

**Oportunidade:** Exibir na interface a data e a hora da última atualização dos dados do SIGAA, com um alerta quando a última atualização ultrapassar um limite definido pela equipe mantenedora (por exemplo, 48 horas). Para isso, o comando de atualização passaria a registrar a data e a hora de cada execução bem-sucedida, e a interface passaria a exibir esse registro.

**Impacto esperado:** Permitir que o estudante saiba quando conferir as turmas no SIGAA antes da matrícula e oferecer à equipe mantenedora um meio simples de monitorar a atualização, apoiando a Decisão 2.

**Natureza:** Melhoria preventiva e de monitoramento. A avaliação não mediu dados desatualizados; a oportunidade decorre de um risco documentado pelo próprio produto e de uma decisão do propósito que os resultados não conseguiram apoiar.

**Tipo de ação:** Protótipo de alta fidelidade.

**Prioridade:** Alta.

### 2.2. Filtros de busca por horário e por unidade acadêmica

**Relação com a avaliação:** M3 — Adequação às tarefas; coleta complementar de 18 e 19/11/2026.

**Evidência:**

1. A busca aceita apenas o nome da matéria ou do professor ([evidência](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/complementar/02-busca-qualidade.png)).
2. Os resultados misturam disciplinas de várias unidades e da pós-graduação. A busca por "qualidade" retornou, entre outras, Administração da Qualidade (ADM) e Qualidade de Carne de Aves e Ovos (PPGSA) ([evidência](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/complementar/17-m4-busca03-qualidade.png)); a busca por "algoritmos" retornou disciplinas da FCTE, do CIC, da ENE e do PPCA ([evidência](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/complementar/23-m4-busca09-algoritmos.png)).
3. A preferência de horário só aparece na etapa de geração da grade, como intensidade por turno ([evidência](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/complementar/04-periodo-preferencia.png)). Para escolher turmas em um dia e turno específicos, o usuário precisa abrir cada disciplina e interpretar os códigos de horário (por exemplo, 24M34).

**Oportunidade:** Permitir filtrar os resultados da busca por dia e turno das turmas e por unidade acadêmica (por exemplo, apenas FCTE ou apenas graduação).

**Impacto esperado:** Reduzir o esforço para encontrar turmas compatíveis com a rotina do estudante, tarefa central do produto.

**Natureza:** Melhoria preventiva. A M3 mostrou que as cinco tarefas avaliadas podem ser concluídas (100%); a oportunidade trata do esforço para concluí-las, que não foi medido.

**Tipo de ação:** Proposta de requisito, com história de usuário e critérios de aceitação.

**Prioridade:** Média.

### 2.3. Ampliação da cobertura dos testes de avaliação

**Métricas relacionadas:** M2 a M7 — Métricas de avaliação do produto.

**Evidência:** Embora as métricas tenham apresentado resultados favoráveis nos cenários avaliados, algumas coletas utilizaram amostras limitadas, como cinco disciplinas na verificação de correção funcional, quatro cenários de maturidade e seis ambientes de navegação na avaliação de adaptabilidade. A página [Relações entre as características](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_HEDY_LAMAR/fase-4/relacoes-caracteristicas/) também identificou relações que ficaram sem dados, como os cenários de confiabilidade nos demais ambientes da M7.

**Oportunidade:** Ampliar gradualmente a quantidade e a diversidade dos cenários utilizados nas avaliações, incluindo mais disciplinas, situações de uso e ambientes de navegação, e registrar o navegador e o dispositivo de cada coleta.

**Impacto esperado:** Aumentar a abrangência das avaliações e reduzir as limitações decorrentes de amostras pequenas.

**Tipo de ação:** Template técnico para registro padronizado de cenários, resultados e evidências.

**Prioridade:** Média.

## 3. Priorização

As oportunidades foram organizadas considerando a relação com o propósito da avaliação, a evidência disponível, o impacto potencial e a viabilidade de execução.

| Prioridade | Oportunidade | Relação com a avaliação | Tipo de ação |
|:---:|---|---|---|
| Alta | Indicar a data da última atualização dos dados do SIGAA | M2 e Decisão 2 do propósito | Protótipo de alta fidelidade |
| Média | Filtrar a busca por horário e por unidade acadêmica | M3 e coleta complementar | Proposta de requisito |
| Média | Ampliar a cobertura dos testes de avaliação | M2 a M7 | Template técnico |

## 4. Oportunidade selecionada para execução

A oportunidade selecionada para a execução da ação de melhoria é a indicação da data da última atualização dos dados do SIGAA (seção 2.1).

A escolha foi motivada pela relação direta com o propósito da avaliação: a Decisão 2 trata da atualização dos dados, e o Julgamento final registra que os resultados não permitiram apoiá-la. A oportunidade também tem evidência documental no próprio produto e impacto direto na confiança do estudante nos dados exibidos.

Como o repositório de avaliação não contém o código-fonte oficial do Sua Grade UnB, a ação será realizada por meio de um protótipo de alta fidelidade, demonstrando a indicação da data da última atualização na interface e o alerta exibido quando os dados ultrapassarem o limite definido.

O protótipo será apresentado como entrega técnica da Fase 4 e servirá como referência para uma possível implementação futura no produto.

## 5. Considerações finais

A análise identificou oportunidades relacionadas ao produto e ao processo de avaliação. A indicação da data de atualização dos dados foi considerada a oportunidade prioritária por responder a uma decisão prevista no propósito da avaliação e por ter evidência documental no próprio produto.

Os filtros de busca e a ampliação da cobertura dos testes representam possibilidades de aprimoramento contínuo do produto e das próximas avaliações. A execução da ação selecionada permitirá demonstrar uma melhoria concreta fundamentada nos resultados e nas limitações registradas.

## Histórico de Versão

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :----: | :--- | :--- | :---: | :--- | :---: |
| 1.0 | Criação do documento de oportunidades de melhoria | [Leonardo Rodrigues](https://github.com/LeonardoRodriguesMarrtinns99) | 14/11/2026 | | |
| 1.1 | Atualização dos números da Métrica 3 do PSM após a recoleta | [Cauã Clemente](https://github.com/CauaoClemente) | 15/11/2026 | | |
| 1.2 | Revisão das oportunidades após a verificação complementar da R9 | [Cauã Clemente](https://github.com/CauaoClemente) | 19/11/2026 | | |
