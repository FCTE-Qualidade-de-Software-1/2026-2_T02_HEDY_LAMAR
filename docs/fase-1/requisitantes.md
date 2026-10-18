# 2.2 Requisitantes e Partes Interessadas

## Introdução

Esta página identifica quem pede a avaliação e quem é afetado pelo Sua Grade UnB, e o que cada parte precisa do produto e da avaliação.

## Metodologia

As partes interessadas foram classificadas segundo a seção 3.6 da ISO/IEC 25010:2011, em usuário primário, usuário secundário e usuário indireto. Os pontos de vista de comprador, fornecedor, desenvolvedor e operador, citados na descrição do processo de avaliação da disciplina, foram mapeados nesses tipos. Por ser software livre e gratuito, o produto não tem comprador nem fornecedor comerciais.

## 2.2.1 Papéis, necessidades e influência na avaliação

<font size="3"><p style="text-align: left">Tabela 1: Requisitante e partes interessadas</p></font>

| Parte | Necessidade | Critério de sucesso | Influência na avaliação |
| :--- | :--- | :--- | :--- |
| Estudantes da UnB (usuário primário) | Montar a grade com turmas atuais, sem conflitos e com pouco esforço | Gerar e guardar uma grade válida do período corrente, no dispositivo que já usam | Define a prioridade da Adequação Funcional e a matriz de ambientes da Portabilidade |
| Equipe mantenedora (secundário: mantenedor e operador, requisitante) | Lista de defeitos priorizada e reproduzível; executa a atualização manual dos dados | Relatório com evidências suficientes para decidir o que corrigir primeiro | Define o propósito e o ponto de vista das métricas |
| UnB/SIGAA (secundário: provedor de conteúdo) | Evitar sobrecarga do SIGAA por requisições, motivo declarado do *scraping* na documentação | Dados do produto coerentes com a página pública de turmas | Fornece a referência de verdade da corretude; limita a coleta a consultas manuais da página pública |
| Quem recebe a grade exportada (indireto) | Abrir um arquivo legível e fiel à grade que o estudante montou | O PDF exportado reproduz a grade, com os mesmos horários, salas e professores | Sem influência direta nas escolhas da avaliação; justifica incluir a exportação em PDF no escopo, por ser a saída do sistema entregue a terceiros |

_OBS: Na parte indireta dos requisitantes, o estudante pode mandar esse PDF para alguém, como um orientador, um coordenador, a família ou um colega. Essa pessoa é o “usuário indireto”, porque recebe o PDF sem nunca abrir o site._

Autor(es):  [João Vitor](https://github.com/Jauzimm), 2026.

## 2.2.2 Quem não é parte interessada do produto

A equipe de avaliação e a professora da disciplina não são usuárias do produto: a primeira executa a avaliação e a segunda avalia o processo.

## 2.2.3 Premissa sobre o requisitante

Não há um requisitante formal para esta avaliação. Adotamos a equipe mantenedora como requisitante, porque é ela quem pode agir sobre os resultados. A premissa depende de a equipe ainda manter o projeto. O último commit no repositório é de 15/02/2026, o que indica manutenção recente.

## Bibliografia

> 1. ISO/IEC 25010:2011. *Systems and software engineering: SQuaRE: System and software quality models*. Seção 3.6.

> 2. EQUIPE SUA GRADE UNB. *Arquitetura*. In: Docs - Sua Grade UnB. Disponível em: <https://unb-mds.github.io/2023-2-SuaGradeUnB/architecture/>. Acesso em: 17 out. 2026.

## Histórico de Versão

| Versão |          Descrição          |                       Autor                       |    Data    |                       Revisor                       | Data de revisão |
| :----: | :-------------------------: | :-----------------------------------------------: | :--------: | :-------------------------------------------------: | :-------------: |
|  1.0   |       Versão Inicial        |     [João Vitor](https://github.com/Jauzimm)      | 18/10/2026 | [Joao Victor](https://github.com/jmarquees) |   |