import time
import numpy as np

def estimate_flops(n=100_000_000):
    print(f"Lancement de {n} opérations en virgule flottante...")

    a = np.random.rand(n).astype(np.float32)
    b = np.random.rand(n).astype(np.float32)

    start = time.time()

    # Une opération FLOP ici : addition
    c = a + b

    end = time.time()

    elapsed = end - start
    flops = n / elapsed

    print(f"Temps écoulé : {elapsed:.4f} secondes")
    print(f"Estimation des FLOPS : {flops:.2f} FLOPS ({flops / 1e9:.2f} GFLOPS)")

if __name__ == "__main__":
    estimate_flops()
