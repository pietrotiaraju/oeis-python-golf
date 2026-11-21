# A002085

> From the expansion of sinh(x) / cos(x): a(n) = odd part of A002084(n).
> — [OEIS A002085](https://oeis.org/A002085)

Offset 0: 1, 1, 9, 39, 1141, 12721, 804309, 17113719, 1886573641, 65373260641, …

### Python 3 — 80 bytes

```python
r=[1,s:=1]
while[print(s//(s&-s))]:
 for s in 0,1:r=[s:=s+x for x in[0]+r[::-1]]
```

**How it works**

- **A002084.** The triangle is the one of [A002084](../A002084/): the
  boustrophedon triangle T(m, 0) = u_m, T(m, k) = T(m, k−1) + T(m−1, m−k),
  whose diagonal has e.g.f. (sec x + tan x)·U(x), started from
  u = (0, 1, 0, 1, …), the coefficients of U = sinh x. Its odd diagonal
  T(2n+1, 2n+1) is the coefficient of x^(2n+1)/(2n+1)! in
  sec x·sinh x = sinh x/cos x, the A002084 term, and it is `s` after each
  pass.
- **Odd part.** `s&-s` is the lowest set bit of s (two's complement), so
  `s//(s&-s)` is the odd part, the definition in the name.

**Notes**

- The odd part divides A002084(n) by 2^(n + n mod 2) on all 51 terms of
  the b-file, as in Somos's PARI program, which uses
  sinh(x/2)/cos(x/2); the program follows the name and takes the odd part
  directly.
- The b-file has 51 terms (n = 0 to 50), and the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 80 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002085), CC BY-SA 4.0.
