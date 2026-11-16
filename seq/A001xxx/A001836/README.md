# A001836

> Numbers k such that phi(2k-1) < phi(2k), where phi is Euler's totient function A000010.
> — [OEIS A001836](https://oeis.org/A001836)

Offset 1: 53, 83, 158, 263, 293, 368, 578, 683, 743, 788, 878, 893, 908, 998, 1073, …

### Python 3 — 111 bytes

```python
D={};a=k=1
while 1:
 b=k=k+1
 for p in D.pop(k,[k]):b-=b//p;D[k+p]=D.get(k+p,[])+[p]
 a<~k%2*b==print(k//2);a=b
```

**How it works**

- The sieve is the one of [A001274](../A001274/). `D` maps each number ahead of k to the primes
  found to divide it. When the loop reaches k, `D.pop(k,[k])` gives the distinct prime factors of
  k, or `[k]` when no prime was filed there, which happens exactly when k is prime. Each prime p
  is refiled at k + p, its next multiple, so every number meets all its prime factors.
- φ(k) = k·∏(1 − 1/p): starting from b = k, `b-=b//p` multiplies by (p − 1)/p, exactly, since p
  divides k and none of the primes already used.
- `a` holds φ(k − 1) and `b` is φ(k). For even k, `~k%2` is 1 and `a<~k%2*b` asks whether
  φ(k − 1) < φ(k); for odd k it is `a<0`, always false. The chained `==print(k//2)` runs only when
  the test holds and prints k/2, the index with 2k − 1 and 2k in the definition.

**Notes**

- Exact integer arithmetic; the sieve keeps one list per prime up to k, about π(k) entries.
- The b-file has 1000 terms (k up to 60869); the bar is the whole b-file in 60 s, which takes
  under a second here. [A001837](../A001837/) and [A001838](../A001838/) use the same sieve.

## First 150 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 150 terms have to arrive in time.

### Python 3, 150 terms — 96 bytes

```python
from math import*
n=2
while[sum(1//gcd(n,i)-1//gcd(n-1,i)for i in range(n))>0==print(n//2)]:n+=2
```

**How it works**

- No sieve. For n = 2k the sum runs over i < n and adds `1//gcd(n,i)` (1 when gcd(n, i) = 1, else
  0) minus `1//gcd(n-1,i)`, which is φ(2k) − φ(2k − 1): i = 0 adds nothing, since gcd(n, 0) = n,
  except gcd(1, 0) = 1 at n = 2, which only makes that difference negative (k = 1 is not a term).
  `>0==print(n//2)` prints k when the difference is positive.
- Each n costs 2n gcds, so k up to K costs about K² of them: 15 bytes shorter than the sieve,
  but far slower.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-16 | 111 | first entry |

**Python 3, 150 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-16 | 96 | first entry: φ by counting gcds, no sieve |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001836), CC BY-SA 4.0.
