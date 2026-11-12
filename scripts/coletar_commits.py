"""Coleta os commits da branch `main` e os associa aos integrantes da equipe.

Entradas : histórico Git local (referência `origin/main` por padrão) e
           dados/psm/integrantes.csv (e-mail do autor -> integrante)
Saída    : dados/psm/commits.csv (um commit por linha)

Critérios (ver docs/gestao/metrica-2-metodo.md):
  * somente commits da referência indicada (por padrão, `origin/main`);
  * commits de merge são excluídos;
  * commits de automações (autor com "[bot]" no nome ou no e-mail, como o
    `github-actions[bot]`) são excluídos, pois não representam esforço de
    um integrante;
  * identidades diferentes da mesma pessoa são consolidadas pelo
    arquivo integrantes.csv.

O arquivo só é regravado quando os dados mudam. A coluna `coletado_em_utc`
registra o momento da última atualização que alterou os dados.

Uso (a partir da raiz do repositório, após `git fetch origin`):
    python scripts/coletar_commits.py [referencia] [--saida caminho.csv]
"""

import argparse
import csv
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from utilidades import gravar_csv_se_mudou

RAIZ = Path(__file__).resolve().parent.parent
INTEGRANTES = RAIZ / "dados" / "psm" / "integrantes.csv"
SAIDA_PADRAO = RAIZ / "dados" / "psm" / "commits.csv"

SEPARADOR = "\x1f"  # separador de campos que não aparece em mensagens de commit
CAMPOS = ["hash", "data_autor", "autor_nome", "autor_email",
          "integrante", "assunto", "coletado_em_utc"]


def ler_mapa_identidades():
    mapa = {}
    with INTEGRANTES.open(encoding="utf-8", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            if linha["email"]:
                mapa[linha["email"].strip().lower()] = linha["integrante"].strip()
    return mapa


def eh_automacao(nome, email):
    """True para autores de automações, como `github-actions[bot]`."""
    return "[bot]" in nome.lower() or "[bot]" in email.lower()


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
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("referencia", nargs="?", default="origin/main",
                        help="referência Git a coletar (padrão: origin/main)")
    parser.add_argument("--saida", type=Path, default=SAIDA_PADRAO,
                        help="arquivo CSV de saída (padrão: dados/psm/commits.csv)")
    args = parser.parse_args()

    mapa = ler_mapa_identidades()
    coletado_em = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    linhas = []
    nao_mapeados = set()
    automacoes = 0
    for hash_, data, nome, email, assunto in listar_commits(args.referencia):
        if eh_automacao(nome, email):
            automacoes += 1
            continue
        integrante = mapa.get(email.strip().lower())
        if integrante is None:
            nao_mapeados.add(f"{nome} <{email}>")
            integrante = "NAO_MAPEADO"
        linhas.append([hash_, data, nome, email, integrante, assunto, coletado_em])

    linhas.sort(key=lambda linha: linha[1])  # ordem cronológica

    gravou = gravar_csv_se_mudou(args.saida, CAMPOS, linhas, ignorar=("coletado_em_utc",))
    situacao = "atualizado" if gravou else "sem mudanças"
    print(f"{len(linhas)} commits (sem merges e sem automações; "
          f"{automacoes} de automação ignorados) em {args.referencia} -> {args.saida} [{situacao}]")

    if nao_mapeados:
        print("ATENÇÃO: identidades sem integrante em integrantes.csv:")
        for identidade in sorted(nao_mapeados):
            print(f"  - {identidade}")
        sys.exit(1)


if __name__ == "__main__":
    main()
