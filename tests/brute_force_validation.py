# tests/brute_force_validation.py

```python
import math
from src.prime_walk import prime_walk


def is_prime_classic(n: int) -> bool:
    """
    Reference primality test using classic trial division.
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
    Compare geometric walk results against a classic test.
    """

    tested = 0

    for n in range(2, limit + 1):
        walk_result, rows = prime_walk(n)
        classic_result = is_prime_classic(n)

        tested += 1

        if walk_result != classic_result:
            print("=" * 60)
            print("COUNTEREXAMPLE FOUND")
            print("=" * 60)

            print(f"n               = {n}")
            print(f"walk_result     = {walk_result}")
            print(f"classic_result  = {classic_result}")

            print("\nWalk trace:\n")

            for row in rows:
                print(row)

            return False

    print("=" * 60)
    print("VALIDATION FINISHED")
    print("=" * 60)

    print(f"Numbers tested : {tested}")
    print(f"Limit          : {limit}")
    print("Counterexamples: none found")

    return True


if __name__ == "__main__":
    validate(100_000)
```
