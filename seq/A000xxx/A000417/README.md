# A000417

> Euler transform of A000389.
> — [OEIS A000417](https://oeis.org/A000417)

Offset 1: 1, 7, 28, 105, 357, 1232, 4067, 13301, 42357, 132845, …

A000389 is C(k, 5) with offset 5, so here the weights are c(k) = C(k+4, 5)
for k ≥ 1, and a(n) is the coefficient of xⁿ in Π_{k≥1} (1 − xᵏ)^(−c(k)).

### Python 3 — 108 bytes

```python
import math
*a,n=1,0
while 1:n-=1;print(x:=sum(d*math.comb(4-d,5)*sum(a[d::d])for d in range(n,0))//n);a+=x,
```

**How it works**

- Logarithmic differentiation of the product gives, with a(0) = 1,
  m·a(m) = Σ_{k=1}^{m} k·c(k)·Σ_{j≥1} a(m − jk) (the divisor sums of the
  usual Euler-transform recurrence, with the order of summation swapped).
- This is the [A000041](../A000041/) loop: `a` holds a(0), …, a(m−1) and
  `n` is −m, so for d = −k the slice `a[d::d]` is a(m−k), a(m−2k), … .
  `math.comb(4-d,5)` is C(k+4, 5) = c(k), and the signs of `d` and `n`
  cancel in the division, which is exact because the left side is m·a(m).
- `*a,n=1,0` sets `a=[1]` and `n=0` in one assignment, and
  `print(x:=…)` prints the new term before `a+=x,` appends it; output
  starts at a(1).

**Notes**

- Appending first and then `print(a[-1])` is 1 byte longer, and so is
  printing in a `while[print(a[-1])]:` header, which needs the start
  `*a,n=1,1,-1`. `from math import*` costs one more byte than
  `import math`.
- Exact integer arithmetic, so the program is right for every n.
- Term m costs about m·ln m additions: the whole b-file prints in about
  2 s here and about 5000 terms in 60 s. The b-file has 1000 terms (up to
  a(1000)); the bar is the whole b-file in 60 s.
- a(n) has about 870 digits at n = 3800 and the digit count grows like
  n^(6/7), so the 4300-digit limit is out of reach (it would come near
  n = 25 000).
- [A000428](../A000428/) is the same program with C(k+5, 6).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 161 | first entry |
| 2026-11-06 | Python 3 | 160 | use a shorter math import |
| 2026-11-06 | Python 3 | 111 | reorder the Euler-transform sum and use one coefficient list |
| 2026-11-07 | Python 3 | 108 | `import math`, `*a,n=1,0` and a walrus print |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000417), CC BY-SA 4.0.
