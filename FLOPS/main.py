from time import time
from matplotlib import pyplot as plt
import numpy as np

lista_n = [100000]   # Quantidade de operações
R = 30                 # Quantidade de testes

t = []

for n in lista_n:

    tt = []

    for r in range(R):

        tic = time()

        for i in range(n):
            x = 1.0 + 2.0       # operação de ponto flutuante

        toc = time()

        tempo = toc - tic
        tt.append(tempo)

    t.append(tt)

    # transforma em array NumPy
    tt = np.array(tt)

    # ==========================================
    # ESTATÍSTICAS
    # ==========================================

    media = np.mean(tt)
    sigma = np.std(tt)

    cv = sigma / media

    # ==========================================
    # OPERAÇÕES POR SEGUNDO
    # ==========================================

    ops_por_segundo = n / media

    # ==========================================
    # HISTOGRAMA
    # ==========================================

    plt.hist(tt, bins=50)
    plt.title(f"n = {n}")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Frequência")
    plt.show()

    # ==========================================
    # RESULTADOS
    # ==========================================

    print("=" * 60)
    print(f"n = {n}")
    print(f"R = {R}")
    print("=" * 60)

    print(f"Média: {media:.10f} s")
    print(f"Desvio padrão: {sigma:.10f} s")
    print(f"CV: {cv:.4f}")

    print(f"\nOperações: {n:,}")
    print(f"Operações por segundo: {ops_por_segundo:,.2f}")