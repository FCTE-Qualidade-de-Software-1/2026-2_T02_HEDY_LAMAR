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
C_f = (10 / 11) * 100 ≈ 90,90%
```

**Interpretação:** o resultado indica que 90,90% das funcionalidades identificadas no planejamento estão implementadas. O julgamento de adequação desse resultado deve seguir os critérios definidos em `criterios-julgamento.md`.

### M2 — Correção funcional

**Questão relacionada:** Qual é a proporção das execuções de tarefas avaliadas que produzem os resultados esperados?

**Definição:** Mede a proporção de execuções de tarefas em que o produto produz o resultado esperado, conforme os requisitos e as condições definidos para cada teste.

**Fórmula:**

```text
C_c = (T_c / T_e) * 100
```

Em que:

- `C_c`: proporção de execuções corretas;
- `T_c`: número de execuções que produziram o resultado esperado;
- `T_e`: número total de execuções avaliadas.

**Fonte dos dados:** requisitos do produto, cenários de teste, resultados esperados.

**Procedimento de coleta:**

1. Selecionar tarefas funcionais previstas no planejamento.
2. Definir previamente o resultado esperado para cada tarefa.
3. Executar os cenários de teste nas condições estabelecidas.
4. Registrar o resultado observado.
5. Contabilizar as execuções que produziram o resultado esperado e calcular a proporção.

# espaço para resultado obtido, atualizar interpretação com o resultado tambem 

**Interpretação:** valores mais elevados indicam maior proporção de execuções que produziram os resultados esperados. O resultado deverá ser julgado de acordo com os níveis definidos em `criterios-julgamento.md`.

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

# espaço para resultado obtido, atualizar interpretação com o resultado tambem

**Interpretação:** valores mais elevados indicam que uma parcela maior das tarefas avaliadas é adequadamente atendida. Essa métrica avalia a adequação das funcionalidades às tarefas, enquanto a completude funcional verifica se as funcionalidades planejadas estão implementadas e a correção funcional verifica se as execuções produzem os resultados esperados.

## 2. Confiabilidade

### M4 — Execuções sem falhas

**Questão relacionada:** Qual é a proporção das execuções avaliadas que ocorre sem falhas observáveis?

**Definição:** Mede a proporção de execuções de cenários de teste que são concluídas sem falhas observáveis que impeçam ou comprometam o comportamento esperado.

**Fórmula:**

```text
R_e = (E_s / E_t) * 100
```

Em que:

- `R_e`: proporção de execuções sem falhas;
- `E_s`: número de execuções concluídas sem falhas observáveis;
- `E_t`: número total de execuções avaliadas.

**Fonte dos dados:** registros de execução dos testes, resultados observados e evidências de falhas.

**Procedimento de coleta:**

1. Definir os cenários de teste e as condições de execução.
2. Executar cada cenário conforme o procedimento estabelecido.
3. Registrar falhas observadas, incluindo as condições em que ocorreram.
4. Classificar as execuções como concluídas sem falhas ou com falhas.
5. Calcular a proporção de execuções sem falhas.

# espaço para resultado obtido, atualizar interpretação com o resultado tambem 

**Interpretação:** valores mais elevados indicam maior proporção de execuções sem falhas observáveis nas condições testadas. A métrica não demonstra, isoladamente, a ausência de defeitos nem a confiabilidade do produto em todas as condições de uso.

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
2. Em cada verificação, testar o acesso ao produto e executar a operação funcional selecionada.
3. Registrar data, horário, resultado e evidência.
4. Investigar problemas de conexão ou outras condições externas que possam comprometer a interpretação do resultado.
5. Calcular a proporção de verificações bem-sucedidas.

Uma verificação será considerada bem-sucedida quando o produto puder ser acessado, a página principal carregar sem erro impeditivo e a operação selecionada produzir o resultado esperado.

# espaço para resultado obtido, atualizar interpretação com o resultado tambem 

**Interpretação:** a métrica descreve a proporção de verificações bem-sucedidas durante a janela observada. Ela não deve ser interpretada como uma estimativa de disponibilidade contínua ao longo do tempo, pois a coleta é amostral. A janela e a quantidade de verificações são propostas de avaliação e deverão ser confirmadas antes da coleta.

### M6 — Tolerância a falhas

**Questão relacionada:** Qual é a proporção das situações de falha avaliadas em que o produto mantém ou recupera o comportamento esperado sem perda inaceitável?

**Definição:** Mede a proporção das situações de falha selecionadas para avaliação em que o produto mantém ou recupera o comportamento esperado, conforme critérios definidos previamente.

**Fórmula:**

```text
T_f = (F_r / F_a) * 100
```

Em que:

- `T_f`: proporção de situações de falha tratadas adequadamente;
- `F_r`: número de situações de falha em que o comportamento esperado foi mantido ou recuperado;
- `F_a`: número total de situações de falha avaliadas.

**Fonte dos dados:** cenários de teste de falhas, comportamento esperado e evidências das execuções.

**Procedimento de coleta:**

1. Identificar situações de falha relevantes e reproduzíveis para o produto.
2. Definir o comportamento esperado em cada situação.
3. Executar os cenários em ambiente controlado, quando viável.
4. Registrar se o produto manteve ou recuperou o comportamento esperado.
5. Calcular a proporção de situações tratadas adequadamente.

# espaço para resultado obtido, atualizar interpretação com o resultado tambem 

**Interpretação:** valores mais elevados indicam maior proporção de situações de falha tratadas adequadamente entre as avaliadas. Se não for possível definir e executar situações de falha pertinentes, a métrica deverá ser registrada como não avaliada, em vez de receber um resultado presumido.

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

1. Selecionar e documentar os ambientes pertinentes ao uso do produto, como navegadores e sistemas operacionais.
2. Definir as condições necessárias para considerar o produto utilizável em cada ambiente.
3. Executar os mesmos cenários funcionais nos ambientes selecionados.
4. Registrar os resultados e as evidências por ambiente.
5. Calcular a proporção de ambientes compatíveis.

# espaço para resultado obtido, atualizar interpretação com o resultado tambem 

**Interpretação:** valores mais elevados indicam compatibilidade com uma parcela maior dos ambientes avaliados. A conclusão deve se restringir aos ambientes efetivamente testados.

## 4. Rastreabilidade e julgamento

Os dados brutos, as evidências e os registros de cálculo deverão ser mantidos no repositório do projeto, permitindo relacionar cada resultado à respectiva fonte.

Os critérios de julgamento e os níveis de pontuação de cada métrica deverão ser documentados em `criterios-julgamento.md`. Quando uma métrica depender de testes ainda não realizados, seu resultado será registrado como pendente até a coleta das evidências necessárias.

A métrica de completude funcional utiliza o planejamento do *story map* como referência. As demais métricas dependem de cenários, condições e resultados esperados definidos antes da coleta, de modo a garantir consistência e reprodutibilidade.

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1.0 | Versão inicial das metricas | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 22/10/2026 |   |  |