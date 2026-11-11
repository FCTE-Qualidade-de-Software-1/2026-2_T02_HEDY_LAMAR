"""Gera o gráfico de barras da Métrica 3 do PSM (tempo de resolução de PRs).

Entrada : dados/psm/prs.csv
Saída   : docs/assets/psm-prs-tempo-resolucao.png

Somente os Pull Requests integrados à `main` entram no gráfico e no
cálculo da média e da mediana (ver seção 5 de docs/gestao/PSM.md).

Uso (a partir da raiz do repositório):
    python scripts/gerar_grafico_prs.py

O gráfico é regenerado integralmente a partir do CSV; para atualizá-lo,
basta atualizar o CSV e executar o script novamente.
"""

import csv
import statistics
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # não exige interface gráfica (útil em CI)
import matplotlib.pyplot as plt
import matplotlib.ticker

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "dados" / "psm" / "prs.csv"
SAIDA = RAIZ / "docs" / "assets" / "psm-prs-tempo-resolucao.png"

LIMITE_IDEAL = 3  # dias (critério "Ideal" da Métrica 3)

COR_BARRA = "#2e7d32"
COR_MEDIA = "#1565c0"
COR_LIMITE = "#616161"


def fmt(valor):
    """Formata número com vírgula decimal (padrão pt-BR)."""
    return f"{valor:.2f}".replace(".", ",")


def ler_prs_integrados():
    with ENTRADA.open(encoding="utf-8", newline="") as arquivo:
        return [
            {
                "numero": int(linha["numero"]),
                "dias": float(linha["dias"]),
                "coleta": linha["coletado_em_utc"],
            }
            for linha in csv.DictReader(arquivo)
            if linha["situacao"] == "integrado"
        ]


def main():
    prs = sorted(ler_prs_integrados(), key=lambda pr: pr["numero"])
    valores = [pr["dias"] for pr in prs]
    media = statistics.mean(valores)
    mediana = statistics.median(valores)
    ano, mes, dia = prs[0]["coleta"][:10].split("-")
    coleta = f"{dia}/{mes}/{ano}"

    rotulos = [f"PR #{pr['numero']}" for pr in prs]

    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=150)
    barras = ax.bar(rotulos, valores, color=COR_BARRA, edgecolor="white", linewidth=0.8)

    for barra, valor in zip(barras, valores):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            valor + 0.05,
            fmt(valor),
            ha="center",
            va="bottom",
            fontsize=9,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.2, "alpha": 0.9},
            zorder=5,
        )

    ax.axhline(media, color=COR_MEDIA, linestyle="--", linewidth=1.3)
    ax.axhline(LIMITE_IDEAL, color=COR_LIMITE, linestyle=":", linewidth=1.2)

    ax.set_ylabel("Tempo (dias)")
    ax.set_title("Tempo de resolução dos Pull Requests integrados", fontsize=13, pad=12)
    ax.set_ylim(0, max(max(valores), LIMITE_IDEAL) * 1.15)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.4)
    ax.set_axisbelow(True)
    ax.yaxis.set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}".replace(".", ","))
    )

    legenda = [
        plt.Line2D([0], [0], color=COR_MEDIA, linestyle="--",
                   label=f"Média: {fmt(media)} dia(s)"),
        plt.Line2D([0], [0], color=COR_LIMITE, linestyle=":",
                   label=f"Limite Ideal: {LIMITE_IDEAL} dias"),
    ]
    ax.legend(
        handles=legenda,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.1),
        ncol=2,
        fontsize=9,
        frameon=False,
    )

    fig.text(
        0.01, 0.01,
        f"Fonte: dados/psm/prs.csv (coleta em {coleta}). "
        f"Mediana: {fmt(mediana)} dia(s). PRs integrados: {len(valores)}.",
        fontsize=8, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(SAIDA)
    print(f"Gráfico salvo em {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
