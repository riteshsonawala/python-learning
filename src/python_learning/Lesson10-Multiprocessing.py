from multiprocessing import Pool
import os
import time

def cpu_heavy(n: int) -> int:
    print(f"Process {os.getpid()} working...")
    return sum(range(n))    # CPU bound — benefits from multiple processes

# Pool.map — simplest, like executor.map() but with processes
if __name__ == "__main__":    # REQUIRED for multiprocessing on Mac/Windows
    start = time.time()

    with Pool(processes=4) as pool:
        results = pool.map(cpu_heavy, [
            10_000_000,
            20_000_000,
            30_000_000,
            40_000_000,
        ])

    print(f"Results: {results}")
    print(f"Time: {time.time() - start:.1f}s")