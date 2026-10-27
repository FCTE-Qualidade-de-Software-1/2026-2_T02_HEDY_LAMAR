# 3.2 Diagrama GQM

O diagrama abaixo representa a hierarquia de medição (Objetivo → Questão → Métrica) definida para a avaliação do Sua Grade UnB, conforme detalhado na seção [3.1 Objetivos, Questões e Hipóteses](objetivos.md) e nas [Métricas](Metricas.md).

```mermaid
graph TD
    %% Estilos
    classDef goal fill:#2f5d3a,color:#fff,stroke:#1f4228,stroke-width:2px;
    classDef question fill:#8cc9a0,color:#1f2a22,stroke:#46785a,stroke-width:1px;
    classDef metric fill:#faf8f2,color:#1f2a22,stroke:#2f5d3a,stroke-width:1px,stroke-dasharray: 5 5;

    %% Objetivo 1
    G1["G1: Adequação Funcional<br>(Identificar deficiências funcionais)"]:::goal
    G1 --> Q1["Q1: Completude funcional<br>(Funções previstas disponíveis?)"]:::question
    G1 --> Q2["Q2: Corretude funcional<br>(Dados correspondem ao SIGAA?)"]:::question
    G1 --> Q3["Q3: Adequação funcional<br>(Permite concluir a tarefa?)"]:::question
    
    Q1 --> M1["M1: Completude funcional<br>(10/11 funcionais = 90,91%)"]:::metric
    Q2 --> M2["M2: Correção funcional<br>(15/15 atributos = 100%)"]:::metric
    Q3 --> M3["M3: Adequação às tarefas<br>(5/5 tarefas = 100%)"]:::metric

    %% Objetivo 2
    G2["G2: Confiabilidade<br>(Identificar falhas e disponibilidade)"]:::goal
    G2 --> Q4["Q4: Maturidade<br>(Frequência de falhas)"]:::question
    G2 --> Q5["Q5: Disponibilidade<br>(Proporção de acessos)"]:::question
    G2 --> Q6["Q6: Tolerância a falhas<br>(Comportamento em erros)"]:::question
    
    Q4 --> M4["M4: Maturidade<br>(4/4 cenários = 100%)"]:::metric
    Q5 --> M5["M5: Disponibilidade<br>(15/15 verificações = 100%)"]:::metric
    Q6 --> M6["M6: Tolerância a falhas<br>(5/5 avisos = 100%)"]:::metric

    %% Objetivo 3
    G3["G3: Portabilidade<br>(Identificar limitações de ambiente)"]:::goal
    G3 --> Q7["Q7: Adaptabilidade<br>(Funciona nos ambientes?)"]:::question
    
    Q7 --> M7["M7: Adaptabilidade<br>(6/6 ambientes = 100%)"]:::metric

 

