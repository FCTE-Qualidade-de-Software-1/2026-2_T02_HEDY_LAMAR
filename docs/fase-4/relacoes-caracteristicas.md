# Relações entre as características de qualidade

## 1. Introdução

Esta página discute as relações entre as três características avaliadas no **Sua Grade UnB**: Adequação Funcional, Confiabilidade e Portabilidade. Cada relação é apoiada nos resultados registrados em [Métricas de avaliação](Metricas.md), no [Julgamento final da qualidade](julgamento-final.md) e em uma **coleta complementar** feita em 18 e 19/11/2026 (seção 3). Quando os dados não permitem concluir, a página declara essa limitação, em vez de afirmar uma relação não verificada.

As relações discutidas aqui são **dependências entre comportamentos observados**, isto é, situações em que o resultado de uma característica depende de um comportamento medido em outra. Elas não são correlações estatísticas: as sete métricas ficaram em 100%, então não houve variação para observar se a piora de uma característica acompanha a de outra (seção 5).

## 2. Ambiente de cada medição

As relações que envolvem a Portabilidade dependem de saber onde cada métrica foi medida. O [Plano de avaliação](../fase-3/plano-avaliacao.md) define o navegador de referência (Google Chrome no computador) para a M1 e a matriz de seis ambientes para a M7. Para M2 a M6, nem o plano nem as [Métricas de avaliação](Metricas.md) registram o navegador usado em cada coleta.

<font size="3"><p style="text-align: left">Tabela 1: Ambiente de coleta das métricas</p></font>

| Coleta | Métricas | Ambiente |
| :--- | :--- | :--- |
| Original (outubro de 2026) | M1 | Navegador de referência: Google Chrome no computador |
| Original (outubro de 2026) | M2 a M6 | Não registrado por coleta |
| Original (outubro de 2026) | M7 | Firefox, Opera GX, Brave e Edge no Windows; Chrome e DuckDuckGo no Android |
| Complementar (18 e 19/11/2026) | Funções da M1, cenários da M4 e situações da M6 | Chrome 157.0.8103.51 no Android 15 (Motorola moto g34 5G) |
| Complementar (19/11/2026) | Função R9 da M1 | Chrome 157.0.8103.79 no Windows 10 |

Fonte: [Plano de avaliação](../fase-3/plano-avaliacao.md), [Métricas de avaliação](Metricas.md) e seção 3 desta página.

<font size="3"><p style="text-align: left">Autor(es): [Cauã Clemente](https://github.com/CauaoClemente), 2026.</p></font>

## 3. Coleta complementar (18 e 19/11/2026)

### 3.1. Objetivo e regras

A primeira versão desta discussão mostrou que as relações com a Portabilidade não tinham dados: as funções da M1 e os cenários de Confiabilidade não tinham sido repetidos em nenhum ambiente da matriz da M7. A coleta complementar repetiu, no **Chrome do Android** (um dos seis ambientes da M7), as funções da M1, os quatro cenários da M4 e as cinco situações da M6.

A coleta foi feita por [Cauã Clemente](https://github.com/CauaoClemente), no produto em produção, com o período 2026/2, entre 18/11/2026 às 18h29 e 19/11/2026 às 03h00. Ela **complementa** as medições de outubro e não substitui os resultados de M1 a M7. As evidências estão em `docs/evidencias/complementar/`.

### 3.2. Funções da M1 no celular

<font size="3"><p style="text-align: left">Tabela 2: Funções da M1 verificadas no Chrome do Android</p></font>

| ID | Função | Resultado | Evidência |
| :---: | :--- | :--- | :--- |
| R1 | Criar grade horária | Grade gerada e salva | [E5](../evidencias/complementar/05-grade-local-salva.png) |
| R2 | Filtrar matéria em uma lista pré-definida | Busca retornou a disciplina | [E2](../evidencias/complementar/02-busca-qualidade.png) |
| R3 | Selecionar uma turma em uma lista | Turma marcada em verde | [E2](../evidencias/complementar/02-busca-qualidade.png) |
| R4 | Adicionar matéria selecionada | Três disciplinas na tela inicial | [E3](../evidencias/complementar/03-tres-disciplinas.png) |
| R5 | Selecionar preferência de turno | Tela "Período de preferência" | [E4](../evidencias/complementar/04-periodo-preferencia.png) |
| R6 | Fazer registro e login via Google | Login concluído | [E8](../evidencias/complementar/08-login-google.png) |
| R7 | Visualizar grade horária | Grade aberta em tamanho grande | [E34](../evidencias/complementar/34-r7-visualizar-grade-nuvem.png) |
| R8 | Salvar grade localmente | Grade em "Grades locais" | [E5](../evidencias/complementar/05-grade-local-salva.png) |
| R9 | Apagar grade horária local | Confirmação, exclusão e lista vazia após recarregar | [E6](../evidencias/complementar/06-r9-confirmacao-exclusao-local.png), [E7](../evidencias/complementar/07-r9-apos-exclusao.png) |
| R10 | Salvar grade na nuvem | "Grade salva com sucesso!" | [E10](../evidencias/complementar/10-r10-salva-na-nuvem.png), [E11](../evidencias/complementar/11-grades-nuvem.png) |
| R11 | Apagar grade horária na nuvem | Confirmação, exclusão e lista vazia após recarregar | [E35](../evidencias/complementar/35-r11-confirmacao-exclusao-nuvem.png), [E36](../evidencias/complementar/36-r11-apos-exclusao.png) |

Fonte: coleta complementar, Chrome 157 no Android 15.

**Achado sobre a R9.** A coleta mostrou que a exclusão de grade salva localmente **está implementada**: na tela "Suas Grades", cada grade local tem um ícone de lixeira, que pede confirmação ("A grade será deletada para sempre, tem certeza?") e remove a grade, que continua removida depois de recarregar a página. O mesmo comportamento foi observado no Chrome 157 do Windows 10, em 19/11/2026 entre 02h58 e 03h00, com a barra de endereço e o relógio do sistema visíveis nos prints ([E12](../evidencias/complementar/12-pc-r9-grades-locais.png), [E13](../evidencias/complementar/13-pc-r9-confirmacao.png), [E14](../evidencias/complementar/14-pc-r9-apos-exclusao.png), [versão do Chrome](../evidencias/complementar/00-pc-sobre-chrome.png)). No [código-fonte público do produto](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/main/web/app/components/SchedulePreview/SchedulePreview.tsx), a remoção de grades locais existe desde dezembro de 2023, e o arquivo não foi alterado depois de fevereiro de 2024; portanto, a função já existia durante a avaliação de outubro. O registro "não implementado" da M1 foi revisado em [Métricas de avaliação](Metricas.md), e a M1 passa a 11 de 11 funções (100%).

### 3.3. Cenários da M4 no celular

<font size="3"><p style="text-align: left">Tabela 3: Cenários de confiabilidade repetidos no Chrome do Android</p></font>

| Cenário | Execução | Resultado | Evidência |
| :--- | :--- | :--- | :--- |
| Repetição das operações principais | Dez buscas seguidas de disciplinas (19h40 a 19h42) e duas gerações de grade, uma anônima e uma com login | Sem falhas observáveis | [E15](../evidencias/complementar/15-m4-busca01-calculo.png) a [E24](../evidencias/complementar/24-m4-busca10-orientacao-objetos.png) |
| Persistência das grades salvas | Recarregar a tela "Suas Grades" com uma grade na nuvem | Grade mantida | [E25](../evidencias/complementar/25-m4-persistencia-apos-recarregar.png) |
| Uso contínuo | Sessão aberta de 18h29 a 19h45 | Sem travamento, erro ou saída automática da conta | Anotações da coleta |
| Acesso em diferentes sessões | Sair da conta, fechar a aba, abrir outra e entrar de novo | Grade de 18/11 mantida na nuvem | [E26](../evidencias/complementar/26-m4-apos-sair-anonimo.png), [E27](../evidencias/complementar/27-m4-nova-aba-tela-entrada.png), [E28](../evidencias/complementar/28-m4-novo-login-grade-nuvem.png) |

Fonte: coleta complementar, Chrome 157 no Android 15.

### 3.4. Situações da M6 no celular

<font size="3"><p style="text-align: left">Tabela 4: Situações de falha repetidas no Chrome do Android</p></font>

| Teste | Situação | Aviso exibido | Evidência |
| :---: | :--- | :--- | :--- |
| T1 | Buscar sem informar o período letivo | "Escolha o ano/período" | [E29](../evidencias/complementar/29-m6-t1-sem-periodo.png) |
| T2 | Selecionar a quinta turma de Cálculo 1 | "Você só pode escolher até 4 aulas da mesma disciplina!" | [E30](../evidencias/complementar/30-m6-t2-mais-de-4-turmas.png) |
| T3 | Buscar um termo sem resultado (`xyzqwerty`) | "Nenhuma disciplina encontrada" | [E31](../evidencias/complementar/31-m6-t3-sem-resultado.png) |
| T4 | Gerar grade com Qualidade de Software 1 (24M34) e Arquitetura e Desenho de Software (26M34), que coincidem na segunda-feira das 10h às 12h | "Não há horários disponíveis para a combinação de disciplinas selecionadas", com a sugestão de remover uma das duas | [E32](../evidencias/complementar/32-m6-t4-conflito-horario.png) |
| T5 | Buscar com o campo de matéria vazio | "Escreva no nome da disciplina" | [E33](../evidencias/complementar/33-m6-t5-sem-parametros.png) |

Fonte: coleta complementar, Chrome 157 no Android 15.

<font size="3"><p style="text-align: left">Autor(es): [Cauã Clemente](https://github.com/CauaoClemente), 2026.</p></font>

## 4. Relações discutidas

### 4.1. Adequação Funcional e Confiabilidade: conflito de horário

**Relação.** O mesmo comportamento do produto sustenta as duas características: ao gerar uma grade com disciplinas que não cabem juntas sem conflito de horário, o produto não gera a grade e avisa o usuário, indicando quais disciplinas remover. Para a Confiabilidade, isso é tolerância a falhas. Para a Adequação Funcional, isso protege a corretude da grade, que é parte da questão Q2.

**Evidência.** M6, teste T4, na coleta original ([evidência do teste T4](../evidencias/Impedir%20conflitos%20de%20horarios.png)) e na coleta complementar no celular (Tabela 4). O teste T2 registra também o limite de quatro turmas por disciplina, que é a regra de negócio do produto descrita na Fase 1.

**O que se pode afirmar.** Nos pares testados, o produto não gera uma grade com conflito de horário e explica o motivo ao usuário, no computador e no celular.

**O que não se pode afirmar.** Que todas as grades geradas automaticamente respeitam as restrições de horário. A M6 testou pares específicos de disciplinas; a correção das grades geradas não tem métrica própria, como registra a seção 4.1 do [Julgamento final](julgamento-final.md).

### 4.2. Adequação Funcional e Confiabilidade: salvar, recuperar e apagar grades

**Relação.** A persistência avaliada na Confiabilidade depende das funções de salvar e apagar avaliadas na Adequação Funcional: só é possível testar se uma grade continua disponível, ou continua removida, se o produto oferece essas funções.

**Evidência.** As funções R8 a R11 estão implementadas (Tabela 2). Na nuvem, a grade continuou disponível depois de recarregar a página e de trocar de sessão (Tabela 3). No armazenamento local, a exclusão (R9) continuou valendo depois de recarregar a página, no celular e no computador.

**O que se pode afirmar.** Para as grades na nuvem, salvar, recuperar e apagar funcionaram entre recarregamentos e sessões. Para as grades locais, salvar e apagar funcionaram, e a exclusão persistiu após recarregar.

**O que não se pode afirmar.** Se uma grade local **mantida** continua disponível depois de fechar o navegador. A coleta recarregou a página com grades na nuvem, mas não fechou o navegador com uma grade local salva.

### 4.3. Adequação Funcional e Portabilidade

**Relação.** A Portabilidade indica em quais ambientes as funções do produto podem ser usadas. Assim, o alcance dos resultados de Adequação Funcional depende dos ambientes em que essas funções foram verificadas.

**Evidência.** A M7 registra que o produto funcionou nos seis ambientes da matriz, com uma evidência por ambiente. Na coleta complementar, as 11 funções da M1 foram verificadas uma a uma no Chrome do Android (Tabela 2).

**O que se pode afirmar.** No Chrome do Android, as 11 funções da M1 estão disponíveis e funcionam como no computador. Nos outros cinco ambientes da M7, o produto funcionou, mas sem verificação função por função.

**O que não se pode afirmar.** Que a correção dos dados (M2) se repete em cada ambiente, e que as 11 funções funcionam nos outros cinco ambientes da M7.

### 4.4. Confiabilidade e Portabilidade

**Relação.** No ambiente móvel testado, os resultados de Confiabilidade foram os mesmos do computador: a Portabilidade do produto não trouxe falhas de confiabilidade nesse ambiente.

**Evidência.** No Chrome do Android, os quatro cenários da M4 foram concluídos sem falhas observáveis (Tabela 3), e as cinco situações da M6 foram comunicadas com aviso claro (Tabela 4), como na coleta original.

**O que se pode afirmar.** Para o Chrome do Android, a ausência de falhas (M4) e o tratamento de entradas inválidas (M6) se mantêm.

**O que não se pode afirmar.** Que isso vale para os outros cinco ambientes da M7, que não repetiram os cenários. A disponibilidade (M5) não foi repetida, porque depende do servidor do produto e exige observação em vários dias.

### 4.5. Dependências externas

**Relação.** O login Google e os dados do SIGAA atravessam a Adequação Funcional e a Confiabilidade: o login é uma função da M1 (R6), uma tarefa da M3 e a condição do cenário de sessões da M4; os dados do SIGAA são a referência da M2.

**Evidência.** O login funcionou no computador e no celular, inclusive ao trocar de sessão (Tabela 3).

**O que não se pode afirmar.** Como uma falha nesses serviços afetaria cada característica. Nenhuma métrica simulou indisponibilidade do login Google ou dados desatualizados do SIGAA, e esse tipo de teste não pode ser feito no produto em produção. Esta relação é declarada como **sem dados suficientes**.

### 4.6. Síntese

<font size="3"><p style="text-align: left">Tabela 5: Síntese das relações entre as características</p></font>

| Nº | Características | Relação observada | Métricas | Situação |
| :---: | :--- | :--- | :--- | :--- |
| 1 | Adequação Funcional e Confiabilidade | O aviso de conflito impede a geração de grades com conflito nos pares testados | M6 (T2, T4) e Q2 | Sustentada no computador e no celular; grades geradas em geral não verificadas |
| 2 | Adequação Funcional e Confiabilidade | Salvar, recuperar e apagar grades persistem entre recarregamentos e sessões | M1 (R8 a R11) e M4 | Sustentada na nuvem; no armazenamento local, sem teste de fechar o navegador |
| 3 | Adequação Funcional e Portabilidade | As 11 funções funcionam fora do navegador de referência | M1 e M7 | Sustentada no Chrome do Android; parcial nos outros cinco ambientes |
| 4 | Confiabilidade e Portabilidade | Sem falhas de confiabilidade no ambiente móvel testado | M4, M6 e M7 | Sustentada no Chrome do Android; sem dados nos outros cinco ambientes |
| 5 | Dependências externas (login Google e SIGAA) | Não estabelecida | M1 (R6), M2, M3 e M4 | Sem dados suficientes |

Fonte: [Métricas de avaliação](Metricas.md), [Julgamento final da qualidade](julgamento-final.md) e seção 3 desta página.

<font size="3"><p style="text-align: left">Autor(es): [Cauã Clemente](https://github.com/CauaoClemente), 2026.</p></font>

## 5. Limitações

- **Resultados sem variação:** as sete métricas ficaram em 100%. Sem variação, não é possível observar se a piora de uma característica acompanha a de outra, nem medir a força de qualquer relação.
- **Amostras pequenas:** cinco disciplinas, quatro cenários de confiabilidade, cinco situações de falha e seis ambientes, mais um ambiente repetido na coleta complementar. As relações valem para essas amostras, conforme a seção 6 do [Julgamento final](julgamento-final.md).
- **Datas diferentes:** a coleta complementar foi feita em 18 e 19/11/2026, quase um mês depois das medições originais. O código público do produto não mudou nesse intervalo, mas não há como confirmar que a versão em produção era idêntica.
- **Um avaliador e um aparelho:** a coleta complementar foi feita por um integrante, em um celular. Ela não substitui a revisão por outro avaliador.
- **Repetição reduzida:** no cenário de repetição, as buscas foram repetidas dez vezes, mas a geração e o salvamento de grades foram feitos duas vezes.
- **Avaliação externa:** a avaliação é de caixa-preta, pela interface em produção. As relações descrevem comportamentos observados, não as causas internas no código.

## 6. Implicações para as próximas avaliações

As relações ainda parciais indicam o que uma nova avaliação precisaria medir:

- registrar o navegador e o dispositivo de cada coleta, e, na M7, a lista de funções verificadas em cada ambiente;
- repetir os cenários da M4 e da M6 nos demais ambientes da matriz da M7;
- incluir um cenário que feche o navegador com uma grade local salva;
- verificar se as grades geradas automaticamente respeitam as restrições de horário em mais combinações de disciplinas.

Esses pontos complementam a oportunidade de ampliar a cobertura dos testes, descrita em [Oportunidades de melhoria](oportunidades-de-melhoria.md).

---

## Bibliografia

> 1. ISO/IEC 25010:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. 2011.

> 2. RAMOS, Cristiane Soares. *Processo de Avaliação de Produto de Software*. Material da disciplina Qualidade de Software 1. Universidade de Brasília (UnB), 2026.

> 3. UNB-MDS. *Sua Grade UnB*: código-fonte. GitHub, 2023-2026. Disponível em: <https://github.com/unb-mds/2023-2-SuaGradeUnB>.

## Histórico de Versão

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :----: | :--- | :--- | :---: | :--- | :---: |
| 1.0 | Discussão das relações entre as características de qualidade, com a coleta complementar de 18 e 19/11/2026 | [Cauã Clemente](https://github.com/CauaoClemente) | 19/11/2026 | | |
