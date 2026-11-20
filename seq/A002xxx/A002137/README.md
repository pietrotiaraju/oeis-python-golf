# A002137

> Number of n X n symmetric matrices with nonnegative integer entries, trace 0 and all row sums 2.
> — [OEIS A002137](https://oeis.org/A002137)

Offset 0: 1, 0, 1, 1, 6, 22, 130, 822, 6202, 52552, 499194, 5238370, 60222844, …

### Python 3 — 61 bytes

```python
x=y=m=0;z=1
while[print(z)]:x,y,z=y,z,m*(z+y)-m*~-m*x//2;m+=1
```

**How it works**

- **E.g.f.** A symmetric n×n matrix with zero diagonal and row sums 2 is
  a loopless multigraph on n labeled vertices, every vertex of degree 2:
  its components are double edges (an entry 2; x²/2) and cycles of length
  k ≥ 3, each counted once for its two directions ((k−1)!/2 labelings).
  So the e.g.f. is exp(x²/2 + Σ_(k≥3) x^k/(2k)) =
  (1−x)^(−1/2)·exp(−x/2 + x²/4), the entry's formula.
- **Recurrence.** Its log-derivative is x(2 − x)/(2(1 − x)), so
  2(1−x)F′ = x(2−x)F, and on coefficients
  a(n) = (n−1)(a(n−1) + a(n−2)) − (n−1)(n−2)/2·a(n−3), the formula in the
  entry.
- **Loop.** As in [A002135](../A002135/): the state is
  (x, y, z) = (a(m−2), a(m−1), a(m)) from (0, 0, 1) (phantom zeros give
  a(1) = 0 and a(2) = 1), m = n − 1, and the new term is
  m·(z + y) − m(m−1)·x/2, exact because m(m−1) is even.

**Notes**

- [A002135](../A002135/) is the binomial transform of this sequence (loops
  allowed on the diagonal there).
- a(n) has about n·log₁₀ n digits; the b-file has 101 terms (n = 0 to
  100), and the bar is the whole b-file in 60 s, which takes a fraction of
  a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002137), CC BY-SA 4.0.
