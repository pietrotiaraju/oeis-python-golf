# A000743

> Number of compositions of n into 5 ordered relatively prime parts.
> — [OEIS A000743](https://oeis.org/A000743)

Offset 5: 1, 5, 15, 35, 70, 125, 210, 325, 495, 700, 1000, 1330, 1820, 2305, 3060, 3750, 4830, 5775, 7315, 8490, …

### Python 3 — 100 bytes

```python
L=[0]*4;m=3
while m:=m+1:L+=m*~-m*(m-2)*(m-3)//24-sum(L[d]for d in range(m)if-~m%-~d<1),;print(L[m])
```

**How it works**

- Dividing a composition of n into 5 parts by the gcd d of its parts
  (d | n) gives a composition of n/d into 5 relatively prime parts, so
  Σ_{d|n} a(d) = C(n−1, 4), the number of all compositions of n into 5
  parts. Turned around: a(n) = C(n−1, 4) − Σ a(d) over the divisors d < n
  (the Möbius transform of the OEIS entry, without the Möbius function).
- `L` holds a(1), a(2), …; it starts as `[0]*4`, since a(1) = … = a(4) = 0.
  With m = n−1 the new term is `m*~-m*(m-2)*(m-3)//24` = C(m, 4) minus
  the sum of `L[d]` = a(d+1) over the d < m with (d+1) | (m+1), written
  `-~m%-~d<1`.
- `while m:=m+1:` starts at n = 5, the OEIS offset. Writing the binomial
  out (22 bytes) still beats `from math import*` plus `comb(m,4)`.
- Same template as [A000741](../A000741/) (3 parts) and
  [A000742](../A000742/) (4 parts).

**Notes**

- Exact integer arithmetic; the only fact used is the gcd argument above.
- Term n scans the n−1 earlier terms: the whole b-file (9996 terms) takes
  about 11 s; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 100 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000743), CC BY-SA 4.0.
