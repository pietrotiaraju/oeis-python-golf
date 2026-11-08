# A000956

> A sequence satisfying (a(2n+1) + 1)^3 = Sum_{k=1..2n+1} a(k)^3.
> — [OEIS A000956](https://oeis.org/A000956)

Offset 1: 2, 17, 40, 5126, 211888, 134691268742, 28539643139633848, …

### Python 3 — 60 bytes

```python
x=1
while[print(x+1//x),print(y:=3*x*x+8*x+6)]:x=-~x*(x+y+2)
```

**The construction**

The OEIS formula (Sean A. Irvine) is a(1), a(2), a(3) = 2, 17, 40 and then

a(2n+2) = 3x² + 8x + 6, a(2n+3) = 3x³ + 12x² + 17x + 8, with x = a(2n+1).

The second polynomial is (x+1)(3x²+9x+8) = (x+1)(x+y+2), with y the new
even term; call it z. The identity (x+1)³ + y³ + z³ = (z+1)³ holds for
every x (it reduces to (x+1)³ + y³ = 3z² + 3z + 1, two equal degree-6
polynomials), so if the cubes up to x sum to (x+1)³, the
cubes up to z sum to (z+1)³.

**How it works**

- `x` is the cube root of the sum so far, minus 1. The sum starts at
  2³, so `x=1`, and the formula at x = 1 gives exactly 17 and 40: the given
  a(2), a(3) come out of the loop.
- Only a(1) = 2 = x + 1 differs from x: `x+1//x` adds 1 when x = 1 and 0
  for every later x ≥ 40.
- Each pass prints x and y = 3x² + 8x + 6 (kept with `:=`), then
  `x=-~x*(x+y+2)` makes the next odd term (x+1)(x+y+2).

**Notes**

- Exact integer arithmetic, correct for every n.
- 17 terms print; a(18) has more than 4300 digits and `str()` stops the
  program with a `ValueError` (Python 3.11+ limit).
- The b-file has 14 terms; the bar is all 14.
- [A000955](../A000955/) is the same loop from x = 0, with `x or 1`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000956), CC BY-SA 4.0.
