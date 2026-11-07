# A000741

> Number of compositions of n into 3 ordered relatively prime parts.
> — [OEIS A000741](https://oeis.org/A000741)

Offset 1: 0, 0, 1, 3, 6, 9, 15, 18, 27, 30, 45, 42, 66, 63, 84, 84, 120, 99, 153, 132, …

### Python 3 — 84 bytes

```python
L=[0];m=0
while[print(L[m])]:m+=1;L+=m*~-m//2-sum(L[d]for d in range(m)if-~m%-~d<1),
```

**How it works**

- Every composition of n into 3 positive parts has some gcd d, with d | n,
  and dividing by d gives a composition of n/d into 3 relatively prime
  parts. So Σ_{d|n} a(d) = C(n−1, 2), the number of all compositions of n
  into 3 parts (stars and bars), which is the Möbius-transform formula of
  the OEIS entry turned around:
  a(n) = C(n−1, 2) − Σ a(d) over the divisors d < n.
- `L` holds a(1), a(2), …, so with m = n−1 the new term is
  `m*~-m//2` = C(m, 2) minus the sum of `L[d]` = a(d+1) over the d < m
  with (d+1) | (m+1), written `-~m%-~d<1`.
- The recursion needs no Möbius function, and the binomial written out as
  m(m−1)/2 needs no `import math`. The list is seeded with a(1) = 0 =
  C(0, 2), and `while[print(L[m])]:` prints each term before computing
  the next one.
- Same template as [A000742](../A000742/) (4 parts) and
  [A000743](../A000743/) (5 parts).

**Notes**

- Exact integer arithmetic; the only fact used is the gcd argument above.
- Term n scans the n−1 earlier terms: the whole b-file (10000 terms) takes
  about 12 s; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000741), CC BY-SA 4.0.
