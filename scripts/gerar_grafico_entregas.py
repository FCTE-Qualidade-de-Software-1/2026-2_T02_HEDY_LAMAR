"""Gera o gráfico da Métrica 1 do PSM (antecedência de conclusão das entregas).

Entrada : dados/psm/entregas.csv
Saída   : docs/assets/psm-entregas-antecedencia.png

Antecedência (dias) = data do prazo combinado - data de conclusão.
As datas de conclusão (UTC) são convertidas para o horário de Brasília
(UTC-3) antes de se obter a data, pois o prazo é definido nesse fuso.
Entregas sem prazo ou sem conclusão aparecem como pendentes.

Uso (a partir da raiz do repositório):
    python scripts/gerar_grafico_entregas.py
"""

import csv
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # não exige interface gráfica (útil em CI)
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.patches import Patch

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "dados" / "psm" / "entregas.csv"
SAIDA = RAIZ / "docs" / "assets" / "psm-entregas-antecedencia.png"

BRASILIA = timezone(timedelta(hours=-3))
LIMITE_IDEAL = 2  # dias (seção 3.2 de docs/gestao/PSM.md)

COR = {"Ideal": "#2e7d32", "Aceitável": "#f9a825", "Ruim": "#c62828"}


def classificar(antecedencia):
    if antecedencia >= LIMITE_IDEAL:
        return "Ideal"
    if antecedencia >= 0:
        return "Aceitável"
    return "Ruim"


def ler_entregas():
    entregas = []
    with ENTRADA.open(encoding="utf-8", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            antecedencia = None
            if linha["prazo"] and linha["conclusao_utc"]:
                prazo = date.fromisoformat(linha["prazo"])
                conclusao = datetime.fromisoformat(
                    linha["conclusao_utc"].replace("Z", "+00:00")
                ).astimezone(BRASILIA)
                antecedencia = (prazo - conclusao.date()).days
            entregas.append({"entrega": linha["entrega"], "antecedencia": antecedencia})
    return entregas


def main():
    entregas = ler_entregas()
    concluidas = [e for e in entregas if e["antecedencia"] is not None]

    fig, ax = plt.subplots(figsize=(9, 3.6), dpi=150)
    xmin, xmax = -3, 5

    ax.axvspan(xmin, 0, color="#ffcdd2", alpha=0.5, lw=0)
    ax.axvspan(0, LIMITE_IDEAL, color="#fff3c4", alpha=0.8, lw=0)
    ax.axvspan(LIMITE_IDEAL, xmax, color="#c8e6c9", alpha=0.7, lw=0)

    posicoes = list(range(len(entregas)))
    for pos, entrega in zip(posicoes, entregas):
        if entrega["antecedencia"] is None:
            ax.text((xmin + xmax) / 2, pos, "pendente", ha="center", va="center",
                    fontsize=10, color="#555555", style="italic")
            continue
        valor = entrega["antecedencia"]
        classe = classificar(valor)
        ax.scatter(valor, pos, s=260, color=COR[classe], edgecolor="black",
                   linewidth=1, zorder=5)
        ax.annotate(f"{valor} dia(s): {classe}", (valor, pos),
                    textcoords="offset points", xytext=(18, 0),
                    ha="left", va="center", fontsize=9, zorder=6,
                    bbox={"facecolor": "white", "edgecolor": "none",
                          "pad": 1.5, "alpha": 0.85})

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(len(entregas) - 0.5, -0.5)
    ax.set_yticks(posicoes)
    ax.set_yticklabels([e["entrega"] for e in entregas])
    ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    ax.set_xlabel("Antecedência de conclusão (dias antes do prazo)")
    ax.set_title("Antecedência de conclusão das entregas", fontsize=13, pad=12)
    ax.spines[["top", "right"]].set_visible(False)
    ax.axvline(0, color="#555555", linewidth=1, linestyle="--", zorder=2)

    legenda = [
        Patch(facecolor="#c8e6c9", label="Ideal (2 dias ou mais)"),
        Patch(facecolor="#fff3c4", label="Aceitável (0 a menos de 2 dias)"),
        Patch(facecolor="#ffcdd2", label="Ruim (atraso)"),
    ]
    ax.legend(handles=legenda, loc="upper center", bbox_to_anchor=(0.5, -0.3),
              ncol=3, fontsize=8.5, frameon=False)

    fig.text(0.01, 0.01,
             "Fonte: dados/psm/entregas.csv. Datas no horário de Brasília (UTC-3).",
             fontsize=8, color="#555555")
    fig.tight_layout(rect=(0, 0.04, 1, 1))

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(SAIDA)
    print(f"Gráfico salvo em {SAIDA.relative_to(RAIZ)}")
    for e in concluidas:
        print(f"  {e['entrega']}: antecedência {e['antecedencia']} dia(s) -> "
              f"{classificar(e['antecedencia'])}")


if __name__ == "__main__":
    main()
