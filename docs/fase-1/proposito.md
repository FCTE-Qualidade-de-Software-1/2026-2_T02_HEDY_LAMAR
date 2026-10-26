# 2.1 Propósito da Avaliação

## Introdução

Este artefato descreve por que o **Sua Grade UnB** está sendo avaliado, para quem e quais decisões os resultados vão apoiar. O Sua Grade UnB é uma aplicação web livre (licença MIT), criada na disciplina Métodos de Desenvolvimento de Software da UnB, que ajuda estudantes a montar suas grades horárias. O produto está em <https://suagradeunb.com.br>.

A avaliação segue a série **ISO/IEC 25000 (SQuaRE)** e foca nas características de **Adequação Funcional**, **Confiabilidade** e **Portabilidade**, conforme o modelo da ISO/IEC 25010:2011.

## 2.1.1 Propósito da avaliação e uso pretendido

O propósito é identificar pontos de melhoria em Adequação Funcional, Confiabilidade e Portabilidade do Sua Grade UnB, para apoiar a priorização de correções e evoluções do produto.

## 2.1.2 Por que avaliar?

Montar a grade do semestre é uma tarefa recorrente e com consequências: uma turma errada ou desatualizada leva o estudante a planejar o semestre sobre informação incorreta. O produto resolve essa tarefa, e a documentação do projeto indica dois pontos que merecem atenção:

- Dados dependentes de uma atualização manual: As turmas vêm de *web scraping* da página pública de turmas do SIGAA. Segundo a documentação, a equipe de desenvolvimento executa a atualização manualmente e tenta repeti-la a cada 24 h. A frequência real de atualização hoje não foi confirmada (OBS: Não há rastros no repositório que indiquem a automação).
- Dependência de serviços externos: O login usa a conta Google (OAuth), e o frontend e a API ficam em plataformas de hospedagem distintas (Vercel e Heroku).

Esses pontos tornam a corretude dos dados, a disponibilidade e o comportamento diante de falhas externas os riscos mais prováveis, o que orienta a escolha das três características.

## 2.1.3 Para quem avaliar?

- Equipe mantenedora do produto (requisitante e decisora).Recebe o relatório da equipe de avaliação e decide o que corrigir. Essa atribuição de papel é uma premissa da avaliação, adotada pela equipe porque não há um requisitante formal. Ela depende de a equipe ainda manter o projeto. O último commit no repositório é de 15/02/2026, uma correção no *web scraping*, o que indica manutenção recente.
- Estudantes da UnB (beneficiários). Usam o produto e se beneficiam das correções.
- Equipe de avaliação e professora da disciplina. A primeira executa a avaliação e a segunda avalia o processo. Nenhuma das duas é usuária do produto.

## 2.1.4 Como os resultados serão utilizados?

Os resultados servirão a três decisões, que cabem à equipe mantenedora. A equipe de avaliação produz as recomendações; a decisão de implementá-las é da equipe mantenedora.


<font size="3"><p style="text-align: left">Tabela 1: Decisões a serem apoiadas</p></font>

| Nº | Decisão apoiada | Característica | Evidência a produzir | Quem decide |
| :---: | :--- | :--- | :--- | :--- |
| 1 | Quais divergências entre os dados do produto e a página pública de turmas do SIGAA, e quais conflitos de horário em grades geradas, corrigir primeiro | Adequação Funcional | Comparação dos dados com o SIGAA e verificação das grades geradas | Equipe mantenedora |
| 2 | Se a atualização dos dados de turmas, manual segundo a documentação, deve ser automatizada ou monitorada | Adequação Funcional e Confiabilidade | Defasagem observada dos dados e falhas durante o uso normal | Equipe mantenedora |
| 3 | Quais navegadores, sistemas operacionais e tamanhos de tela passam a ser suportados e testados de forma sistemática | Portabilidade | Matriz de funcionamento por ambiente | Equipe mantenedora |

Autor(es):  [João Vitor](https://github.com/Jauzimm), 2026.

## Bibliografia

> 1. RAMOS, Cristiane Soares. *Processo de Avaliação de Produto de Software*. Material da disciplina Qualidade de Software 1. Universidade de Brasília (UnB), 2026.

> 2. EQUIPE SUA GRADE UNB. *Sua Grade UnB: repositório do projeto no GitHub*. Disponível em: <https://github.com/unb-mds/2023-2-SuaGradeUnB>. Acesso em: 17 out. 2026.

> 3. EQUIPE SUA GRADE UNB. *Arquitetura*. In: Docs - Sua Grade UnB. Disponível em: <https://unb-mds.github.io/2023-2-SuaGradeUnB/architecture/>. Acesso em: 17 out. 2026.

## Histórico de Versão

| Versão |          Descrição          |                       Autor                       |    Data    |                       Revisor                       | Data de revisão |
| :----: | :-------------------------: | :-----------------------------------------------: | :--------: | :-------------------------------------------------: | :-------------: |
|  1.0   |       Versão Inicial        |     [João Vitor](https://github.com/Jauzimm)      | 18/10/2026 | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 26/10/2026  |