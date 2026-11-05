# A000016

> a(n) is the number of distinct (infinite) output sequences from binary
> n-stage shift register which feeds back the complement of the last stage.
> — [OEIS A000016](https://oeis.org/A000016)

Offset 0: 1, 1, 1, 2, 2, 4, 6, 10, 16, 30, 52, 94, 172, 316, 586, 1096, …

### Python 3 — 97 bytes

```python
from math import*
n=1;k=0
while[print(sum(n//(g:=gcd(j,n))%2<<g-1for j in range(n))//n)]:n+=k;k=1
```

**How it works**

- The OEIS formula is a(n) = Σ φ(d)·2^(n/d) / (2n) over the odd divisors d
  of n.
- In the cyclic group of order n there are φ(d) elements j of order d, and
  each has gcd(j, n) = n/d. So the divisor sum is a sum over j = 0…n−1 of
  2^g with g = gcd(j, n), kept only when n/g is odd. No φ is needed.
- `n//g%2<<g-1` is that term divided by 2: 2^(g−1) when n/g is odd, else 0.
  Summing over j and dividing by n gives a(n).
- a(0) = a(1) = 1, so the loop prints n = 1 twice instead of dividing by
  zero at n = 0: `k` is 0 on the first pass, then 1 (as in
  [A000011](../A000011/) and [A000013](../A000013/)).
- `1for` raises a `SyntaxWarning` on stderr, which the rules allow.

**Notes**

- It is the same sum as [A000013](../A000013/) with the opposite parity
  test: A000013 keeps 2^g when n/g is even and 2^(g−1) when it is odd.
- The whole b-file (3335 terms) takes a few seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 97 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000016), CC BY-SA 4.0.
