# Métricas de avaliação

Este documento descreve as métricas selecionadas para avaliar a qualidade do **Sua Grade UnB**, relacionando cada métrica às questões de medição definidas pelo método Goal–Question–Metric (GQM). Para cada métrica, são apresentados sua definição, seu procedimento de cálculo, a fonte dos dados e o procedimento de coleta.

As métricas estão organizadas de acordo com as questões de medição. Os critérios detalhados de julgamento são apresentados em `criterios-julgamento.md`.

## 1. Adequação funcional

### M1 — Completude funcional

**Questão relacionada:** Qual é a proporção das funcionalidades planejadas que está implementada no produto?

**Definição:** Mede a proporção de funcionalidades previstas no *story map* que estão implementadas no Sua Grade UnB. A avaliação considera o planejamento registrado no *story map*, em vez de se limitar às funcionalidades encontradas durante a inspeção do produto.

**Fórmula:**

```text
C_f = (F_i / F_p) * 100
```

Em que:

- `C_f`: completude funcional, em porcentagem;
- `F_i`: número de funcionalidades planejadas que estão implementadas;
- `F_p`: número total de funcionalidades planejadas.

**Fonte dos dados:** [Story map](https://miro.com/app/board/uXjVNYnku7s=/?share_link_id=596015837126) do projeto e inspeção das funcionalidades disponíveis no produto avaliado.

**Procedimento de coleta:**

1. Identificar as funcionalidades previstas no *story map*.
2. Verificar, no produto, se cada funcionalidade está implementada.
3. Registrar cada funcionalidade como implementada ou não implementada, mantendo evidências que permitam verificar a classificação.
4. Contabilizar as funcionalidades implementadas e o total de funcionalidades planejadas.
5. Aplicar a fórmula e registrar o resultado.

Na contagem, cada funcionalidade considerada deve corresponder a uma unidade identificável no planejamento. Temas e agrupamentos do *story map* não devem ser contabilizados como funcionalidades adicionais quando apenas agrupam outras funcionalidades.

**Resultado obtido:**

Foram identificadas 11 funcionalidades planejadas, das quais 10 estão implementadas. A funcionalidade ausente identificada foi a possibilidade de apagar uma grade horária salva localmente diretamente pelo produto. Excluir manualmente um arquivo pelo sistema operacional não foi considerado equivalente, pois essa ação não é oferecida pelo produto como funcionalidade própria.

```text
C_f = (10 / 11) * 100 ≈ 90,91%
```
| ID | Requisito | Evidência |
| :---: | :--- | :--- |
| R1 | Criar grade horária | [E1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Gerar%20grades%20validas.png) |
| R2 | Filtrar matéria em uma lista pré-definida | [E2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Sele%C3%A7%C3%A3o%20de%20mat%C3%A9ria.png) |
| R3 | Selecionar uma turma em uma lista | [E3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Sele%C3%A7%C3%A3o%20de%20mat%C3%A9ria.png) |
| R4 | Adicionar matéria selecionada | [E4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Materia%20selecionada.png) |
| R5 | Selecionar preferência de turno | [E5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Escolher%20preferencia%20de%20turno.png) |
| R6 | Fazer registro e login via Google | [E6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Cadastro%20atrav%C3%A9s%20do%20google.png) |
| R7 | Visualizar grade horária | [E7](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Visualizar%20grade%20horaria.png) |
| R8 | Salvar grade localmente | [E8](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Salvar%20grade%20localmente.png) |
| R9 | Apagar grade horária local | Não implementado |
| R10 | Salvar grade na nuvem | [E10](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Salvar%20grades%20remotamente.png) |
| R11 | Apagar grade horária na nuvem | [E11](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Salvar%20grades%20remotamente.png) |

**Interpretação:** o resultado indica que 90,91% das funcionalidades identificadas no planejamento estão implementadas. O julgamento de adequação desse resultado deve seguir os critérios definidos em `criterios-julgamento.md`.

### M2 — Correção funcional

**Questão relacionada:** Qual é a proporção das informações acadêmicas exibidas pelo Sua Grade UnB que corresponde às informações registradas no SIGAA?

**Definição:** Mede a proporção dos atributos acadêmicos verificados no Sua Grade UnB que correspondem aos dados registrados no SIGAA. Nesta avaliação, foram comparados o nome do professor, a localização da turma e o horário de cinco disciplinas. A disciplina e sua turma devem ser identificadas de forma correspondente nos dois sistemas para que a comparação seja válida.

**Fórmula:**

```text
C_c = (A_c / A_v) * 100
```

Em que:

- `C_c`: proporção de atributos acadêmicos corretos, em porcentagem;
- `A_c`: número de atributos verificados que correspondem aos dados do SIGAA;
- `A_v`: número total de atributos verificados.

**Fonte dos dados:** informações exibidas pelo Sua Grade UnB e registros correspondentes no SIGAA, considerando a mesma disciplina, turma e período letivo.

**Procedimento de coleta:**

1. Selecionar disciplinas e turmas exibidas pelo Sua Grade UnB.
2. Consultar no SIGAA os dados correspondentes de cada turma.
3. Comparar individualmente o professor, a localização e o horário exibidos pelos dois sistemas.
4. Registrar cada comparação como correta ou incorreta e associar a evidência que permita verificar os dados em ambos os sistemas.
5. Contabilizar os atributos corretos e o total de atributos verificados e aplicar a fórmula.

**Resultado obtido:** foram verificadas cinco disciplinas, comparando três atributos de cada uma — professor, localização e horário —, totalizando 15 atributos. Todos correspondiam às informações consultadas no SIGAA.

```text
C_c = (15 / 15) * 100 = 100%
```

| Disciplina | Professor | Local | Horário | Resultado | Evidência |
| :--- | :--- | :---: | :---: | :---: | :--- |
| Física 1 | Lindomar | I3 | 35M12 | Correto | [E1]() |
| Banco de Dados 2 | Vandor | I10 | 35T34 | Correto | [E2]() |
| Qualidade de Software | Cristiane | S6 | 24M34 | Correto | [E3]() |
| Arquitetura e Desenho de Software | Milene | S4 | 26M12 | Correto | [E4]() |
| Ciências Aeroespaciais | Gabriela | S5 | 35M34 | Correto | [E5]() |

**Interpretação:** o resultado de 100% indica que os 15 atributos verificados — professor, local e horário para cada uma das cinco disciplinas — corresponderam aos dados consultados no SIGAA. A conclusão limita-se à amostra e ao momento da verificação; não garante que todas as informações do sistema estejam corretas ou que permaneçam atualizadas após alterações no SIGAA.

### M3 — Adequação às tarefas dos usuários

**Questão relacionada:** Qual é a proporção das tarefas avaliadas que pode ser atendida adequadamente pelo produto?

**Definição:** Mede a proporção das tarefas selecionadas para avaliação que são atendidas pelas funcionalidades disponíveis e permitem alcançar o objetivo definido para cada tarefa.

**Fórmula:**

```text
A_f = (T_a / T_p) * 100
```

Em que:

- `A_f`: adequação funcional às tarefas avaliadas;
- `T_a`: número de tarefas consideradas adequadamente atendidas;
- `T_p`: número total de tarefas avaliadas.

**Fonte dos dados:** tarefas identificadas no planejamento do produto, objetivos esperados para cada tarefa e evidências da avaliação funcional.

**Procedimento de coleta:**

1. Selecionar tarefas representativas do uso do Sua Grade UnB.
2. Definir o objetivo de cada tarefa e as condições para considerá-la adequadamente atendida.
3. Executar ou inspecionar as funcionalidades relacionadas às tarefas.
4. Classificar cada tarefa conforme os critérios previamente estabelecidos.
5. Calcular a proporção de tarefas adequadamente atendidas.

Descrição da coleta: foram identificadas as tarefas disponíveis no sistema e analisada a relação de cada uma delas com o objetivo principal do serviço: gerar grades horárias e salvá-las na nuvem.


Fonte dos dados: funcionalidades disponíveis no sistema e objetivo proposto para o serviço.

Resultado obtido: foram identificadas cinco tarefas: realizar login com Google para permitir o salvamento de grades na nuvem, buscar matérias, selecionar turmas, gerar grades horárias e gerenciar grades (salvar e excluir). Todas essas tarefas contribuem para o funcionamento do serviço e estão relacionadas ao seu objetivo principal.

**Fórmula:**

```text
A_f = (5 / 5) * 100 = 100%
```

**Interpretação:** considerando as tarefas identificadas, todas estão alinhadas ao objetivo proposto para o sistema. Portanto, as tarefas avaliadas apresentam adequação funcional em relação à finalidade do serviço.

## 2. Confiabilidade

### M4 — Maturidade

**Questão relacionada:** Qual é a proporção dos cenários de teste de confiabilidade avaliados que são concluídos sem falhas observáveis?

**Definição:** Mede a proporção de cenários de teste de confiabilidade concluídos sem falhas observáveis, considerando a repetição das operações principais, a persistência das grades salvas, o uso contínuo do sistema e o acesso aos dados em diferentes sessões.

**Fórmula:**

```text
M_c = (C_s / C_t) * 100
```

Em que:

- `M_c`: proporção de cenários de confiabilidade concluídos sem falhas;
- `C_s`: número de cenários concluídos sem falhas observáveis;
- `C_t`: número total de cenários de confiabilidade avaliados.

**Fonte dos dados:** Resultados observados e evidências de falhas durante a utilização do Sua Grade UnB.

**Procedimento de coleta:**

1. Definir os cenários de teste de confiabilidade e suas condições de execução.
2. Executar testes de repetição das operações principais, persistência das grades salvas, uso contínuo e acesso em diferentes sessões.
3. Registrar os resultados observados em cada cenário, incluindo eventuais falhas.
4. Classificar cada cenário como concluído sem falhas ou concluído com falhas.
5. Calcular a proporção de cenários concluídos sem falhas em relação ao total avaliado.

Descrição da coleta: Foram executados quatro cenários de teste:

| Cenário de teste | Descrição | Resultado |
| :--- | :--- | :--- |
| Repetição das operações principais | Realizar buscas de disciplinas, selecionar turmas, gerar grades e salvá-las na nuvem repetidamente, verificando a ocorrência de falhas. | Sem falhas observáveis |
| Persistência das grades salvas | Salvar grades e verificar se continuam disponíveis após navegar pelo sistema e recarregar a página. | Sem falhas observáveis |
| Uso contínuo | Utilizar o sistema durante um período contínuo, observando possíveis interrupções ou falhas inesperadas. | Sem falhas observáveis |
| Acesso em diferentes sessões | Realizar login com uma conta Google, salvar uma grade, encerrar a sessão, autenticar-se novamente e verificar se a grade continua acessível. | Sem falhas observáveis |

**Resultado obtido:** Os quatro cenários de teste foram concluídos sem falhas observáveis. Portanto, considerando os quatro cenários avaliados, o resultado foi:

```text
M_c = (4 / 4) * 100 = 100%
```

**Interpretação:** O resultado de 100% indica que todos os cenários de confiabilidade avaliados foram concluídos sem falhas observáveis. Esse resultado é favorável à confiabilidade do Sua Grade UnB nas condições testadas. Entretanto, a métrica considera a proporção de cenários aprovados, e não a frequência de falhas em todas as possíveis execuções do sistema. Portanto, o resultado não garante que o software esteja livre de falhas em situações não avaliadas.

### M5 — Disponibilidade observada

**Questão relacionada:** Qual é a proporção das verificações programadas em que o produto está acessível e permite executar a operação funcional selecionada?

**Definição:** Mede a proporção das verificações programadas em que o produto pode ser acessado e a operação selecionada para o teste pode ser executada conforme o resultado esperado.

**Fórmula:**

```text
D = (V_s / V_t) * 100
```

Em que:

- `D`: disponibilidade observada nas verificações;
- `V_s`: número de verificações bem-sucedidas;
- `V_t`: número total de verificações realizadas.

**Fonte dos dados:** registros de acesso ao produto, resultados dos testes e evidências coletadas durante as verificações.

**Procedimento de coleta proposto:**

1. Realizar verificações em horários predefinidos durante cinco dias consecutivos, distribuindo-as entre manhã, tarde e noite, totalizando 15 verificações.
2. Em cada verificação, testar o acesso ao produto e criar uma serie grade.
3. Registrar data, horário, resultado e evidência.
4. Investigar problemas de conexão ou outras condições externas que possam comprometer a interpretação do resultado.
5. Calcular a proporção de verificações bem-sucedidas.

| Dia | Manhã | Tarde | Noite | Evidências |
| :---: | :---: | :---: | :---: | :--- |
| Dia 1 | Ativo | Ativo | Ativo | [E1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-19%2014h%2023m.png), [E2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-19%2019h%2016m.png), [E3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-19%209h%2022m.png) |
| Dia 2 | Ativo | Ativo | Ativo | [E4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-20%2010h%2017m.png), [E5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-20%2013h%2040m.png), [E6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-20%2023h%2040m.png) |
| Dia 3 | Ativo | Ativo | Ativo | [E7](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-21%2012h%2013m.png), [E8](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-21%2013h%2020m.png), [E9](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-21%2020h%2020m.png) |
| Dia 4 | Ativo | Ativo | Ativo | [E10](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-22%2010h%2020m.png), [E11](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-22%2014h%2024m.png), [E12](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-22%2019h%2009m.png) |
| Dia 5 | Ativo | Ativo | Ativo | [E13](), [E14](), [E15]() |

Uma verificação será considerada bem-sucedida quando o produto puder ser acessado, a página principal carregar sem erro impeditivo e a operação selecionada produzir o resultado esperado.

Resultado obtido: As verificações foram realizadas durante cinco dias consecutivos, com três verificações por dia, totalizando 15 verificações. Em todas elas, o produto esteve disponível e permitiu o acesso e a execução da operação funcional selecionada. Portanto, o resultado foi:

D = (15 / 15) * 100 = 100%

Interpretação: O resultado de 100% indica que o Sua Grade UnB esteve acessível em todas as verificações realizadas durante o período avaliado, sem indisponibilidade observada. Esse resultado demonstra disponibilidade observada satisfatória nas condições e nos horários testados. Entretanto, como as verificações ocorreram em momentos específicos do dia, não é possível concluir que o sistema permaneceu disponível ininterruptamente durante os cinco dias.

### M6 — Tolerância a falhas

**Questão relacionada:** Qual é a proporção das situações de falha avaliadas em que o sistema identifica o problema e fornece um aviso adequado ao usuário?

**Definição:** Mede a proporção das situações de falha previstas nos testes em que o Sua Grade UnB reconhece uma condição que impede a operação solicitada e informa o usuário adequadamente, permitindo compreender por que a operação não pôde ser concluída.

**Fórmula:**

```text
T_f = (F_i / F_t) * 100
```

Em que:

- `T_f`: proporção de situações de falha tratadas adequadamente;
- `F_i`: número de situações de falha identificadas e comunicadas adequadamente pelo sistema;
- `F_t`: número total de situações de falha avaliadas.

**Fonte dos dados:** Resultados dos testes realizados no Sua Grade UnB e mensagens de aviso exibidas pelo sistema diante de condições que impedem a execução das operações solicitadas.

**Procedimento de coleta:**

1. Tentar buscar uma disciplina sem informar o período letivo.
2. Tentar selecionar mais de cinco turmas de uma mesma disciplina.
3. Realizar uma busca de disciplinas utilizando parâmetros que não retornem resultados.
4. Tentar inserir uma disciplina em uma grade quando não houver possibilidade de adicioná-la sem conflito de horários.
5. Registrar se o sistema identifica cada situação e apresenta um aviso que explique adequadamente o motivo pelo qual a operação não pode ser concluída.
6. Classificar cada situação como tratada adequadamente ou não tratada adequadamente.
7. Calcular a proporção de situações tratadas adequadamente em relação ao total avaliado.

**Resultado obtido:** Nas cinco situações avaliadas, o sistema apresentou avisos ao usuário: ao tentar buscar uma disciplina sem informar o período letivo, ao tentar selecionar mais de cinco turmas de uma mesma disciplina, quando a busca não encontrou disciplinas correspondentes aos parâmetros informados e quando não era possível inserir uma disciplina sem gerar conflito de horários.

Considerando que as cinco situações foram identificadas e comunicadas adequadamente pelo sistema, o resultado foi:

```text
T_f = (4 / 4) * 100 = 100%
```
| Teste | Descrição | Aviso | Evidência |
| :---: | :--- | :---: | :--- |
| T1 | Buscar uma disciplina sem informar o período letivo. | Sim | [E1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Buscar%20sem%20escolher%20periodo%20(falha).png) |
| T2 | Tentar selecionar mais de quatro turmas de uma mesma disciplina. | Sim | [E2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Selecionando%20mais%20de%204%20turmas%20da%20mesma%20materia.png) |
| T3 | Buscar disciplinas com parâmetros que não retornam resultados. | Sim | [E3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Busca%20por%20materia%20e%20professor%20(falha).png) |
| T4 | Tentar inserir uma disciplina que não pode ser encaixado em uma grade válida por conflito. | Sim | [E4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Impedir%20conflitos%20de%20horarios.png) |
| T5 | Tentar buscar sem parametros. | Sim | [E4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/Buscar%20sem%20parametros.png) |

**Interpretação:** O resultado de 100% indica que todas as situações de falha avaliadas foram acompanhadas de avisos do sistema. Isso demonstra que, nos cenários testados, o Sua Grade UnB fornece respostas informativas quando determinadas condições impedem a realização das operações solicitadas. Entretanto, a métrica avalia especificamente a identificação e a comunicação dessas situações, não abrangendo a recuperação automática de falhas, a continuidade do serviço após erros ou a prevenção de perda de dados.

## 3. Portabilidade

### M7 — Adaptabilidade em ambientes avaliados

**Questão relacionada:** Em que proporção dos ambientes selecionados o produto pode ser utilizado sem modificações específicas?

**Definição:** Mede a proporção dos ambientes selecionados para avaliação nos quais o Sua Grade UnB pode ser utilizado conforme os requisitos definidos, sem modificações específicas no produto.

**Fórmula:**

```text
A_p = (A_c / A_t) * 100
```

Em que:

- `A_p`: proporção de ambientes compatíveis;
- `A_c`: número de ambientes em que o produto atende às condições definidas;
- `A_t`: número total de ambientes avaliados.

**Fonte dos dados:** especificação dos ambientes de avaliação, documentação de compatibilidade disponível e resultados dos testes realizados.

**Procedimento de coleta:**

- Acessar o Sua Grade UnB nos navegadores Mozilla Firefox, Opera GX, Brave e Microsoft Edge.
- Acessar o sistema em um dispositivo móvel utilizando os navegadores DuckDuckGo e Google Chrome.
- Verificar se o sistema pode ser acessado e se suas funcionalidades podem ser utilizadas conforme o comportamento esperado.
- Registrar o resultado de cada teste, identificando eventuais problemas de funcionamento.
- Calcular a proporção de ambientes nos quais o sistema funcionou corretamente.

Resultado obtido: Foram avaliados seis ambientes de navegação: Mozilla Firefox, Opera GX, Brave, Microsoft Edge, DuckDuckGo para dispositivos móveis e Google Chrome para dispositivos móveis. Em todos os ambientes testados, o sistema funcionou corretamente, sem problemas observados que impedissem sua utilização.

P = (6 / 6) * 100 = 100%

| Teste | Ambiente | Funcionou  | Evidência |
| :---: | :--- | :---: | :--- |
| T1 | Mozilla firefox (Windows) | Sim | [E1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/disponibilidade/Captura%20de%20tela%202026-10-19%209h%2022m.png) |
| T2 | Opera gx (Windows) | Sim | [E2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/portabilidade/Funcionando%20no%20opera.png) |
| T3 | Brave (Windows) | Sim | [E3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/portabilidade/Funcionando%20no%20brave.png) |
| T4 | Microsoft Edge (Windows) | Sim | [E4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/portabilidade/Funcionando%20no%20microsoft%20edge.png) |
| T5 | DuckDuckGo (Android) | Sim | [E4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/portabilidade/Funcionando%20duckduckgo%20(celular).jpeg) |
| T6 | Chrome (Android) | Sim | [E5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_HEDY_LAMAR/blob/main/docs/evidencias/portabilidade/Funcionando%20chrome%20(celular).jpeg) |

Interpretação: O resultado de 100% indica que o Sua Grade UnB funcionou corretamente em todos os ambientes de navegação avaliados, incluindo navegadores utilizados em computadores e dispositivos móveis. Esse resultado demonstra compatibilidade nos ambientes testados, mas não garante o funcionamento adequado em todos os navegadores, dispositivos, sistemas operacionais ou versões existentes.

## 4. Rastreabilidade e julgamento

Os dados brutos, as evidências e os registros de cálculo deverão ser mantidos no repositório do projeto, permitindo relacionar cada resultado à respectiva fonte.

Os critérios de julgamento e os níveis de pontuação de cada métrica deverão ser documentados em `criterios-julgamento.md`. 

A métrica de completude funcional utiliza o planejamento do *story map* como referência. As demais métricas dependem de cenários, condições e resultados esperados definidos antes da coleta, de modo a garantir consistência e reprodutibilidade.

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1.0 | Versão inicial das metricas | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 22/10/2026 |   |  |
| 1.1 | Adição das métricas de funcionalidades e confiabilidade | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 22/10/2026 |   |  |
| 1.2 | Adição das evidencias em confiabilidade e resultado de portabilidade | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 22/10/2026 |   |  |
| 1.2 | Adição das evidencias em portabilidade | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 22/10/2026 |   |  |
| 1.3 | Correção do M6 | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 23/10/2026 |   |  |