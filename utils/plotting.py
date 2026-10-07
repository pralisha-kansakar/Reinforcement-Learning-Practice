"""Small plotting helpers for RL experiments."""

import matplotlib.pyplot as plt


def plot_values(values, title="Value function", xlabel="State", ylabel="Value"):
    plt.figure()
    plt.plot(range(len(values)), values, marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()
