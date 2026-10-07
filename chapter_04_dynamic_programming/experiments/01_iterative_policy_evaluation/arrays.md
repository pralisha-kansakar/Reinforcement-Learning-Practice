# One Array vs Two Arrays

## Question

What is the difference between using two arrays and one array when doing iterative policy evaluation?

## Experiment

I tested the same policy evaluation problem using:

1. **Two arrays** — `old_values` and `values`
2. **One array (in-place)** — newly computed values immediately overwrite old values

The state space was:

```text
States: 0, 1, 2, 3
Terminal states: 0 and 3
Reward: -1 per transition
Policy: left/right with equal probability
gamma = 1
```

## Observation

### Two-array version

```text
iteration 0: [ 0. -1. -1.  0.]
iteration 1: [ 0.  -1.5 -1.5  0.]
iteration 2: [ 0.   -1.75 -1.75  0.]
...
iteration 27: [ 0. -1.99999999 -1.99999999  0.]

Final: [ 0. -2. -2.  0.]
```

Both non-terminal states changed at the same rate because each update used the **old values from the previous sweep**.

### One-array / in-place version

```text
iteration 0: [ 0.  -1.  -1.5  0. ]
iteration 1: [ 0.   -1.75 -1.875  0.  ]
iteration 2: [ 0.     -1.9375 -1.96875  0.     ]
...
iteration 13: [ 0. -1.99999999 -1.99999999  0.]
iteration 14: [ 0. -2. -2.  0.]

Final: [ 0. -2. -2.  0.]
```

The in-place version converged much faster: about **15 iterations instead of 28**.

## Why?

In the two-array version, state 2 uses the old value of state 1:

```python
old_values[1]
```

In the in-place version, state 2 can use the **newly updated value** of state 1:

```python
values[1]
```

So information moves through the state space during the same sweep.

Because I updated the states in the order:
 
```text
1 → 2
```

state 2 immediately benefited from the new value of state 1.


The final answer is the same, but the **speed of convergence can be different**.

This also means that for in-place DP, **the order in which states are updated can affect how quickly the algorithm converges**.
