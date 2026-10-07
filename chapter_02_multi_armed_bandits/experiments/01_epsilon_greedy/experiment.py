"""Minimal epsilon-greedy bandit experiment."""

import numpy as np


def run_bandit(epsilon=0.1, steps=200, seed=0):
    rng = np.random.default_rng(seed)

    true_values = np.array([0.0, 1.0, 1.5])
    estimates = np.zeros(3)
    counts = np.zeros(3)

    rewards = []

    for step in range(steps):
        if rng.random() < epsilon:
            action = rng.integers(0, len(true_values))
        else:
            action = int(np.argmax(estimates))

        reward = rng.normal(true_values[action], 1.0)

        counts[action] += 1
        estimates[action] += (reward - estimates[action]) / counts[action]
        rewards.append(reward)

        if step < 10:
            print(
                f"step={step:3d} action={action} reward={reward: .3f} "
                f"estimates={np.round(estimates, 3)}"
            )

    print("\nTrue values:     ", true_values)
    print("Estimated values:", np.round(estimates, 3))
    print("Action counts:   ", counts.astype(int))
    print("Average reward:  ", round(float(np.mean(rewards)), 3))


if __name__ == "__main__":
    run_bandit()
