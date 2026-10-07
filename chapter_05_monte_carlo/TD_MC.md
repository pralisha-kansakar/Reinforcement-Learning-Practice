# Temporal-Difference (TD) Learning and Bootstrapping

## 1. What is Temporal-Difference (TD) Learning?

**TD = Temporal-Difference learning.**

The main idea is:

> TD learning updates the value function from experience one step at a time, without waiting for the episode to finish.

Suppose the agent is in state `S_t`.

It takes action `A_t`, receives reward `R_(t+1)`, and moves to state `S_(t+1)`.

TD immediately uses this experience to update the value of `S_t`.

The standard TD(0) update is:

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \right]
$$

Where:

- `V(S_t)` = current estimate of the value of the current state
- `R_(t+1)` = reward received after taking the action
- `V(S_(t+1))` = current estimate of the next state's value
- `gamma` = discount factor
- `alpha` = learning rate

---

# 2. TD vs. Monte Carlo

Consider an episode:

```text
S0 -> S1 -> S2 -> S3 -> Terminal
```

with rewards:

```text
     -1   -1   +10
```

## Monte Carlo

Monte Carlo waits until the episode finishes.

It calculates the complete return:

$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots
$$

Then it uses that return to update the value.

**MC waits until the episode ends.**

---

## Temporal-Difference Learning

TD updates immediately after a transition.

It uses:

$$
R_{t+1} + \gamma V(S_{t+1})
$$

as its target.

**TD does not wait for the episode to finish.**

---

# 3. What is Bootstrapping?

**Bootstrapping** means:

> Using an estimate to improve another estimate.

In TD, the target is:

$$
R_{t+1} + \gamma V(S_{t+1})
$$

The important part is:

$$
V(S_{t+1})
$$

This is **not the true value** of `S_(t+1)`.

It is our **current estimate** of its value.

Therefore, TD uses one estimate to improve another estimate.

That is called **bootstrapping**.

$$
\boxed{\text{TD bootstraps}}
$$

---

# 4. Simple Intuition for Bootstrapping

Imagine you are trying to estimate how far you are from your destination.

You are at location A.

You move to location B and travel 1 mile.

You currently estimate that B is 5 miles from the destination.

So you estimate:

```text
1 mile + estimated 5 miles = 6 miles
```

You don't know the true remaining distance.

You use your **current estimate of B** to improve your estimate for A.

That is the basic idea of bootstrapping.

---

# 5. Numerical Example of TD

Suppose:

$$
V(S_t) = 5
$$

$$
V(S_{t+1}) = 8
$$

$$
R_{t+1} = 2
$$

and:

$$
\gamma = 0.9
$$

The TD target is:

$$
R_{t+1} + \gamma V(S_{t+1})
$$

Substituting the values:

$$
2 + 0.9(8) = 9.2
$$

Our current estimate is:

$$
V(S_t) = 5
$$

The target is:

$$
9.2
$$

So we move our estimate toward `9.2`.

Suppose:

$$
\alpha = 0.1
$$

Then:

$$
V(S_t) = 5 + 0.1(9.2 - 5)
$$

$$
V(S_t) = 5.42
$$

So:

$$
\boxed{V(S_t) = 5.42}
$$

TD updated the value **without waiting for the episode to end**.

---

# 6. TD Error

The quantity

$$
R_{t+1} + \gamma V(S_{t+1}) - V(S_t)
$$

is called the **TD error**.

It is usually written as:

$$
\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)
$$

The TD error tells us:

> How different is the new TD target from our current prediction?

In the previous example:

$$
\delta_t = 9.2 - 5
$$

$$
\delta_t = 4.2
$$

Our current estimate was 4.2 lower than the TD target.

The update can therefore be written as:

$$
V(S_t) \leftarrow V(S_t) + \alpha \delta_t
$$

---

# 7. Example of TD Learning Step-by-Step

Suppose:

```text
S0 --(-1)--> S1 --(-1)--> S2 --(+10)--> Terminal
```

Initially:

$$
V(S_0) = 0
$$

$$
V(S_1) = 0
$$

$$
V(S_2) = 0
$$

## Step 1: `S0 -> S1`

The agent receives:

$$
R_1 = -1
$$

TD uses:

$$
-1 + \gamma V(S_1)
$$

Since:

$$
V(S_1) = 0
$$

the target is initially:

$$
-1
$$

So `V(S0)` moves toward `-1`.

TD has already learned something after **one step**.

It did not need to wait for the terminal state.

---

## Step 2: `S1 -> S2`

The agent receives:

$$
R_2 = -1
$$

TD updates `V(S1)` using:

$$
-1 + \gamma V(S_2)
$$

Again, it learns immediately.

---

## Step 3: `S2 -> Terminal`

The agent receives:

$$
R_3 = 10
$$

For a terminal state:

$$
V(\text{Terminal}) = 0
$$

Therefore the target becomes:

$$
10 + \gamma(0) = 10
$$

So `V(S2)` learns that this state leads to a reward of `10`.

That information can then influence earlier states through future TD updates.

---

# 8. Why Does TD Bootstrap?

Look at the TD target:

$$
R_{t+1} + \gamma V(S_{t+1})
$$

The target depends on:

$$
V(S_{t+1})
$$

But `V(S_(t+1))` is itself an **estimate**.

Therefore:

```text
estimate of next state
        |
        v
update current state
```

This is bootstrapping.

---

# 9. Monte Carlo Does NOT Bootstrap

Monte Carlo uses the complete return:

$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots
$$

The target consists of **actual rewards observed in the episode**.

It does not use:

$$
V(S_{t+1})
$$

as part of its target.

Therefore:

$$
\boxed{\text{MC does not bootstrap}}
$$

---

# 10. TD and the Bellman Equation

TD is closely related to the Bellman equation.

The Bellman expectation equation is:

$$
V^\pi(s) =
\mathbb{E}_\pi
\left[
R_{t+1} + \gamma V^\pi(S_{t+1})
\mid S_t = s
\right]
$$

The key quantity is:

$$
R_{t+1} + \gamma V(S_{t+1})
$$

Dynamic Programming calculates an **expectation over possible transitions** using the environment model.

TD does not need the model.

Instead, TD observes **one actual transition**:

```text
S_t -> S_(t+1)
```

and one actual reward:

```text
R_(t+1)
```

Then it uses:

$$
R_{t+1} + \gamma V(S_{t+1})
$$

as a sample-based target.

So TD can be thought of as performing a:

> **sample-based Bellman backup**

---

# 11. DP vs. MC vs. TD

| Method | Uses Model? | Waits for Episode End? | Bootstraps? | Main Idea |
|---|---|---|---|---|
| **Dynamic Programming** | Yes | No | Yes | Use Bellman equations and the environment model |
| **Monte Carlo** | No | **Yes** | **No** | Learn from complete returns |
| **TD** | No | **No** | **Yes** | Learn from one-step experience |

A useful way to remember them:

```text
DP = Model

MC = Complete Return

TD = Next-State Estimate
```

---

# 12. The Most Important Difference

## Monte Carlo

Target:

$$
G_t
$$

where:

$$G_t = R_{t+1}+ \gamma R_{t+2}+ \gamma^2 R_{t+3}+ \cdots
$$

MC waits until the episode is complete.

The target is based on **actual future rewards**.

Therefore:

```text
MC -> does NOT bootstrap
```

---

## TD(0)

Target:

$$
R_{t+1} + \gamma V(S_{t+1})
$$

TD updates after one step.

Because it uses `V(S_(t+1))`, it **bootstraps**.

```text
TD -> DOES bootstrap
```

---

# 13. Easy Intuition

Think of the three methods this way:

### Dynamic Programming

> "I know the rules of the environment, so I can calculate what should happen."

### Monte Carlo

> "I'll wait until I see the final outcome, then learn from what actually happened."

### TD

> "I don't need to wait. I'll use the reward I just received and my current estimate of what comes next."

---

# 14. Key Definitions to Memorize

### Temporal-Difference Learning

> TD learning updates value estimates from experience before the episode ends.

### Bootstrapping

> Bootstrapping means using an existing estimate to update another estimate.

### TD Error

$$ 
\delta_t = R_{t+1}+ \gamma V(S_{t+1})- V(S_t)
$$

### TD(0) Update

$$
V(S_t) \leftarrow V(S_t) + \alpha \delta_t
$$

or equivalently:

$$V(S_t)\leftarrow V(S_t)+ \alpha \left[R_{t+1}+ \gamma V(S_{t+1})- V(S_t)\right]
$$

---

# 15. One-Sentence Summary

> **Monte Carlo waits until the end and learns from the actual return, while TD learns after each step and bootstraps by using its current estimate of the next state's value.**

$$
\boxed{\text{MC: actual future}}
\qquad
\boxed{\text{TD: estimated future}}
$$