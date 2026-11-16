# A001838

> Numbers k such that phi(k+2) = phi(k) + 2.
> — [OEIS A001838](https://oeis.org/A001838)

Offset 1: 3, 5, 6, 11, 12, 14, 17, 18, 20, 29, 41, 44, 59, 62, 71, 92, 101, 107, 116, …

### Python 3 — 114 bytes

```python
D={};x=y=k=1
while 1:
 b=k=k+1
 for p in D.pop(k,[k]):b-=b//p;D[k+p]=D.get(k+p,[])+[p]
 b-x-2or print(k-2);x,y=y,b
```

**How it works**

- The sieve is the one of [A001274](../A001274/). `D` maps each number ahead of k to the primes
  found to divide it. When the loop reaches k, `D.pop(k,[k])` gives the distinct prime factors of
  k, or `[k]` when no prime was filed there, which happens exactly when k is prime. Each prime p
  is refiled at k + p, its next multiple, so every number meets all its prime factors.
- φ(k) = k·∏(1 − 1/p): starting from b = k, `b-=b//p` multiplies by (p − 1)/p, exactly, since p
  divides k and none of the primes already used.
- `x` and `y` hold φ(k − 2) and φ(k − 1), and `b` is φ(k); `b-x-2or print(k-2)` prints k − 2
  when φ(k) = φ(k − 2) + 2, and `x,y=y,b` shifts the window. The start values x = y = 1 only meet
  k = 2, where 1 − 1 − 2 ≠ 0.

**Notes**

- Exact integer arithmetic; the sieve keeps one list per prime up to k, about π(k) entries.
- The b-file has 10000 terms (k up to 927284); the bar is the whole b-file in 60 s, which takes
  about 4 s here. [A001836](../A001836/) and [A001837](../A001837/) use the same sieve.

## First 300 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 300 terms have to arrive in time.

### Python 3, 300 terms — 96 bytes

```python
from math import*
k=1
while[sum(1//gcd(k+2,i)-1//gcd(k,i)for i in range(k+2))==1==print(k)]:k+=1
```

**How it works**

- No sieve. The sum runs over i = 0, …, k + 1 and adds `1//gcd(k+2,i)` (1 when gcd(k + 2, i) = 1,
  else 0), which counts φ(k + 2), minus `1//gcd(k,i)`, which counts φ(k) plus one extra: for
  k ≥ 2, i = 0 and i = k add nothing (gcd = k) but i = k + 1 is prime to k. So the sum is
  φ(k + 2) − φ(k) − 1, and `==1==print(k)` prints k when φ(k + 2) = φ(k) + 2. At k = 1 the sum
  is 2 − 3 = −1.
- Each k costs 2(k + 2) gcds, so k up to K costs about K² of them: 18 bytes shorter than the
  sieve, but far slower.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-16 | 114 | first entry |

**Python 3, 300 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-16 | 96 | first entry: φ by counting gcds, no sieve |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001838), CC BY-SA 4.0.
