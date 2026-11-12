"""Funções compartilhadas pelos scripts de coleta do PSM."""

import csv
from pathlib import Path


def gravar_csv_se_mudou(caminho: Path, cabecalho, linhas, ignorar=()):
    """Grava o CSV somente se os dados mudaram.

    As colunas listadas em `ignorar` não entram na comparação (por exemplo,
    o horário da coleta). Assim, uma execução automática sem novidades não
    altera o arquivo e não gera commit.

    Retorna True se o arquivo foi gravado e False se permaneceu como estava.
    """
    indices = [i for i, nome in enumerate(cabecalho) if nome not in ignorar]

    if caminho.exists():
        with caminho.open(encoding="utf-8", newline="") as arquivo:
            existentes = list(csv.reader(arquivo))
        if (
            existentes
            and existentes[0] == list(cabecalho)
            and all(len(linha) == len(cabecalho) for linha in existentes[1:])
        ):
            antigas = [[linha[i] for i in indices] for linha in existentes[1:]]
            novas = [[str(linha[i]) for i in indices] for linha in linhas]
            if antigas == novas:
                return False

    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(cabecalho)
        escritor.writerows(linhas)
    return True
