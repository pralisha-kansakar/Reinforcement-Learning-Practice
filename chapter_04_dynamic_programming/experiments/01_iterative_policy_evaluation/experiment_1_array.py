"""Tiny iterative-policy-evaluation experiment.

States: 0, 1, 2, 3
Terminal states: 0 and 3
Policy: from states 1 and 2, move left/right with equal probability.
Reward: -1 per transition.
"""

import numpy as np


def evaluate_policy(theta=1e-8, gamma=1.0):
    values = np.zeros(4)
    terminal = {0, 3}

    iteration = 0
    while True:
        old_values = values.copy()

        for state in [1, 2]:
            left_state = state - 1
            right_state = state + 1

            left_return = -1 + gamma * values[left_state]
            right_return = -1 + gamma * values[right_state]

            values[state] = 0.5 * left_return + 0.5 * right_return

        delta = np.max(np.abs(values - old_values))
        print(f"iteration {iteration:2d}: {values}")
        iteration += 1

        if delta < theta:
            break

    return values


if __name__ == "__main__":
    final_values = evaluate_policy()
    print("\nFinal values:", final_values)
