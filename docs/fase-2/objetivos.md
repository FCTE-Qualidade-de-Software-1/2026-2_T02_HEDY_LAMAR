# 3.1 Objetivos, Questões e Hipóteses de Medição

## Introdução

Este artefato define os objetivos de medição, as questões e as hipóteses da avaliação de qualidade do **Sua Grade UnB**, utilizando o método Goal–Question–Metric (GQM). O objetivo é estabelecer uma relação rastreável entre as necessidades identificadas na Fase 1 e as informações que deverão ser obtidas durante a avaliação.

A definição dos objetivos considera o propósito da avaliação, as necessidades das partes interessadas e as características de qualidade priorizadas na página [2.5 Modelo de Qualidade](modelo.md): Adequação Funcional, Confiabilidade e Portabilidade, conforme a ISO/IEC 25010:2011.

A avaliação será realizada externamente, por meio da interface do produto em produção, caracterizando uma abordagem de caixa-preta. As hipóteses apresentadas representam expectativas a serem verificadas durante a coleta de dados, não resultados já obtidos.

## 3.1.1 Objetivos de medição — Nível conceitual

Os objetivos foram definidos a partir da estrutura GQM, considerando o objeto de estudo, o propósito da medição, o foco de qualidade, o ponto de vista e o contexto da avaliação.

### Objetivo G1 — Adequação Funcional

- **Analisar:** o Sua Grade UnB.
- **Com o propósito de:** identificar deficiências funcionais e oportunidades de melhoria.
- **Com respeito a:** Adequação Funcional, considerando completude funcional, corretude funcional e adequação funcional.
- **Do ponto de vista:** da equipe mantenedora, responsável por decidir quais correções e evoluções devem ser priorizadas.
- **No contexto de:** uso do produto em produção por estudantes da UnB, com avaliação externa das funções de busca, seleção de turmas, geração, salvamento e exportação de grades.

Este objetivo busca verificar se as funções necessárias à tarefa principal estão disponíveis, se os dados e as grades produzidas estão corretos e se as funções permitem realizar as tarefas previstas.

### Objetivo G2 — Confiabilidade

- **Analisar:** o Sua Grade UnB.
- **Com o propósito de:** identificar falhas operacionais e avaliar a disponibilidade do produto durante o uso.
- **Com respeito a:** Confiabilidade, considerando maturidade, disponibilidade e tolerância a falhas.
- **Do ponto de vista:** da equipe mantenedora, responsável por priorizar correções que reduzam interrupções e falhas de funcionamento.
- **No contexto de:** execução dos fluxos principais do produto, durante uma janela de observação definida, considerando a dependência de serviços externos, como o login Google, e de dados provenientes do SIGAA.

Este objetivo busca verificar a ocorrência de falhas durante a operação normal, a possibilidade de acessar o produto quando necessário e seu comportamento diante de entradas inválidas ou problemas em dependências externas.

### Objetivo G3 — Portabilidade

- **Analisar:** o Sua Grade UnB.
- **Com o propósito de:** identificar limitações de funcionamento em diferentes ambientes de uso.
- **Com respeito a:** Portabilidade, considerando adaptabilidade e instalabilidade conforme o modelo de qualidade adotado na Fase 1.
- **Do ponto de vista:** da equipe mantenedora, responsável por definir os ambientes nos quais o produto deve ser testado e suportado.
- **No contexto de:** acesso à aplicação web por diferentes navegadores, sistemas operacionais e tamanhos de tela, utilizando os recursos de acesso previstos para o produto.

Este objetivo busca verificar se as funções principais continuam operacionais em diferentes ambientes e se o acesso ao produto exige alguma instalação adicional.

## 3.1.2 Questões de medição — Nível operacional

As questões foram derivadas dos objetivos de medição e organizadas de acordo com as características e subcaracterísticas de qualidade selecionadas. Cada questão representa um aspecto que deverá ser investigado por meio de evidências coletadas durante a avaliação.

### Questões do objetivo G1 — Adequação Funcional

**Q1. Completude funcional:** As funções previstas para a realização da tarefa principal estão disponíveis e podem ser executadas pelo usuário?

A questão abrange a busca e seleção de disciplinas, preferência do turno, a geração de grades, o salvamento e a exportação, e acesso através do google.

**Q2. Corretude funcional:** Os dados das turmas apresentados pelo produto correspondem aos dados de referência do SIGAA, e as grades geradas respeitam as restrições de horários e de disciplinas?

A questão considera a correspondência de informações como códigos, horários, salas e docentes, além da ausência de conflitos de horário e de disciplinas repetidas nas grades geradas.

**Q3. Adequação funcional:** As funções disponíveis permitem concluir a tarefa de montar uma grade horária e salvá-la ou exportá-la conforme o comportamento esperado?

A questão investiga se o conjunto de funções atende à tarefa principal definida para o produto, sem considerar como funcionalidade do site operações realizadas exclusivamente por ferramentas externas.

### Questões do objetivo G2 — Confiabilidade

**Q4. Maturidade:** Com que frequência ocorrem falhas durante a execução normal dos fluxos principais do produto?

A questão busca identificar interrupções, erros inesperados e operações que não são concluídas nas condições de uso previstas.

**Q5. Disponibilidade:** Em que proporção das tentativas de acesso observadas o produto está acessível e permite iniciar a tarefa principal?

A questão considera a acessibilidade do produto durante a janela de observação definida, registrando as tentativas realizadas e as falhas verificadas.

**Q6. Tolerância a falhas:** O produto mantém um comportamento controlado diante de entradas inválidas ou de falhas em dependências externas, sem comprometer indevidamente a operação em andamento?

A questão investiga o comportamento observável do sistema nessas condições, incluindo mensagens de erro, interrupções e preservação do estado da operação quando aplicável. Os testes devem respeitar os limites de acesso e não provocar situações de risco em produção.

### Questões do objetivo G3 — Portabilidade

**Q7. Adaptabilidade:** As funções principais do Sua Grade UnB operam corretamente nos diferentes navegadores, sistemas operacionais e tamanhos de tela selecionados para a avaliação?

A questão considera a execução dos fluxos principais em uma matriz de ambientes definida previamente, permitindo identificar incompatibilidades ou limitações específicas.

Considerando que o Sua Grade UnB é uma aplicação web, não se pressupõe a existência de instalação como aplicativo. O acesso pelo navegador será considerado de acordo com o funcionamento efetivamente oferecido pelo produto.

## 3.1.3 Hipóteses de medição — Nível operacional

As hipóteses expressam os comportamentos esperados para cada questão e deverão ser confrontadas com os dados coletados. Sua formulação permite orientar a interpretação das evidências, sem antecipar o julgamento final da qualidade do produto.

### Hipóteses do objetivo G1 — Adequação Funcional

**H1 — Completude funcional (Q1):** Espera-se que as funções previstas pelo story map estejam disponíveis e possam ser executadas nos modos de acesso aplicáveis. A hipótese será contrariada se uma função prevista estiver ausente ou não puder ser concluída nas condições de avaliação.

**H2 — Corretude funcional (Q2):** Espera-se que os dados das turmas examinadas correspondam às informações de referência do SIGAA e que as grades geradas respeitem as restrições de horário e de disciplinas. Divergências nos dados ou grades com conflitos e repetições constituirão evidências contrárias à hipótese.

**H3 — Adequação funcional (Q3):** Espera-se que as funções disponíveis permitam concluir a tarefa principal conforme o comportamento especificado para o produto. A hipótese será contrariada quando limitações funcionais impedirem a conclusão da tarefa ou exigirem procedimentos externos não previstos como parte do fluxo do sistema.

### Hipóteses do objetivo G2 — Confiabilidade

**H4 — Maturidade (Q4):** Espera-se que os fluxos principais sejam executados sem falhas inesperadas nas condições normais de uso. A ocorrência de falhas durante as execuções fornecerá evidências contrárias à hipótese, cuja relevância deverá ser interpretada conforme a frequência e o impacto observados.

**H5 — Disponibilidade (Q5):** Espera-se que o produto esteja acessível na maior parte das tentativas realizadas durante a janela de observação. Indisponibilidades recorrentes ou falhas que impeçam o início da tarefa fornecerão evidências contrárias à hipótese. O nível de disponibilidade considerado aceitável deverá ser estabelecido na definição das métricas e dos critérios de julgamento.

**H6 — Tolerância a falhas (Q6):** Espera-se que entradas inválidas e falhas em dependências externas sejam tratadas de forma controlada, com comunicação adequada do problema e sem perda indevida do estado da operação. Comportamentos inesperados, interrupções indevidas ou perda de dados observável fornecerão evidências contrárias à hipótese.

### Hipóteses do objetivo G3 — Portabilidade

**H7 — Adaptabilidade (Q7):** Espera-se que as funções principais permaneçam operacionais nos ambientes selecionados para a avaliação. Diferenças de comportamento que impeçam a execução dos fluxos previstos em algum dos ambientes fornecerão evidências contrárias à hipótese.


## 3.1.4 Rastreabilidade entre objetivos, questões e hipóteses

A tabela a seguir resume a relação entre os elementos GQM definidos neste artefato.

| Objetivo | Característica de qualidade | Questão | Hipótese |
| :--- | :--- | :--- | :--- |
| G1 | Adequação Funcional | Q1 — Completude funcional | H1 |
| G1 | Adequação Funcional | Q2 — Corretude funcional | H2 |
| G1 | Adequação Funcional | Q3 — Adequação funcional | H3 |
| G2 | Confiabilidade | Q4 — Maturidade | H4 |
| G2 | Confiabilidade | Q5 — Disponibilidade | H5 |
| G2 | Confiabilidade | Q6 — Tolerância a falhas | H6 |
| G3 | Portabilidade | Q7 — Adaptabilidade | H7 |

Essa hierarquia estabelece a base para a próxima etapa do GQM: a seleção das métricas que permitirão responder às questões. Para cada métrica, deverão ser especificados sua definição, o procedimento de cálculo, a fonte dos dados, o procedimento de coleta e os critérios de interpretação. Os níveis de pontuação e os critérios de julgamento deverão ser definidos antes da análise dos resultados.

## Bibliografia

> 1. RAMOS, Cristiane Soares. *Processo de Avaliação de Produto de Software*. Material da disciplina Qualidade de Software 1. Universidade de Brasília (UnB), 2026.

> 2. ISO/IEC 25010:2011. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. 2011.

## Histórico de Versão

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1.0 | Versão inicial dos objetivos, questões e hipóteses de medição | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 21/10/2026 |   |  |
| 1.1 | Remoção de instalabilidade | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 21/10/2026 |   |  |
