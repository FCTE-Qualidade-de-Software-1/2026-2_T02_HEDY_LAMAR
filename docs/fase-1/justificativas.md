# 2.4 Justificativas

## 2.4.1 Por que o Sua Grade UnB?

### Um produto real, em uso e com público próximo

O Sua Grade UnB está em produção e atende uma tarefa concreta de estudantes da UnB, o mesmo público da equipe de avaliação. Isso permite validar as necessidades dos usuários primários e interpretar o uso do produto com conhecimento do contexto.

### Evidências públicas para fundamentar a avaliação

O produto é software livre (licença MIT), com repositório público e documentação de arquitetura. Isso permite caracterizá-lo com fontes verificáveis, e separar o que está confirmado do que ainda precisa de verificação.

### Riscos de qualidade observáveis de fora

O produto depende de uma atualização manual de dados e de serviços externos (login Google, SIGAA, hospedagem). Esses pontos geram falhas que um avaliador consegue observar pela interface, sem acesso ao código: dados divergentes, indisponibilidade e comportamento diante de falhas externas.

## 2.4.2 Por que estas três características?

A escolha de Adequação Funcional, Confiabilidade e Portabilidade vem da matriz de impacto por risco.

- **Adequação Funcional.** É o núcleo do produto: o valor está em mostrar turmas corretas e gerar grades sem conflito. Os dados vêm de *scraping* manual, e a correção da geração de grades ainda não foi verificada.
- **Confiabilidade.** O produto depende de login externo, de hospedagem e de atualização manual. Se estiver fora do ar ou falhar diante de uma entrada inválida, o estudante perde a tarefa.
- **Portabilidade.** Estudantes acessam de dispositivos variados (premissa da equipe), e uma matriz de navegadores, sistemas e telas é viável de medir de fora.

## 2.4.3 Por que uma avaliação externa?

A avaliação é de caixa-preta porque a equipe de avaliação não tem acesso ao banco de dados nem à infraestrutura do produto, e o código público no GitHub pode não corresponder exatamente à versão em produção. Por isso as medições são feitas pela interface; o código foi consultado só para descrever o produto. Isso é coerente com o objetivo, que é apoiar decisões da equipe mantenedora a partir do que o usuário observa, e define os limites do que pode ser medido.

## 2.4.4 Estruturação da medição

Na Fase 2, as medidas serão definidas pelo método **GQM (Goal-Question-Metric)**, com base na série ISO/IEC 25000. Para garantir coerência entre as fases, a Fase 1 fixou as decisões abaixo, citadas pelo identificador nos demais documentos.

<font size="3"><p style="text-align: left">Tabela 1: Decisões que alimentam a Fase 2</p></font>

| ID | Decisão | Valor |
| :---: | :--- | :--- |
| D1 | Subcaracterísticas de Adequação Funcional | Completude funcional, corretude funcional e adequação funcional |
| D2 | Subcaracterísticas de Confiabilidade | Maturidade, disponibilidade e tolerância a falhas |
| D3 | Subcaracterísticas de Portabilidade | Adaptabilidade e instalabilidade |
| D4 | Fora do escopo | Recuperabilidade e substituibilidade |
| D5 | Modelo-base | ISO/IEC 25010:2011 |

Autor(es):  [João Vitor](https://github.com/Jauzimm), 2026.

## Bibliografia

> 1. ISO/IEC 25010:2011. *Systems and software engineering: SQuaRE: System and software quality models*.

> 2. RAMOS, Cristiane Soares. *Processo de Avaliação de Produto de Software*. Material da disciplina Qualidade de Software 1. Universidade de Brasília (UnB), 2026.

> 3. EQUIPE SUA GRADE UNB. *Sua Grade UnB: repositório do projeto no GitHub*. Disponível em: <https://github.com/unb-mds/2023-2-SuaGradeUnB>. Acesso em: 17 out. 2026.

## Histórico de Versão

| Versão |          Descrição          |                       Autor                       |    Data    |                       Revisor                       | Data de revisão |
| :----: | :-------------------------: | :-----------------------------------------------: | :--------: | :-------------------------------------------------: | :-------------: |
|  1.0   |       Versão Inicial        |     [João Vitor](https://github.com/Jauzimm)      | 18/10/2026 | [Caua Clemente](https://github.com/CauaoClemente) |   |