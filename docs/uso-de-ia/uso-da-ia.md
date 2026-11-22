# Uso de Inteligência Artificial

Esta página declara o uso de ferramentas de inteligência artificial na elaboração dos documentos e na criação dos scripts Python que automatizam a coleta de dados do PSM. Ela informa qual ferramenta foi usada, em quais tarefas, como os resultados foram conferidos pela equipe e quais decisões permaneceram sob responsabilidade humana.

## Ferramenta e tarefas

A ferramenta utilizada foi o Claude, IA da Anthropic. Ela foi usada como apoio em três tarefas, descritas na Tabela 1.

<font size="3"><p style="text-align: left">Tabela 1: Tarefas com apoio de IA nas fases</p></font>

| Tarefa | Como foi usada | Como foi conferida pela equipe |
| :--- | :--- | :--- |
| Rascunho de texto | Geração de primeira versão de trechos de texto | Cada trecho foi lido, reescrito quando necessário e conferido nas fontes |
| Revisão de português | Sugestões de correção gramatical e de clareza em trechos já escritos pela equipe | Cada sugestão foi avaliada antes de ser aceita |
| Estrutura e tabelas | Sugestões de organização das seções e de formatação das tabelas | A organização final foi decidida pela equipe e revisada na leitura dos documentos |
| Transcrição de reuniões | Foi utilizada para fazer as transcrições das reuniões, resumos das mesmas, auxiliando no documento de atas. | Cada transcrição foi conferida por um membro da equipe antes da criação dos documentos |

Autor(es):  [João Vitor](https://github.com/Jauzimm), [João Victor Marques](https://github.com/jmarquees), 2026.

## Conferência e criticidade

Todo trecho produzido com apoio da ferramenta foi lido e, quando necessário, reescrito pela equipe. As afirmações técnicas foram checadas contra as fontes citadas nos documentos: as normas da série ISO/IEC 25000 (ISO/IEC 25010, 25021 e a própria 25000), os materiais da disciplina e a página do IPEA sobre o ODS 4.

Em alguns momentos, a ferramenta gerou sugestões que a equipe corrigiu antes de aceitá-las, seja por imprecisão, seja por não se ajustar ao contexto do Sua Grade UnB. Por isso, a ferramenta foi tratada como fonte de rascunhos e de sugestões, e não como fonte de conteúdo técnico.

## Scripts Python e automação da coleta de dados

Os scripts Python do repositório foram escritos integralmente pela IA. A equipe não escreveu o código desses scripts: ela definiu o que cada um deveria fazer, pediu a implementação à ferramenta e fez a supervisão humana, que consistiu em executar os scripts e verificar se funcionavam e se os resultados faziam sentido.

Muitos desses scripts geram arquivos CSV, que permitem automatizar as tabelas e a coleta de dados do PSM. A Tabela 2 lista os scripts, suas entradas e saídas.

<font size="3"><p style="text-align: left">Tabela 2: Scripts Python criados com apoio de IA</p></font>

| Script | O que faz | Entrada | Saída |
| :--- | :--- | :--- | :--- |
| `coletar_commits.py` | Coleta os commits da `main` e os associa a cada integrante (Métrica 2) | Histórico Git e `dados/psm/integrantes.csv` | `dados/psm/commits.csv` |
| `coletar_prs.py` | Coleta os Pull Requests pelo GitHub CLI e calcula os dias até a integração (Métrica 3) | GitHub CLI (`gh`) | `dados/psm/prs.csv` |
| `gerar_grafico_commits.py` | Gera o gráfico da distribuição de commits (Métrica 2) | `commits.csv` e `integrantes.csv` | `docs/assets/psm-commits-distribuicao.png` |
| `gerar_grafico_prs.py` | Gera o gráfico do tempo de resolução de PRs (Métrica 3) | `prs.csv` | `docs/assets/psm-prs-tempo-resolucao.png` |
| `gerar_grafico_entregas.py` | Gera o gráfico da antecedência de conclusão das entregas (Métrica 1) | `entregas.csv` | `docs/assets/psm-entregas-antecedencia.png` |
| `utilidades.py` | Funções compartilhadas, como a gravação do CSV somente quando os dados mudam | Não se aplica | Não se aplica |

Autor(es):  [João Vitor](https://github.com/Jauzimm), 2026.

Os scripts de coleta são executados diariamente pelo fluxo de trabalho `psm-coleta.yml`, do GitHub Actions, e os CSV resultantes alimentam as tabelas e os gráficos do PSM. Os critérios de cada métrica (o que conta como commit, o que conta como Pull Request integrado e as faixas de avaliação) foram definidos pela equipe e estão nos documentos de método da gestão. A IA apenas os implementou em código.

## Decisões de conteúdo

As decisões de conteúdo são julgamentos da equipe, registrados nos próprios documentos. Entre elas estão a escolha das características de qualidade, os valores da matriz de priorização (impacto, risco e viabilidade), as premissas sobre o requisitante e a definição do escopo. Essas escolhas podem ser verificadas nas seções [2.1](../fase-1/proposito.md), [2.2](../fase-1/requisitantes.md), [2.4](../fase-1/justificativas.md) e [2.5](../fase-1/modelo.md).

## Ética e citações

As referências citadas em cada documento são as da bibliografia correspondente e foram conferidas pela equipe. Quando um trecho reproduz literalmente uma norma ou um material da disciplina, ele aparece entre aspas e com a fonte indicada. A ferramenta não é citada como fonte de conteúdo técnico.


## Limitações

A ferramenta pode produzir texto plausível e impreciso. Por isso, a conferência foi feita nas fontes, e não apenas pela leitura do texto gerado. Nenhuma afirmação das fases deve ser lida como resultado de verificação automatizada.

Os scripts Python foram gerados pela IA e conferidos pela equipe apenas por meio de execução e supervisão humana, sem revisão linha a linha do código. Por isso, os números do PSM dependem do funcionamento correto desses scripts e podem ser recoletados e conferidos nos CSV em `dados/psm/`.

---

## Bibliografia

> 1. ANTHROPIC. *Claude*. Modelo de linguagem. 2026. Disponível em: <https://claude.ai>.

## Histórico de Versão

| Versão |          Descrição          |                       Autor                       |    Data    |                       Revisor                       | Data de revisão |
| :----: | :-------------------------: | :-----------------------------------------------: | :--------: | :-------------------------------------------------: | :-------------: |
|  1.0   |       Versão Inicial        |     [João Vitor](https://github.com/Jauzimm)      | 24/10/2026 | [Pablo Rodrigues](https://github.com/Pablo-R-L) | 26/10/2026  |
|  1.1   |      Adição sobre scripts       |     [João Vitor](https://github.com/Jauzimm)      | 15/11/2026 |  |   |
|  1.2   |  Correção dos links após a mudança de pasta e de erros de digitação  |  [Cauã Clemente](https://github.com/CauaoClemente)  | 15/11/2026 |  |   |
