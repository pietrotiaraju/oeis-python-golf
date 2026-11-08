# A000955

> A sequence satisfying (a(2n+1) + 1)^3 = Sum_{k=1..2n+1} a(k)^3.
> — [OEIS A000955](https://oeis.org/A000955)

Offset 1: 1, 6, 8, 262, 2448, 17997702, 44082372248, 5829766629386380698502, …

### Python 3 — 60 bytes

```python
x=0
while[print(x or 1),print(y:=3*x*x+8*x+6)]:x=-~x*(x+y+2)
```

**The construction**

The OEIS formula (Sean A. Irvine) is a(1), a(2), a(3) = 1, 6, 8 and then

a(2n+2) = 3x² + 8x + 6, a(2n+3) = 3x³ + 12x² + 17x + 8, with x = a(2n+1).

The second polynomial factors as (x+1)(3x²+9x+8) = (x+1)(x+y+2), with y the
new even term. Write z for it. Then

(x+1)³ + y³ + z³ = (z+1)³

holds for every x: it says (x+1)³ + y³ = 3z² + 3z + 1, and both sides are
the same degree-6 polynomial in x (expand them). So if the cubes up to
a(2n+1) = x sum to (x+1)³, adding y³ and z³ makes the sum (z+1)³: the
property passes from x to z.

**How it works**

- `x` is always the cube root of the sum so far, minus 1. At the start
  the sum is 1³, so `x=0`, and then the first two steps of the formula give
  6 and 8: the given a(2), a(3) are just the formula applied to x = 0.
  So one loop does everything; only a(1) = 1 ≠ x needs `x or 1` (x is
  positive afterwards).
- Each pass prints the odd term x and the even term y (kept with `:=`),
  then `x=-~x*(x+y+2)` is the next odd term, (x+1)(x+y+2).
- Both prints sit in the `while[…]` test; the list is never empty.

**Notes**

- Exact integer arithmetic, correct for every n.
- The terms roughly cube every two steps: 17 terms print, then a(18)
  passes the 4300-digit limit of `str()` (Python 3.11+) and the program
  stops with a `ValueError`.
- The b-file has 10 terms (the OEIS data); the bar is all 10.
- [A000956](../A000956/) is the same loop from x = 1.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000955), CC BY-SA 4.0.
