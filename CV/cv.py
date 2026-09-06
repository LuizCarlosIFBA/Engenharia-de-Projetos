from time import time
from matplotlib import pyplot as plt
import numpy as np

lista_n = [100000]

t = []
R = 300

for n in lista_n:

    tt = []

    for r in range(R):

        tic = time()

        for i in range(n):
            x = 1

        toc = time()

        tt.append(toc - tic)

    t.append(tt)

    # transforma em array numpy
    tt = np.array(tt)

    bins = 50

    plt.hist(tt, bins=bins)
    plt.title(f"n = {n}")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Frequência")

    plt.savefig(f"tempos_n{n}.png")
    plt.show()


    # ==========================================
    # CV ANTES DA FILTRAGEM
    # ==========================================

    media = np.mean(tt)
    sigma = np.std(tt)

    cv_antes = sigma / media


    # ==========================================
    # MÉTODO 1
    # média + x * desvio padrão
    # ==========================================

    # x = 2
    corte_x2 = media + 2 * sigma

    filtro_x2 = tt[tt < corte_x2]

    media_x2 = np.mean(filtro_x2)
    sigma_x2 = np.std(filtro_x2)

    cv_x2 = sigma_x2 / media_x2


    # x = 3
    corte_x3 = media + 3 * sigma

    filtro_x3 = tt[tt < corte_x3]

    media_x3 = np.mean(filtro_x3)
    sigma_x3 = np.std(filtro_x3)

    cv_x3 = sigma_x3 / media_x3


    # ==========================================
    # MÉTODO 2
    # remoção dos maiores 2% e 5%
    # ==========================================

    # retirar maiores 2%
    corte_p2 = np.percentile(tt, 98)

    filtro_p2 = tt[tt < corte_p2]

    media_p2 = np.mean(filtro_p2)
    sigma_p2 = np.std(filtro_p2)

    cv_p2 = sigma_p2 / media_p2


    # retirar maiores 5%
    corte_p5 = np.percentile(tt, 95)

    filtro_p5 = tt[tt < corte_p5]

    media_p5 = np.mean(filtro_p5)
    sigma_p5 = np.std(filtro_p5)

    cv_p5 = sigma_p5 / media_p5


    # ==========================================
    # RESULTADOS
    # ==========================================

    print("=" * 60)
    print(f"n = {n}")
    print("=" * 60)

    print(f"Média original: {media:.8f} s")
    print(f"Desvio padrão original: {sigma:.8f} s")
    print(f"CV ANTES: {cv_antes:.4f}")

    print("\nMÉTODO 1")

    print(f"x = 2")
    print(f"Corte: {corte_x2:.8f}")
    print(f"Quantidade após filtro: {len(filtro_x2)}")
    print(f"CV: {cv_x2:.4f}")

    print(f"\nx = 3")
    print(f"Corte: {corte_x3:.8f}")
    print(f"Quantidade após filtro: {len(filtro_x3)}")
    print(f"CV: {cv_x3:.4f}")

    print("\nMÉTODO 2")

    print("Removendo maiores 2%")
    print(f"Corte (percentil 98): {corte_p2:.8f}")
    print(f"Quantidade após filtro: {len(filtro_p2)}")
    print(f"CV: {cv_p2:.4f}")

    print("\nRemovendo maiores 5%")
    print(f"Corte (percentil 95): {corte_p5:.8f}")
    print(f"Quantidade após filtro: {len(filtro_p5)}")
    print(f"CV: {cv_p5:.4f}")

    print()