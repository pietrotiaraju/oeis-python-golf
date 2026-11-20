# A002095

> Number of partitions of n into nonprime parts.
> — [OEIS A002095](https://oeis.org/A002095)

Offset 0: 1, 1, 1, 1, 2, 2, 3, 3, 5, 6, 8, 8, 12, 13, 17, 19, …

### Python 3 — 99 bytes

```python
a=[1];*P,F,n=1,0
while[print(a[-1])]:n-=1;P+=[n][F%-n:];F*=n*n;a+=sum(d*sum(a[d::d])for d in P)//n,
```

**How it works**

- The generating function is ∏ 1/(1 − x^d) over the nonprime d (1 and the
  composites): the Euler transform of the nonprime indicator. Its
  logarithmic derivative gives n·a(n) = Σ_{d ≤ n nonprime} d·Σ_{j ≥ 1} a(n − jd).
- This is the [A000607](../../A000xxx/A000607/) record (partitions into primes)
  with the complementary list. The counter runs downwards, n = −m; `P` holds
  the negated nonprimes d = −k ≤ m, and `a[d::d]` starts at index m − k of
  the list a(0), …, a(m − 1) and steps back by k: a(m − k), a(m − 2k), … .
  Each product d·Σ is negative, and `//n` with the negative n divides it
  exactly.
- F = ((m − 1)!)² (Wilson), so F mod m is 1 for a prime m and 0 for every
  nonprime m (m = 1 included, and m = 4, where F = 36). `[n][F%-n:]` is
  `[n]` when that residue is 0 and `[]` when it is 1: 3 bytes over
  A000607's `F%-n*[n]`, which keeps the primes instead.
- The starred assignment sets P = [], F = 1, n = 0.

**Notes**

- Exact integer arithmetic throughout: the division is exact because the
  identity is, and Wilson's theorem decides primality.
- The b-file has 5001 terms (n = 0 to 5000); the program prints all of them
  in about 9 s here, so the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 99 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002095), CC BY-SA 4.0.
