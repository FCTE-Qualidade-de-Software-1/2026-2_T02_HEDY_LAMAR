"""Coleta os commits da branch `main` e os associa aos integrantes da equipe.

Entradas : histórico Git local (referência `origin/main` por padrão) e
           dados/psm/integrantes.csv (e-mail do autor -> integrante)
Saída    : dados/psm/commits.csv (um commit por linha)

Critérios (ver docs/gestao/metrica-2-metodo.md):
  * somente commits da referência indicada (por padrão, `origin/main`);
  * commits de merge são excluídos;
  * identidades diferentes da mesma pessoa são consolidadas pelo
    arquivo integrantes.csv.

Uso (a partir da raiz do repositório, após `git fetch origin`):
    python scripts/coletar_commits.py [referencia]
"""

import csv
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INTEGRANTES = RAIZ / "dados" / "psm" / "integrantes.csv"
SAIDA = RAIZ / "dados" / "psm" / "commits.csv"

SEPARADOR = "\x1f"  # separador de campos que não aparece em mensagens de commit


def ler_mapa_identidades():
    mapa = {}
    with INTEGRANTES.open(encoding="utf-8", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            if linha["email"]:
                mapa[linha["email"].strip().lower()] = linha["integrante"].strip()
    return mapa


def listar_commits(referencia):
    formato = SEPARADOR.join(["%H", "%aI", "%an", "%ae", "%s"])
    resultado = subprocess.run(
        ["git", "log", referencia, "--no-merges", f"--format={formato}"],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return [linha.split(SEPARADOR) for linha in resultado.stdout.splitlines() if linha]


def main():
    referencia = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
    mapa = ler_mapa_identidades()
    coletado_em = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    linhas = []
    nao_mapeados = set()
    for hash_, data, nome, email, assunto in listar_commits(referencia):
        integrante = mapa.get(email.strip().lower())
        if integrante is None:
            nao_mapeados.add(f"{nome} <{email}>")
            integrante = "NAO_MAPEADO"
        linhas.append([hash_, data, nome, email, integrante, assunto, coletado_em])

    linhas.sort(key=lambda linha: linha[1])  # ordem cronológica

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    with SAIDA.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(
            ["hash", "data_autor", "autor_nome", "autor_email",
             "integrante", "assunto", "coletado_em_utc"]
        )
        escritor.writerows(linhas)

    print(f"{len(linhas)} commits (sem merges) em {referencia} -> {SAIDA.relative_to(RAIZ)}")
    if nao_mapeados:
        print("ATENÇÃO: identidades sem integrante em integrantes.csv:")
        for identidade in sorted(nao_mapeados):
            print(f"  - {identidade}")
        sys.exit(1)


if __name__ == "__main__":
    main()
