# A002105

> Reduced tangent numbers: 2^n*(2^{2n} - 1)*|B_{2n}|/n, where B_n = Bernoulli numbers.
> — [OEIS A002105](https://oeis.org/A002105)

Offset 1: 1, 1, 4, 34, 496, 11056, 349504, 14873104, 819786496, 56814228736, …

### Python 3 — 79 bytes

```python
r=[t:=1]
while[r<[t%2]or print(t>>~-len(r)//2)]:r=[t:=t+x for x in[-t]+r[::-1]]
```

**How it works**

- **Formula.** 2^n(2^(2n) − 1)|B_(2n)|/n is T(n)/2^(n−1), where
  T(n) = 2^(2n)(2^(2n) − 1)|B_(2n)|/(2n) is the n-th tangent number
  [A000182](../A000182/) (the entry's A000182(n) = 2^(n−1)·a(n)).
- **Tangent numbers.** The loop is the 66-byte program of
  [A000182](../A000182/): the Seidel–Entringer triangle of the Euler
  zigzag numbers ([A000111](../A000111/)), one row per pass, each a running
  sum over the previous row read backwards (`[-t]` makes the first entry
  0). Row m ends with E(m); `r<[t%2]` skips the odd values (rows of
  secant numbers, and E(1) = 1, whose row starts [0, …] < [1]), so the
  printed values are E(0) = 1 = T(1), then T(n) = E(2n−1) from row 2n−1.
- **Shift.** Row 2n − 1 has 2n entries and row 0 has one, so
  (len(r) − 1)//2 = `~-len(r)//2` is n − 1 at every printed row, and
  `t>>~-len(r)//2` is T(n)/2^(n−1) (2^(n−1) divides T(n): the quotient
  is the integer a(n), the reduced tangent number).

**Notes**

- 13 bytes over [A000182](../A000182/). The b-file has 100 terms
  (n = 1 to 100), and the bar is the whole b-file in 60 s, which takes a
  fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002105), CC BY-SA 4.0.
