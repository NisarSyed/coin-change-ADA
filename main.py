from CoinChange import CoinChange as cc
from matplotlib import pyplot as plt
from time import perf_counter
import numpy as np

def main():
    coins = [1, 5, 10, 20, 50, 100, 500]
    n = [i for i in range(10**2, 10**6 + 1, 10**2)]
    amounts = []
    for i in range(len(n)-1):
        amounts.append(np.random.randint(n[i], n[i+1]))
    print(amounts)
    dp_bottom_up = []
    # dp_top_down = []
    # recursion = []
    greedy = []
    for amount in amounts:
        start = perf_counter()
        cc(coins, amount, "dp_bottom_up")
        dp_bottom_up.append(perf_counter()-start)
        # start = perf_counter()
        # cc(coins, amount, "dp_top_down")
        # dp_top_down.append(perf_counter()-start)
        # start = perf_counter()
        # cc(coins, amount, "recursion")
        # recursion.append(perf_counter()-start)
        start = perf_counter()
        cc(coins, amount, "greedy")
        greedy.append(perf_counter()-start)
        print(amount)
    plt.plot(n[:-1], dp_bottom_up, label="dp_bottom_up")
    # plt.plot(n[:-1], dp_top_down, label="dp_top_down")
    # plt.plot(n[:-1], recursion, label="recursion")
    plt.plot(n[:-1], greedy, label="greedy")
    plt.xlabel("Amount")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("Graph.png")

if __name__ == "__main__":
    main()