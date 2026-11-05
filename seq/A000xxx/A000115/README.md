# A000115

> Denumerants: Expansion of 1/((1-x)*(1-x^2)*(1-x^5)).
> — [OEIS A000115](https://oeis.org/A000115)

Offset 0: 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 16, 18, 20, 22, 24, 26, 29, 31, …

The number of ways to make n out of parts 1, 2 and 5 (coins of 1, 2 and 5).

### Python 3 — 34 bytes

```python
n=4
while[print((n*n+4)//20)]:n+=1
```

**How it works**

- The OEIS formula a(n) = round((n+4)²/20). Here `n` stands for n + 4,
  so it starts at 4.
- Rounding without floats: (n+4)² mod 20 is always one of 0, 1, 4, 5, 9
  or 16, so adding any c from 4 to 10 before flooring rounds the same
  way (9 + c must stay below 20, 16 + c must reach it). The usual
  `+10` becomes the one-digit `+4`.
- `while[print(…)]` prints and loops forever, because `[None]` is a
  non-empty list.

**Notes**

- Why the formula holds for every n: the g.f. denominator
  (1−x)(1−x²)(1−x⁵) divides (1−x¹⁰)³, so on each residue class mod 10
  a(10m + j) is a polynomial in m of degree at most 2. The formula has
  the same shape, since ((n+14)² + 4) − ((n+4)² + 4) = 20(n + 9) gives
  f(n + 10) = f(n) + n + 9 exactly. Two such polynomials that agree at
  m = 0, 1, 2 are equal, so agreement on n = 0 to 29, which the b-file
  check covers, proves it for all n. A check against the g.f. confirmed
  that exactly the constants 4 to 10 work.
- `while 1:print(…);n+=1` is 1 byte longer, and a walrus inside the
  print (`n=3`, `(n:=n+1)**2`) costs more than the separate `n+=1`. The
  PARI form `(n*n+8*n+26)//20` counting from 0 is longer, and
  `round(n*n/20)` is longer and goes through floats.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10001 terms (n = 0 to 10000); they print in well under
  a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000115), CC BY-SA 4.0.
