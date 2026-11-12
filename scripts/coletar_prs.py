"""Coleta os Pull Requests do repositório no GitHub (Métrica 3 do PSM).

Entrada : GitHub CLI (`gh`) autenticado, executado na raiz do repositório
Saída   : dados/psm/prs.csv (um Pull Request por linha)

Colunas de dias (ver docs/gestao/metrica-3-metodo.md):
  * integrado : data de integração - data de criação;
  * aberto    : data da coleta - data de criação (tempo decorrido);
  * fechado   : data de fechamento - data de criação (fechado sem integração).
O arquivo guarda todos os Pull Requests (dado bruto); o cálculo da média e o
gráfico consideram somente os integrados.

O arquivo só é regravado quando os dados dos Pull Requests mudam (número,
título, situação ou datas). Por isso `coletado_em_utc` registra o momento da
última atualização que alterou os dados, e o tempo decorrido dos Pull
Requests abertos refere-se a esse momento.

Uso (a partir da raiz do repositório):
    python scripts/coletar_prs.py [--saida caminho.csv]
"""

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from utilidades import gravar_csv_se_mudou

RAIZ = Path(__file__).resolve().parent.parent
SAIDA_PADRAO = RAIZ / "dados" / "psm" / "prs.csv"

SITUACAO = {"MERGED": "integrado", "OPEN": "aberto", "CLOSED": "fechado"}
CAMPOS = ["numero", "titulo", "situacao", "criado_em_utc", "integrado_em_utc",
          "fechado_em_utc", "dias", "coletado_em_utc"]


def parse(data_iso):
    return datetime.fromisoformat(data_iso.replace("Z", "+00:00")) if data_iso else None


def buscar_prs():
    resultado = subprocess.run(
        ["gh", "pr", "list", "--state", "all", "--limit", "1000", "--json",
         "number,title,state,createdAt,mergedAt,closedAt"],
        cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", check=True,
    )
    return json.loads(resultado.stdout)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--saida", type=Path, default=SAIDA_PADRAO,
                        help="arquivo CSV de saída (padrão: dados/psm/prs.csv)")
    args = parser.parse_args()

    agora = datetime.now(timezone.utc).replace(microsecond=0)
    coletado_em = agora.strftime("%Y-%m-%dT%H:%M:%SZ")

    linhas = []
    for pr in sorted(buscar_prs(), key=lambda p: p["number"]):
        criado = parse(pr["createdAt"])
        integrado = parse(pr["mergedAt"])
        fechado = parse(pr["closedAt"])
        situacao = SITUACAO[pr["state"]]
        fim = {"integrado": integrado, "fechado": fechado, "aberto": agora}[situacao]
        dias = (fim - criado).total_seconds() / 86400
        linhas.append([
            pr["number"], pr["title"], situacao, pr["createdAt"],
            pr["mergedAt"] or "", pr["closedAt"] or "", f"{dias:.2f}", coletado_em,
        ])

    # "dias" e "coletado_em_utc" não entram na comparação: o primeiro cresce a
    # cada dia nos PRs abertos e o segundo muda a cada execução.
    gravou = gravar_csv_se_mudou(args.saida, CAMPOS, linhas,
                                 ignorar=("dias", "coletado_em_utc"))
    por_situacao = {s: sum(1 for l in linhas if l[2] == s) for s in SITUACAO.values()}
    situacao = "atualizado" if gravou else "sem mudanças"
    print(f"{len(linhas)} Pull Requests -> {args.saida} {por_situacao} [{situacao}]")


if __name__ == "__main__":
    main()
