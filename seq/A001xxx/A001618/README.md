# A001618

> Nearest integer to 2*n*log(n).
> — [OEIS A001618](https://oeis.org/A001618)

Offset 0: 0, 0, 3, 7, 11, 16, 22, 27, 33, 40, 46, 53, 60, 67, 74, 81, 89, 96, 104, 112, …

### Python 3 — 159 bytes

```python
from decimal import*
getcontext().prec=MAX_PREC
n=0;p=1
while 1:v=2*n*Context(p).ln(n or 1);a,b=round(v-(w:=v.scaleb(1-p))),round(v+w);p+=b-a;n+=a==b!=print(a)
```

**How it works**

- `Context(p).ln(n)` is ln n rounded to p significant digits. The
  `decimal` documentation states that `ln` is correctly rounded, so the
  error is at most half a unit in the last place, which is at most
  ½·10¹⁻ᵖ·x for the result x. Multiplying by 2n (exactly), the true
  2n·ln n lies within v·10¹⁻ᵖ of v = 2n·x: `w=v.scaleb(1-p)` is that
  bound.
- If v − w and v + w round to the same integer, every number in between
  does, and so does 2n·ln n: the program prints it and moves on
  (`n+=a==b!=print(a)` prints and steps n only when a = b). Otherwise
  `p+=b-a` raises the precision and the same n is tried again.
- The loop always ends: for n ≥ 2, 2n·ln n is irrational (n would be
  e^(rational), which by Lindemann's theorem is transcendental), so it is
  never a half-integer, and the interval eventually avoids every
  half-integer. The precision only grows; over the whole b-file it climbs
  to just 12 digits.
- `getcontext().prec=MAX_PREC` makes every other operation (the product,
  `scaleb`, the sums and `round`) exact. Ties to even in `round` do not
  matter: an endpoint can be a half-integer, but 2n·ln n cannot, and the two
  endpoints agree only when the whole interval rounds the same way.
- n = 0 uses `ln(n or 1)` = 0, so a(0) = 0, the value 2n·log n tends to;
  a(1) = 0 exactly.

**Notes**

- The arithmetic is certified at every step, so the program is right for
  every n.
- The whole b-file (100001 terms) prints in about 4 s here; the bar is the
  whole b-file.
- Integer-only versions (ln 2 and atanh series with error bounds) are
  longer; the `decimal` module is the cheapest correctly rounded logarithm
  in the standard library.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 159 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001618), CC BY-SA 4.0.
