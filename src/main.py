from coinchange import CoinChange as cc
from matplotlib import pyplot as plt
from time import perf_counter
import numpy as np

coins = [1, 5, 10, 25, 50]
ranges = {
    "recursion": np.arange(1, 59), 
    "dp_top_down": np.arange(10**1, 10**3 + 1, 10**1), 
    "dp_bottom_up": np.arange(10**2, 10**6 + 1, 10**3), 
    "greedy": np.arange(10**2, 10**5 + 1, 10**3)
}
amounts, times = {}, {}
for key,val in ranges.items():
    if key == "recursion":
        amounts[key] = val
        times[key] = []
        continue
    amounts[key] = [np.random.randint(val[i], val[i+1]) for i in range(len(val)-1)]
    times[key] = []
for key, val in amounts.items():
    print(f"Started timing {key}")
    l = len(val)
    for i,n in enumerate(val):
        # Average time for greedy and dp_top_down for a smoother graph
        if key in ["greedy","dp_top_down"]:
            avg = 10000 if key == "greedy" else 100
            for _ in range(avg):
                temp = 0
                start = perf_counter()
                cc(coins, n, key)
                end = perf_counter()
                temp += end - start
            times[key].append(temp/avg)
        else:
            start = perf_counter()
            cc(coins, n, key)
            end = perf_counter()
            times[key].append(end - start)
        print(f"{round((i+1)*100/l, 4)}%")
    plt.plot(val, times[key], label=key)
    plt.xlabel("Amount")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.savefig(f"plots/graph_{key}.png")
    plt.clf()
    print(f"Finished timing {key}")