# src/prime_walk.py
import math


def start_point(P: int):
    """
    Build the initial geometric state for an odd integer P.

    State variables:
        a : odd-family index
        B : quadratic envelope parameter
        n : active odd slope, n = 2a + 1
        x : current integer position
        y : vertical coordinate
    """
    B = math.isqrt(P)

    if B * B < P:
        B += 1

    n = B if B % 2 == 1 else B - 1

    if n < 1:
        n = 1

    a = (n - 1) // 2

    y = 2 * (B - n)
    x = n * (n + y)

    return a, B, n, x, y


def prime_walk(P: int, max_steps: int = 100_000):
    """
    Experimental geometric walk for odd composite detection.

    Returns:
        is_prime_like: bool
        rows: list of states

    Each row:
        (step, a, B, n, x, y, d, move)
    """
    if P < 2:
        return False, [(0, None, None, None, P, None, None, "below 2")]

    if P == 2:
        return True, [(0, None, None, None, P, None, 0, "special prime 2")]

    if P % 2 == 0:
        return False, [(0, None, None, None, P, None, 0, "even composite")]

    a, B, n, x, y = start_point(P)

    rows = []

    for step in range(max_steps):
        d = x - P

        if x == P and n > 1:
            rows.append((step, a, B, n, x, y, d, "hit"))
            return False, rows

        if a == 0:
            rows.append((step, a, B, n, x, y, d, "slope 1 reached"))
            return True, rows

        if d > 0:
            move = "upper-left"

            a -= 1
            n -= 2
            y += 4
            x = n * (n + y)

        else:
            move = "upper-right"

            B += 1
            y += 2
            x += 2 * n

        rows.append((step, a, B, n, x, y, x - P, move))

    raise RuntimeError("Maximum number of steps reached")


def print_walk(P: int):
    is_prime, rows = prime_walk(P)

    print(f"P={P} -> {'PRIME' if is_prime else 'COMPOSITE'}")
    print("step | a | B | n | x | y | d | move")
    print("-" * 64)

    for step, a, B, n, x, y, d, move in rows:
        print(
            f"{step:4} | "
            f"{str(a):>2} | "
            f"{str(B):>2} | "
            f"{str(n):>2} | "
            f"{str(x):>8} | "
            f"{str(y):>4} | "
            f"{str(d):>8} | "
            f"{move}"
        )

    print()


def is_prime_classic(n: int) -> bool:
    """
    Simple reference primality test for validation.
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limit = math.isqrt(n)

    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False

    return True


def validate(limit: int = 100_000):
    """
    Compare the geometric walk against a classic trial-division test.
    """
    for n in range(2, limit + 1):
        walk_result, _ = prime_walk(n)
        classic_result = is_prime_classic(n)

        if walk_result != classic_result:
            print("Counterexample found!")
            print(f"n = {n}")
            print(f"walk_result    = {walk_result}")
            print(f"classic_result = {classic_result}")
            print_walk(n)
            return False

    print(f"No counterexamples up to {limit}.")
    return True


if __name__ == "__main__":
    for P in [23, 29, 31, 35, 87, 89, 91]:
        print_walk(P)

    validate(100_000)
