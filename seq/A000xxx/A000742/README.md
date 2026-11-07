# A000742

> Number of compositions of n into 4 ordered relatively prime parts.
> — [OEIS A000742](https://oeis.org/A000742)

Offset 4: 1, 4, 10, 20, 34, 56, 80, 120, 154, 220, 266, 360, 420, 560, 614, 816, 884, 1120, 1210, 1540, …

### Python 3 — 93 bytes

```python
L=[0]*3;m=2
while m:=m+1:L+=m*~-m*(m-2)//6-sum(L[d]for d in range(m)if-~m%-~d<1),;print(L[m])
```

**How it works**

- Dividing a composition of n into 4 parts by the gcd d of its parts
  (d | n) gives a composition of n/d into 4 relatively prime parts, so
  Σ_{d|n} a(d) = C(n−1, 3), the number of all compositions of n into 4
  parts. Turned around: a(n) = C(n−1, 3) − Σ a(d) over the divisors d < n
  (the Möbius transform of the OEIS entry, without the Möbius function).
- `L` holds a(1), a(2), …; it starts as `[0]*3`, since a(1) = a(2) = a(3)
  = 0 (fewer than 4 parts are impossible). With m = n−1 the new term is
  `m*~-m*(m-2)//6` = C(m, 3) minus the sum of `L[d]` = a(d+1) over the
  d < m with (d+1) | (m+1), written `-~m%-~d<1`.
- `while m:=m+1:` starts at n = 4, the OEIS offset. The binomial written
  out needs no `import math`.
- Same template as [A000741](../A000741/) (3 parts) and
  [A000743](../A000743/) (5 parts).

**Notes**

- Exact integer arithmetic; the only fact used is the gcd argument above.
- Term n scans the n−1 earlier terms: the whole b-file (9997 terms) takes
  about 11 s; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000742), CC BY-SA 4.0.
