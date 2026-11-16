# A001837

> Numbers k such that phi(2k+1) < phi(2k).
> — [OEIS A001837](https://oeis.org/A001837)

Offset 1: 157, 262, 367, 412, 472, 487, 577, 682, 787, 877, 892, 907, 997, 1072, 1207, …

### Python 3 — 110 bytes

```python
D={};a=k=1
while 1:
 b=k=k+1
 for p in D.pop(k,[k]):b-=b//p;D[k+p]=D.get(k+p,[])+[p]
 b<k%2*a==print(k//2);a=b
```

**How it works**

- The sieve is the one of [A001274](../A001274/). `D` maps each number ahead of k to the primes
  found to divide it. When the loop reaches k, `D.pop(k,[k])` gives the distinct prime factors of
  k, or `[k]` when no prime was filed there, which happens exactly when k is prime. Each prime p
  is refiled at k + p, its next multiple, so every number meets all its prime factors.
- φ(k) = k·∏(1 − 1/p): starting from b = k, `b-=b//p` multiplies by (p − 1)/p, exactly, since p
  divides k and none of the primes already used.
- `a` holds φ(k − 1) and `b` is φ(k). For odd k = 2m + 1, `b<k%2*a` asks whether
  φ(2m + 1) < φ(2m); for even k it is `b<0`, always false. The chained `==print(k//2)` runs only
  when the test holds and prints m = k//2.

**Notes**

- Exact integer arithmetic; the sieve keeps one list per prime up to k, about π(k) entries.
- The b-file has 10000 terms (m up to 618832, so the sieve runs to about 1.24·10⁶); the bar is
  the whole b-file in 60 s, which takes about 7 s here. [A001836](../A001836/) and
  [A001838](../A001838/) use the same sieve.

## First 130 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 130 terms have to arrive in time.

### Python 3, 130 terms — 96 bytes

```python
from math import*
n=3
while[sum(1//gcd(n,i)-1//gcd(n-1,i)for i in range(n))<0==print(n//2)]:n+=2
```

**How it works**

- No sieve. For n = 2k + 1 the sum runs over i < n and adds `1//gcd(n,i)` (1 when
  gcd(n, i) = 1, else 0) minus `1//gcd(n-1,i)`, which is φ(2k + 1) − φ(2k): i = 0 and i = n − 1
  add nothing to the second count, since gcd(n − 1, 0) = gcd(n − 1, n − 1) = n − 1 ≥ 2.
  `<0==print(n//2)` prints k when the difference is negative.
- Each n costs 2n gcds, so k up to K costs about K² of them: 14 bytes shorter than the sieve,
  but far slower.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-16 | 110 | first entry |

**Python 3, 130 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-16 | 96 | first entry: φ by counting gcds, no sieve |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001837), CC BY-SA 4.0.
