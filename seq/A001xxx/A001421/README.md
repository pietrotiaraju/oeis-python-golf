# A001421

> a(n) = (6*n)!/((n!)^3*(3*n)!).
> — [OEIS A001421](https://oeis.org/A001421)

Offset 0: 1, 120, 83160, 81681600, 93699005400, 117386113965120, 155667030019300800, …

### Python 3 — 56 bytes

```python
a=k=1
while[print(a)]:a=a*192*k*(9*k*k-4)//(k+1)**3;k+=2
```

**How it works**

- a(n)/a(n−1) = (6n)(6n−1)⋯(6n−5) / (n³ · 3n(3n−1)(3n−2)), and
  6n(6n−2)(6n−4) = 8 · 3n(3n−1)(3n−2), so the ratio is
  8(6n−1)(6n−3)(6n−5)/n³.
- The loop runs k = 2n − 1 = 1, 3, 5, …, where 6n − 1 = 3k + 2,
  6n − 3 = 3k, 6n − 5 = 3k − 2 and n³ = (k+1)³/8, so the ratio becomes
  192k(9k² − 4)/(k+1)³ and the step is `a=a*192*k*(9*k*k-4)//(k+1)**3`.
  It is exact because the quotient is the integer a(n). `a=k=1` starts at
  a(0) = 1 with k = 1 for the step to a(1) = 120.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- In terms of n itself the same step is
  `a=a*24*(2*n-1)*(36*n*n-36*n+5)//n**3` (7 bytes longer); the product of
  three `math.comb`s or of factorials is longer still.
- The b-file has 311 terms (n = 0 to 310); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001421), CC BY-SA 4.0.
