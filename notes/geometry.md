# notes/geometry.md

# Geometry Notes

This document contains informal observations regarding the geometric structure used by the Prime Geometric Walk.

---

# 1. Core Representation

Odd slope families are defined as:

$$
n = 2a + 1
$$

with:

$$
y = \frac{x}{n} - n
$$

which implies:

$$
x = n(n+y)
$$

The quadratic envelope is:

$$
y^2 = (2B)^2 - 4x
$$

---

# 2. Visual Interpretation

The resulting lattice does not behave like a standard Cartesian grid.

Instead, it resembles:

* a rotated square lattice,
* rhomboid neighborhoods,
* or a diamond geometry.

The walk appears to oscillate around the target integer while reducing the active odd slope family.

---

# 3. Discrete Neighborhoods

The two primary transitions are:

## Upper-Right

$$
B \rightarrow B+1
$$

$$
y \rightarrow y+2
$$

$$
x \rightarrow x + 2n
$$

This creates a linear progression along a fixed odd slope family.

---

## Upper-Left

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

This changes the active odd slope family.

---

# 4. Observed Oscillation

For prime targets, the walk experimentally appears to oscillate around the target integer until reaching:

$$
n = 1
$$

Example:

```text id="44ik2n"
P = 31

(35,2) -> +4
(27,6) -> -4
(33,8) -> +2
(13,12) -> slope 1 reached
```

---

# 5. Composite Collisions

Composite numbers appear as exact collisions:

$$
x = P
$$

Examples:

$$
35 = 5 \times 7
$$

$$
87 = 3 \times 29
$$

$$
91 = 7 \times 13
$$

---

# 6. Experimental Status

The geometry currently remains conjectural.

No proof currently exists for:

* completeness,
* asymptotic complexity,
* guaranteed convergence,
* or correctness over arbitrary integers.

The structure is currently being explored experimentally.
