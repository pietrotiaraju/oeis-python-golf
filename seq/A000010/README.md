# A000010

> Euler totient function phi(n): count numbers <= n and prime to n.
> — [OEIS A000010](https://oeis.org/A000010)

Offset 1: 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, …

### Python 3 — 67 bytes

```python
n=F=1
while[print(sum(1%n==pow(k,F,n)for k in range(n)))]:n+=1;F*=n
```

**How it works**

- No `gcd`: k is prime to n exactly when k^F ≡ 1 (mod n) for F = n!.
  If gcd(k, n) = 1, Euler's theorem gives k^φ(n) ≡ 1, and φ(n) ≤ n divides
  n!. If gcd(k, n) > 1, no power of k is 1 mod n, since that would make k
  invertible.
- `F` is kept equal to n! (`F*=n` after each step), and three-argument `pow`
  keeps the numbers small.
- `1%n` is 1, except for n = 1, where every power is 0 mod 1 and `1%1` is 0,
  so k = 0 is counted and φ(1) = 1 comes out without a special case.
- Writing `1%n==pow(…)` instead of `pow(…)==1%n` saves the space before `for`.

**Notes**

- The exponent n! has about n log₂ n bits, so each term costs about n² log n
  steps: about 600 terms a minute. The bar is 500 terms in 60 s.
- The plain `math.gcd` count, `import math` + `sum(math.gcd(n,k)<2for k in
  range(n))`, is 72 bytes and about 30 times faster. The divisor-sum
  recurrence φ(n) = n − Σ φ(d) over proper divisors d is 76.

### Python 3 + sympy — 52 bytes

```python
from sympy import*
n=1
while[print(totient(n))]:n+=1
```

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 67 | first entry |
| 2026-11-05 | Python 3 + sympy | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000010), CC BY-SA 4.0.
