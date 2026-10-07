# Stochastic vs Deterministic Policies

## 1. What is a Policy?

A policy tells the agent what action to take in a given state.

The mathematical notation for a policy is:

$$
\pi(a \mid s)
$$

This means:

> The probability of taking action $a$ when the agent is in state $s$.

---

## 2. Stochastic Policy

A **stochastic policy** assigns probabilities to different actions.

Suppose state $S$ has two actions:

- Left
- Right

A stochastic policy could be:

$$
\pi(\text{Left} \mid S) = 0.7
$$

$$
\pi(\text{Right} \mid S) = 0.3
$$

So:

```text
State S
├── Left  → 70%
└── Right → 30%
```

The agent does not always take the same action.

### Key idea

A stochastic policy says:

> "There is a probability distribution over the possible actions."

---

## 3. Deterministic Policy

A **deterministic policy** always chooses one specific action in a state.

For example:

$$
\pi(\text{Left} \mid S) = 1
$$

$$
\pi(\text{Right} \mid S) = 0
$$

So:

```text
State S
└── Left → 100%
```

The agent always chooses Left in state $S$.

### Key idea

A deterministic policy says:

> "For this state, I choose this particular action."

---

# 4. Stochastic vs Deterministic

| Type | Meaning | Example |
|---|---|---|
| Stochastic | Actions have probabilities | Left = 70%, Right = 30% |
| Deterministic | One action has probability 1 | Right = 100% |

The main difference is **how the policy chooses actions**.

---

# 5. Why Does This Matter in Policy Improvement?

In policy improvement, we already have a policy $\pi$ and its value function:

$$
V^\pi(s)
$$

We want to find a better policy.

To do this, we look at the **action-value function**:

$$
q_\pi(s,a)
$$

This means:

> How good is it to take action $a$ in state $s$, and then continue following policy $\pi$?

---

# 6. Example of Policy Improvement

Suppose in state $S$:

$$
q_\pi(S,\text{Left}) = 5
$$

$$
q_\pi(S,\text{Right}) = 8
$$

Right is the better action.

Suppose our current policy is stochastic:

$$
\pi(\text{Left} \mid S) = 0.5
$$

$$
\pi(\text{Right} \mid S) = 0.5
$$

The value of the state is:

$$
V^\pi(S)
=
\sum_a \pi(a \mid S)q_\pi(S,a)
$$

Therefore:

$$
V^\pi(S)
=
0.5(5) + 0.5(8)
$$

$$
V^\pi(S) = 6.5
$$

But we know that Right has an action value of $8$.

So we can improve the policy by choosing Right with probability 1:

$$
\pi'(\text{Left} \mid S) = 0
$$

$$
\pi'(\text{Right} \mid S) = 1
$$

Now:

$$
V^{\pi'}(S) = 8
$$

Since:

$$
8 > 6.5
$$

the new policy is better.

---

# 7. What Does "Greedy" Mean?

A **greedy policy** chooses the action with the highest action value.

The greedy action is:

$$
\pi'(s) = \arg\max_a q_\pi(s,a)
$$

In simple words:

> Choose the action that currently looks best.

For example:

```text
qπ(S, Left)  = 5
qπ(S, Right) = 8
```

Then:

```text
Greedy choice:

Right → 100%
Left  → 0%
```

The resulting policy is deterministic.

---

# 8. What If Two Actions Are Equally Good?

Suppose:

$$
q_\pi(S,\text{Left}) = 8
$$

$$
q_\pi(S,\text{Right}) = 8
$$

Both actions are equally good.

We could choose either one deterministically:

```text
Left  → 100%
Right → 0%
```

or:

```text
Left  → 0%
Right → 100%
```

We could also use a stochastic policy:

```text
Left  → 50%
Right → 50%
```

because both actions have the same value.

So when there is a tie, a greedy policy can distribute probability among the actions that have the maximum value.

---

# 9. Important Concepts to Keep Separate

Three concepts appear together in this chapter.

## Policy

$$
\pi(a \mid s)
$$

Answers:

> What probability do I assign to action $a$ in state $s$?

---

## State Value

$$
V^\pi(s)
$$

Answers:

> How good is it to be in state $s$ while following policy $\pi$?

---

## Action Value

$$
q_\pi(s,a)
$$

Answers:

> How good is it to take action $a$ in state $s$, and then follow policy $\pi$?

---

# 10. Why Does Choosing the Best Action Improve the Policy?

The state value can be written as:

$$
V^\pi(s)
=
\sum_a \pi(a \mid s)q_\pi(s,a)
$$

This is a weighted average of the action values.

Suppose:

```text
qπ(S, Left)  = 5
qπ(S, Right) = 8
```

and the policy chooses both actions with equal probability:

$$
\pi(\text{Left} \mid S) = 0.5
$$

$$
\pi(\text{Right} \mid S) = 0.5
$$

Then:

$$
V^\pi(S) = 6.5
$$

The best available action has value:

$$
8
$$

Therefore, moving the policy toward Right can improve the expected value.

This is the basic idea behind **policy improvement**.

---

# 11. Policy Iteration

This connects directly to the Policy Iteration algorithm.

### Step 1: Start with a policy

Example:

```text
S1 → Left
S2 → Right
S3 → Left
```

---

### Step 2: Policy Evaluation

Calculate:

$$
V^\pi(s)
$$

This answers:

> How good is the current policy?

---

### Step 3: Policy Improvement

Calculate:

$$
q_\pi(s,a)
$$

for the available actions.

Then choose the best action:

$$
\pi'(s) = \arg\max_a q_\pi(s,a)
$$

---

### Step 4: Repeat

```text
Initial Policy
      ↓
Policy Evaluation
      ↓
Policy Improvement
      ↓
Better Policy
      ↓
Policy Evaluation
      ↓
Policy Improvement
      ↓
...
      ↓
Optimal Policy
```

---

# 12. Concrete Example

Suppose:

```text
State S

Left  → qπ(S, Left)  = 3
Right → qπ(S, Right) = 7
```

Current stochastic policy:

$$
\pi(\text{Left} \mid S) = 0.8
$$

$$
\pi(\text{Right} \mid S) = 0.2
$$

Then:

$$
V^\pi(S)
=
0.8(3) + 0.2(7)
$$

$$
V^\pi(S) = 3.8
$$

But Right has value $7$.

So policy improvement changes the policy toward Right:

$$
\pi'(\text{Left} \mid S) = 0
$$

$$
\pi'(\text{Right} \mid S) = 1
$$

Then:

$$
V^{\pi'}(S) = 7
$$

The new policy is better.

---

# 13. Main Takeaway

### Stochastic Policy

> Multiple actions can be selected, each with some probability.

Example:

$$
\pi(\text{Left} \mid S)=0.7,
\qquad
\pi(\text{Right} \mid S)=0.3
$$

### Deterministic Policy

> One action is selected with probability 1.

Example:

$$
\pi(\text{Right} \mid S)=1
$$

### Policy Improvement

> Compare the action values and move the policy toward the action(s) with the highest value.

### Greedy Policy

> Choose the action with the maximum $q_\pi(s,a)$.

---
