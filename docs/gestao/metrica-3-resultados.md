## Métrica 3 - Tempo médio de resolução de Pull Requests: resultados e análise

Esta página apresenta o resultado, o gráfico e a análise da Métrica 3. O método está em Método.


## 5.5. Resultado

- Período analisado: 19/10/2026 a 14/11/2026.
- Data da coleta registrada: 14/11/2026 (15:42 UTC).
- Quantidade de Pull Requests integrados considerados: 12.
- Tempo médio de resolução: 2,70 dias (classificação: **Ideal**).
- Mediana do tempo de resolução: 0,80 dia.
- Menor tempo de resolução observado: 0 dia (PRs #40 e #41).
- Maior tempo de resolução observado: 17,55 dias (PR #7).
- Pull Requests fechados sem integração: 0.

Cálculo do tempo médio:

(0,34 + 0,81 + 2,02 + 0,79 + 0,76 + 17,55 + 5,65 + 2,14 + 0 + 0 + 2,32 + 0,01) / 12

= 32,39 / 12 ≈ **2,70 dias**.

O resultado permanece dentro do critério Ideal, estabelecido em até 3 dias. Os tempos individuais estão apresentados na Figura 3 e registrados no arquivo `dados/psm/prs.csv`.

## 5.7. Análise

O tempo médio de resolução foi de 2,70 dias, permanecendo dentro do critério Ideal (até 3 dias). Em comparação com a coleta anterior, que apresentou média de 1,14 dia, houve aumento no tempo médio de integração.

A mediana permaneceu em 0,80 dia, indicando que pelo menos metade dos Pull Requests integrados foi resolvida em até esse intervalo. Entretanto, os PRs #7 e #8 apresentaram tempos de 17,55 e 5,65 dias, respectivamente, elevando a média do período.

O resultado demonstra que o fluxo de integração continua atendendo ao critério estabelecido, mas apresenta casos pontuais de demora que merecem atenção. A amostra também aumentou de seis para doze Pull Requests, oferecendo uma base de observação mais ampla, embora ainda limitada ao histórico disponível no projeto.

!!! success "Decisão de gestão decorrente"
    Manter o fluxo atual de integração por Pull Requests, uma vez que o tempo médio permanece na faixa Ideal. Entretanto, acompanhar os casos de maior duração e verificar, nas próximas medições, se o aumento da média representa uma tendência ou situações pontuais.
