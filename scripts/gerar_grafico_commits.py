"""Gera o gráfico de barras da Métrica 2 do PSM (distribuição de commits).

Entradas : dados/psm/commits.csv e dados/psm/integrantes.csv
Saída    : docs/assets/psm-commits-distribuicao.png

Uso (a partir da raiz do repositório):
    python scripts/coletar_commits.py
    python scripts/gerar_grafico_commits.py
"""

import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # não exige interface gráfica (útil em CI)
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.patches import Patch

RAIZ = Path(__file__).resolve().parent.parent
COMMITS = RAIZ / "dados" / "psm" / "commits.csv"
INTEGRANTES = RAIZ / "dados" / "psm" / "integrantes.csv"
SAIDA = RAIZ / "docs" / "assets" / "psm-commits-distribuicao.png"

# Faixas da Métrica 2 (seção 4.2 de docs/gestao/metrica-2-metodo.md), em % do total
IDEAL = (12, 28)
ACEITAVEL_INF = (8, 12)
ACEITAVEL_SUP = (28, 35)

COR = {"Ideal": "#2e7d32", "Aceitável": "#f9a825", "Ruim": "#c62828"}


def classificar(percentual):
    if IDEAL[0] <= percentual <= IDEAL[1]:
        return "Ideal"
    if ACEITAVEL_INF[0] <= percentual < IDEAL[0] or IDEAL[1] < percentual <= ACEITAVEL_SUP[1]:
        return "Aceitável"
    return "Ruim"


def fmt(valor):
    return f"{valor:.1f}".replace(".", ",")


def ler_integrantes():
    ordem = []
    with INTEGRANTES.open(encoding="utf-8", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            if linha["integrante"] not in ordem:
                ordem.append(linha["integrante"])
    return ordem


def ler_commits():
    with COMMITS.open(encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def main():
    commits = ler_commits()
    total = len(commits)
    contagem = Counter(c["integrante"] for c in commits)
    integrantes = ler_integrantes()
    datas = sorted(c["data_autor"][:10] for c in commits)
    coleta = commits[0]["coletado_em_utc"][:10].split("-")
    coleta = f"{coleta[2]}/{coleta[1]}/{coleta[0]}"

    percentuais = [contagem[i] / total * 100 for i in integrantes]
    classes = [classificar(p) for p in percentuais]

    fig, ax = plt.subplots(figsize=(9, 5.6), dpi=150)

    # Faixas de referência ao fundo
    ax.axhspan(0, ACEITAVEL_INF[0], color="#ffcdd2", alpha=0.35, lw=0)
    ax.axhspan(*ACEITAVEL_INF, color="#fff3c4", alpha=0.6, lw=0)
    ax.axhspan(*IDEAL, color="#c8e6c9", alpha=0.6, lw=0)
    ax.axhspan(*ACEITAVEL_SUP, color="#fff3c4", alpha=0.6, lw=0)
    ax.axhspan(ACEITAVEL_SUP[1], 100, color="#ffcdd2", alpha=0.35, lw=0)

    barras = ax.bar(
        integrantes, percentuais, color=[COR[c] for c in classes],
        edgecolor="white", linewidth=0.8, width=0.6, zorder=3,
    )
    for barra, integrante, pct, classe in zip(barras, integrantes, percentuais, classes):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            pct + 0.8,
            f"{fmt(pct)}%\n({contagem[integrante]} commits)\n{classe}",
            ha="center", va="bottom", fontsize=8.5, zorder=5,
        )

    topo = max(max(percentuais) * 1.35, 45)
    ax.set_ylim(0, topo)
    ax.set_ylabel("Participação no total de commits (%)")
    ax.set_title("Distribuição de commits por integrante (branch main)", fontsize=13, pad=12)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}%"))

    legenda = [
        Patch(facecolor=COR["Ideal"], label="Ideal (12% a 28%)"),
        Patch(facecolor=COR["Aceitável"], label="Aceitável (8% a 12% ou 28% a 35%)"),
        Patch(facecolor=COR["Ruim"], label="Ruim (fora das faixas)"),
    ]
    ax.legend(handles=legenda, loc="upper center", bbox_to_anchor=(0.5, -0.1),
              ncol=3, fontsize=8.5, frameon=False)

    fig.text(
        0.01, 0.01,
        f"Fonte: dados/psm/commits.csv (coleta em {coleta}; commits de "
        f"{datas[0][8:]}/{datas[0][5:7]} a {datas[-1][8:]}/{datas[-1][5:7]}; "
        f"total: {total}, sem merges).",
        fontsize=8, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(SAIDA)
    print(f"Gráfico salvo em {SAIDA.relative_to(RAIZ)}")
    for integrante, pct, classe in zip(integrantes, percentuais, classes):
        print(f"  {integrante}: {contagem[integrante]} commits, {fmt(pct)}% -> {classe}")


if __name__ == "__main__":
    main()
