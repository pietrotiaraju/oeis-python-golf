# A001616

> Number of parabolic vertices of Gamma_0(n).
> — [OEIS A001616](https://oeis.org/A001616)

Offset 1: 1, 2, 2, 3, 2, 4, 2, 4, 4, 4, 2, 6, 2, 4, 4, 6, 2, 8, 2, 6, 4, 4, 2, 8, 6, 4, …

### Python 3 — 116 bytes

```python
from math import*
n=1
while[print(sum(gcd(x,d)*gcd(d,n//d)==d for d in range(1,n+1)if n%d<1for x in range(d)))]:n+=1
```

**How it works**

- The parabolic vertices are the cusps of Γ₀(n), and their number is the
  classical **Σ φ(gcd(d, n/d))** over the divisors d of n (one cusp a/d
  for each unit a modulo gcd(d, n/d); Diamond and Shurman, *A First Course
  in Modular Forms*, §3.8; the formula is on the OEIS page).
- φ(g) with g = gcd(d, n/d) is counted inside the residues x modulo d:
  **gcd(x, d) = d/g holds for exactly φ(g) of them**, namely x = (d/g)·y
  with y a unit modulo g. The test is written as `gcd(x,d)*gcd(d,n//d)==d`.
- So the double sum runs over the divisors d of n and x = 0, …, d − 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Term n costs σ(n) steps, so n terms take about 0.4·n² gcd pairs. Counting
  y in `range(gcd(d,n//d))` with `gcd(y,d,n//d)<2` instead is twice as
  fast but one byte longer (117).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001616), CC BY-SA 4.0.
