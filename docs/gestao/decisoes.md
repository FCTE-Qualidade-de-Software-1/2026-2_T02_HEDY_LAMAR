# 6. Registro de decisões de gestão

Esta seção reúne as decisões tomadas a partir das medições, relacionando
cada uma ao resultado e à interpretação que a motivou, e indicando como
o efeito da decisão será verificado na próxima coleta.

## 6.1. Decisões registradas

Tabela 1: Decisões de gestão decorrentes das medições.

| ID | Categoria PSM/CID | Resultado da medição | Interpretação | Decisão | Verificação na próxima coleta |
|:---:|:---|:---|:---|:---|:---|
| D1 | Calendário e Progresso | Métrica 1: Entrega 1 concluída com 0 dia de antecedência (**Aceitável**), conforme a [seção 3.5](metrica-1-resultados.md#35-resultado). | Entrega no próprio dia do prazo, sem margem para imprevistos ([seção 3.7](metrica-1-resultados.md#37-analise)). | Definir, para a Entrega 2, um prazo interno 2 dias antes do prazo oficial e acompanhar as tarefas pendentes para redistribuí-las se o prazo interno estiver em risco. | Antecedência da Entrega 2 de 2 dias ou mais (faixa Ideal). |
| D2 | Recursos e Custos | Métrica 2: 40,0% / 40,0% / 15,0% / 5,0% / 0,0% dos 40 commits; quatro de cinco integrantes em **Ruim** ([seção 4.5](metrica-2-resultados.md#45-resultado)). | A distribuição reflete também o trabalho fora do Git: o código LaTeX do artigo não está versionado no repositório ([seção 4.7](metrica-2-resultados.md#47-analise)). | Versionar o código-fonte LaTeX do artigo no repositório e usar a Tabela de contribuição como referência complementar na interpretação da métrica. | Código LaTeX presente no repositório e participação de todos os integrantes registrada nos commits. |
| D3 | Desempenho dos Processos | Métrica 3: tempo médio de resolução de 1,14 dia (**Ideal**), mediana de 0,80 dia, 6 Pull Requests integrados ([seção 5.5](metrica-3-resultados.md#55-resultado)). | Fluxo de integração rápido; amostra pequena e dependente da disponibilidade para revisão ([seção 5.7](metrica-3-resultados.md#57-analise)). | Manter o fluxo atual de integração por Pull Requests. | Tempo médio de resolução de até 3 dias (faixa Ideal) na nova coleta. |

## 6.2. Procedimento de atualização

A cada nova coleta, o grupo deve:

1.  Atualizar os dados em `dados/psm/`: executar
    `python scripts/coletar_prs.py` (Pull Requests) e
    `python scripts/coletar_commits.py` (commits, após
    `git fetch origin`) e registrar prazo e conclusão de cada entrega em
    `entregas.csv`.
2.  Gerar os gráficos com os scripts `gerar_grafico_*.py` em `scripts/`.
3.  Atualizar os resultados e a análise nas páginas de resultados das métricas ([Métrica 1](metrica-1-resultados.md), [Métrica 2](metrica-2-resultados.md) e [Métrica 3](metrica-3-resultados.md)).
4.  Registrar, na Tabela 1, o resultado das decisões anteriores e as
    novas decisões, com a data da coleta.


## 7. Considerações finais

As três métricas permitem acompanhar dimensões distintas do
desenvolvimento: cumprimento dos prazos combinados, distribuição das
contribuições registradas no Git e tempo de integração das alterações à
branch `main`.

Os resultados deverão ser interpretados considerando o período de
coleta, os critérios de inclusão e as limitações de cada indicador. Em
particular, a quantidade de commits não deve ser tratada como medida
direta de esforço, e o tempo de integração de Pull Requests não deve ser
interpretado isoladamente como medida de produtividade ou qualidade.

## 8. Histórico de atualização  

| Versão | Descrição | Autor | Data | Revisor | Data de revisão |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1.0 | Criação da documentação das métricas PSM/CID. | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 05/10/2026 | [João Vitor](https://github.com/Jauzimm) | 10/11/2026 |
| 1.1 | Remoção do tópico de evidencias. | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 08/10/2026 | [João Vitor](https://github.com/Jauzimm) | 10/11/2026 |
