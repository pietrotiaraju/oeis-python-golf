# A000574

> Coefficient of x^5 in expansion of (1 + x + x^2)^n.
> — [OEIS A000574](https://oeis.org/A000574)

Offset 3: 3, 16, 51, 126, 266, 504, 882, 1452, 2277, 3432, …

### Python 3 — 48 bytes

```python
n=3
while[print(~-(n*n+~n)**2*(n+12)//120)]:n+=1
```

**How it works**

- **The formula.** A degree-5 term of (1 + x + x²)ⁿ takes x from i factors
  and x² from j factors with i + 2j = 5, so (i, j) = (5, 0), (3, 1) or
  (1, 2), giving a(n) = C(n, 5) + 4·C(n, 4) + 3·C(n, 3). This equals
  C(n+1, 4)·(n + 12)/5 = (n+1)n(n−1)(n−2)(n+12)/120: both sides are
  polynomials of degree 5 and they agree at n = −1, 0, …, 5.
- **The product.** (n+1)(n−2) = n² − n − 2 and n(n−1) = n² − n, so with
  X = n² − n − 1 the four-factor product is (X − 1)(X + 1) = X² − 1.
- **The code.** `n*n+~n` is X (`~n` = −n − 1), and `~-(…)**2` is X² − 1,
  because `**` binds tighter than the unary `~` and `-`. The `//120` is an
  exact division of the integer 120·a(n).

**Notes**

- Other versions that print the same terms: the entry's form
  `math.comb(n+1,4)*(n+12)//5` with `import math`: 61 bytes (62 with
  `from math import*`); the product as `(t:=n*n-n)*(t-2)*(n+12)//120`:
  51 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 998 terms (up to a(1000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.1 s here.
- a(n) < n⁵, so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |
| 2026-11-07 | Python 3 | 48 | polynomial (X² − 1)(n + 12)/120 with X = n² − n − 1, no import |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000574), CC BY-SA 4.0.
