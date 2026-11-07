# A000482

> Unsigned Stirling numbers of first kind s(n,5).
> — [OEIS A000482](https://oeis.org/A000482)

Offset 5: 1, 15, 175, 1960, 22449, 269325, 3416930, 45995730, 657206836, 9957703756, …

### Python 3 — 69 bytes

```python
import math
m=4
while[print(math.perm((B:=m**m)+m,m+1)//B**5%B)]:m+=1
```

**How it works**

- The unsigned Stirling numbers of the first kind are the coefficients of
  the rising factorial: x(x+1)⋯(x+n−1) = Σ_k |s(n,k)|·xᵏ.
- `math.perm(N,k)` is N(N−1)⋯(N−k+1), so with n = m + 1,
  `math.perm(B+m,m+1)` = B(B+1)⋯(B+m) is that polynomial at x = B.
- In base B its digits are the |s(n,k)|, provided every coefficient is
  below B: then `//B**5%B` reads the coefficient of B⁵. The coefficients
  are nonnegative and sum to n! = (m+1)!, and B = mᵐ > (m+1)! for m ≥ 3
  (27 > 24 at m = 3, and mᵐ/(m+1)! increases with m), so no digit
  carries.
- `B:=m**m` is set inside the first argument and reused by the rest of
  the expression; m starts at 4 for a(5) = 1.

**Notes**

- The five-column recurrence |s(n+1,k)| = n·|s(n,k)| + |s(n,k−1)|,
  `a=0;b=1;c=e=6;d=11;n=4` / `while[print(a:=a*n+b)]:b=b*n+c;c=c*n+d;…`,
  is 79 bytes. `math.prod(range(B:=m**m,B-~m))` instead of `math.perm` is
  73 bytes, and `from math import*` with `perm` is 70.
- Exact integer arithmetic, so the program is right for every n.
- The polynomial value has about (m+1)·m·log₂ m bits, so the terms slow
  down: about 420 terms in 60 s here. The b-file has 96 terms (up to
  a(100)); the bar is the whole b-file in 60 s.
- a(n) first has more than 4300 digits at n = 1559, far beyond what the
  program reaches in practice.
- [A000481](../A000481/) is the column S(n,5) of the second kind.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 79 | first entry |
| 2026-11-07 | Python 3 | 69 | read the coefficient off `math.perm(B+m,m+1)` in base B = mᵐ |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000482), CC BY-SA 4.0.
