# A Discrete Geometric Walk for Odd Composite Detection Using Incremental Integer Operations

## Razolayer

---

# Abstract

We present an experimental geometric method for detecting odd composite numbers through a discrete walk over a lattice of odd factor families.

The method represents candidate factorizations as intersections between:

* odd linear families,
* and quadratic envelopes.

Unlike classical modular primality checks, the proposed approach operates primarily through:

* integer addition,
* subtraction,
* comparison,
* and local state transitions.

Preliminary brute-force validation up to 100,000 produced no observed counterexamples.

This work is exploratory and currently lacks a formal proof of correctness or asymptotic complexity.

---

# 1. Introduction

Most classical primality tests rely heavily on modular arithmetic and repeated division-like operations.

This work explores an alternative representation where odd composites emerge geometrically through a discrete traversal of odd-factor families.

The central idea is to encode odd divisibility through:

$$
n = 2a + 1
$$

and define:

$$
y = \frac{x}{n} - n
$$

which immediately yields:

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

defines a nontrivial odd factorization.

---

# 2. Quadratic Envelope

A second geometric structure is introduced:

$$
y^2 = (2B)^2 - 4x
$$

This equation defines a quadratic envelope that constrains the search space and determines the initial region of exploration.

The parameter:

$$
B \approx \sqrt{P}
$$

is used to initialize the walk near the target integer.

---

# 3. Initial State

For an odd integer (P):

$$
B = \lceil \sqrt{P} \rceil
$$

We choose the nearest odd slope family:

$$
n = 2a + 1
$$

below or equal to (B).

The initial state is constructed through:

$$
y = 2(B-n)
$$

$$
x = n(n+y)
$$

Example:

For:

$$
P = 31
$$

we obtain:

$$
B = 6
$$

$$
n = 5
$$

$$
y = 2
$$

$$
x = 35
$$

yielding the initial point:

$$
(35,2)
$$

---

# 4. Discrete Walk

The algorithm evolves through two local transitions.

---

## 4.1 Upper-Right Transition

Maintains the active odd slope family:

$$
B \rightarrow B+1
$$

$$
y \rightarrow y+2
$$

$$
x \rightarrow x + 2n
$$

This generates a linear incremental progression.

---

## 4.2 Upper-Left Transition

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

This transition moves toward smaller odd slope families.

---

# 5. Geometric Interpretation

The resulting lattice behaves visually more like:

* a rhomboid grid,
* a rotated square lattice,
* or a diamond neighborhood graph,

than a standard Cartesian plane.

The walk oscillates around the target integer while progressively approaching slope:

$$
n = 1
$$

which acts as a terminal boundary.

---

# 6. Termination Criteria

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

# 7. Experimental Results

Preliminary brute-force validation up to:

$$
100,000
$$

produced no observed counterexamples.

Successful composite detections include:

$$
35 = 5 \times 7
$$

$$
87 = 3 \times 29
$$

$$
91 = 7 \times 13
$$

while correctly classifying:

$$
23,\ 29,\ 31,\ 89
$$

as prime.

---

# 8. Computational Characteristics

The walk avoids repeated modular division inside the core loop.

Instead, the algorithm primarily uses:

* integer addition,
* subtraction,
* comparisons,
* and local updates.

Potential computational advantages include:

* low arithmetic cost,
* low branching complexity,
* favorable cache locality,
* and simple state evolution.

Observed traversal lengths appear experimentally near:

$$
O(\sqrt{P})
$$

though no formal proof currently exists.

---

# 9. Discussion

The proposed structure resembles a discrete geometric navigation over odd-factor space.

The method appears related to:

* difference-of-squares constructions,
* Fermat-style factorization,
* and lattice traversal methods,

while remaining fundamentally incremental and geometric.

At present, the work should be considered conjectural and exploratory.

---

# 10. Open Problems

Several key questions remain unresolved:

1. Does every odd composite necessarily intersect the walk before reaching (n=1)?
2. Can the traversal be formally bounded?
3. Are there pathological trajectories?
4. Can the walk be parallelized efficiently?
5. Does the lattice admit a closed-form geometric interpretation?

---

# 11. Conclusion

We introduced a discrete geometric walk over odd-factor families for experimental primality exploration.

Initial tests suggest surprisingly robust behavior despite the simplicity of the operations involved.

Further mathematical analysis is required to determine whether the construction defines a formally complete primality or factorization procedure.

---

# Author

Razolayer
