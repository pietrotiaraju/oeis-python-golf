# A002035

> Numbers that contain primes to odd powers only.
> — [OEIS A002035](https://oeis.org/A002035)

Offset 1: 2, 3, 5, 6, 7, 8, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 24, 26, 27, …

### Python 3 — 87 bytes

```python
from math import*
n=1
while n:=n+1:all(gcd(n,d**3)-d*d for d in range(2,n))and print(n)
```

**How it works**

- n has a prime p to an even exponent 2k ≥ 2 exactly when some d ≥ 2
  has d² | n with n/d² coprime to d: take d = pᵏ; conversely every
  prime of such a d divides n exactly to twice its exponent in d.
- When d² | n, gcd(n, d³) = d²·gcd(n/d², d); and gcd(n, d³) = d²
  forces d² | n. So the test above is simply gcd(n, d³) = d², and n is
  a term when no d in 2 … n − 1 passes it (d² ≤ n already implies
  d < n for n ≥ 2).
- n starts at 2, so 1 (no prime at all) is left out, as in the data.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1000 terms; the bar is the whole b-file in 60 s, which
  takes under a second.
- The more direct test `n%d**2or gcd(n//d**2,d)>1` is 9 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002035), CC BY-SA 4.0.
