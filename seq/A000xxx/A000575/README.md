# A000575

> Tenth column of quintinomial coefficients.
> — [OEIS A000575](https://oeis.org/A000575)

Offset 0: 10, 80, 365, 1246, 3535, 8800, 19855, 41470, 81367, 151580, …

a(n) is the coefficient of x⁹ in (1 + x + x² + x³ + x⁴)^(n+3) (Joerg Arndt's
formula line on the entry).

### Python 3 — 66 bytes

```python
from math import*
m=3
while[print(comb(m+8,9)-m*comb(m+3,4))]:m+=1
```

**How it works**

- **The formula.** Write m = n + 3 and 1 + x + … + x⁴ = (1 − x⁵)/(1 − x).
  Then (1 − x⁵)^m = 1 − m·x⁵ + …, and (1 − x)^(−m) has coefficient
  C(m−1+k, k) at x^k. Only the x⁰ and x⁵ terms of the first factor reach
  degree 9, so a(n) = C(m+8, 9) − m·C(m+3, 4).
- **The shift.** Running the loop on m instead of n turns the entry's
  `comb(n+11,9)-(n+3)*comb(n+6,4)` into `comb(m+8,9)-m*comb(m+3,4)`,
  7 bytes shorter; at m = 3 it gives C(11, 9) − 3·C(6, 4) = 55 − 45 = 10.
- `comb` is used twice, so `from math import*` beats `import math`.

**Notes**

- Other versions that print the same terms: the same difference in n,
  `n=0` / `while[print(comb(n+11,9)-(n+3)*comb(n+6,4))]:n+=1`: 71 bytes;
  the factored form C(n+6, 6)·(n³ + 42n² + 677n + 5040)/504 from the entry,
  with `import math` and Horner's rule: 80 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.1 s here.
- a(n) is a polynomial of degree 9 in n, so the 4300-digit int-to-str limit
  is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 71 | first entry |
| 2026-11-07 | Python 3 | 66 | loop on m = n + 3 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000575), CC BY-SA 4.0.
