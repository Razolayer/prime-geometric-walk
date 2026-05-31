# Prime Geometric Walk

Experimental discrete geometric walk for odd composite detection using incremental integer operations.

---

# Overview

This project explores an alternative geometric representation of odd integers and primality detection.

Instead of relying primarily on repeated modular division, the method represents odd factor families as intersections between:

* odd linear families,
* and quadratic envelopes.

The resulting search process becomes a discrete walk over a lattice-like geometric structure.

The algorithm currently operates mostly through:

* integer addition,
* subtraction,
* comparisons,
* and local state transitions.

---

# Core Idea

Define odd factor families:

$$
n = 2a + 1
$$

and:

$$
y = \frac{x}{n} - n
$$

which yields:

$$
x = n(n+y)
$$

If:

$$
x = P
$$

then:

$$
P = n(n+y)
$$

is a nontrivial odd factorization.

A quadratic envelope is also defined:

$$
y^2 = (2B)^2 - 4x
$$

The walk navigates the intersections between these structures.

---

# Geometric Interpretation

The lattice behaves visually more like:

* a rotated square grid,
* diamond neighborhoods,
* or a rhomboid geometry,

than a standard Cartesian coordinate system.

The walk oscillates around the target integer while progressively reducing the active odd slope family.

---

# Walk Rules

Two primary transitions are currently used.

## Upper-Right Move

Keeps the same odd slope family:

$$
B \rightarrow B+1
$$

$$
y \rightarrow y+2
$$

$$
x \rightarrow x + 2n
$$

---

## Upper-Left Move

Changes the active odd slope family:

$$
a \rightarrow a-1
$$

$$
n \rightarrow n-2
$$

$$
y \rightarrow y+4
$$

$$
x \rightarrow n(n+y)
$$

---

# Termination

If during the walk:

$$
x = P
$$

with:

$$
n > 1
$$

then a nontrivial odd factorization has been found and the number is composite.

If the walk reaches:

$$
n = 1
$$

without collision, the number is declared prime.

---

# Example

For:

$$
P = 31
$$

The walk becomes:

```text
(35,2)  -> +4
(27,6)  -> -4
(33,8)  -> +2
(13,12) -> slope 1 reached
```

No exact collision occurred before reaching slope 1.

Therefore:

```text
31 is prime
```

---

# Experimental Status

Current brute-force validation produced no known counterexamples up to:

```text
100,000
```

Known successful detections include:

```text
35 = 5 × 7
87 = 3 × 29
91 = 7 × 13
```

This does NOT constitute a proof of correctness.

The project should currently be considered:

* experimental,
* exploratory,
* and conjectural.

---

# Computational Motivation

The primary motivation is reducing the operational cost per step.

The walk avoids repeated modular division inside the core loop and instead uses:

* incremental updates,
* local transitions,
* and discrete geometry.

Potential advantages:

* low arithmetic cost,
* cache locality,
* simple integer operations,
* low branching complexity.

Potential weaknesses:

* unknown worst-case behavior,
* no formal proof,
* possible undiscovered counterexamples.

---

# Repository Structure

```text
prime-geometric-walk/
├── README.md
├── LICENSE
├── paper/
│   └── draft.md
├── src/
│   └── prime_walk.py
├── tests/
│   └── brute_force_validation.py
└── notes/
    └── geometry.md
```

---

# Running

```bash
python src/prime_walk.py
```

---

# License

MIT License

---

# Disclaimer

This project is experimental research.

No formal proof currently exists for:

* completeness,
* asymptotic complexity,
* or correctness over arbitrary integers.

Use at your own risk.

---

# Author

Ariel Lugones
