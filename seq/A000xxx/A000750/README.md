# A000750

> Expansion of bracket function.
> — [OEIS A000750](https://oeis.org/A000750)

Offset 0: 1, -5, 15, -35, 70, -125, 200, -275, 275, 0, -1000, 3625, -9500, 21250, …

### Python 3 — 55 bytes

```python
a=y=w=z=1
while[print(a)]:z=a+w-5*z;w=z-w+y;y=w-y;a=y-a
```

**How it works**

- The g.f. is 1/Q with Q = (1 + x)⁵ − x⁵ = 1 + 5x + 10x² + 10x³ + 5x⁴
  = 1 + 5x·(1 + x)(1 + x + x²). The order-4 recurrence needs four numbers
  of state; the program keeps the coefficients at n of four multiples of
  the g.f. A:
  a = A, y = (1 + x)A, w = (1 + x)²A and z = (1 + x)(1 + x + x²)A
  = (1 + x)w − x·y. All four start at 1, so the start is `a=y=w=z=1`.
- Since A = 1 − 5x·z, a(n+1) = −5z(n), and then
  z(n+1) = a(n+1) + 2a(n) + 2a(n−1) + a(n−2) = −5z + a + w.
  The other three follow from their definitions, top down, each from the
  new value above it and its own old value: w′ = z′ − w + y,
  y′ = w′ − y and a′ = y′ − a. Each statement reads only values it may
  still use, so plain assignments in this order need no tuple.
- The tuple shift `a,b,c,d=b,c,d,-5*(a+d+2*(b+c))` with `a=b=c=0;d=1` is
  58 bytes. A search over all four-statement chains with coefficients
  in {−1, 0, 1} and one self-coefficient ±5 found 55 bytes as the
  minimum.

**Notes**

- Exact integer arithmetic. The roots of t⁴ + 5t³ + 10t² + 10t + 5 are
  ζ − 1 for the primitive fifth roots of unity ζ, so |a(n)| grows like
  (2 sin 2π/5)ⁿ ≈ 1.902ⁿ and has about 0.28n digits: the 4300-digit
  int-to-str limit is reached only near n = 15 400, after the b-file.
- The whole b-file (3001 terms) prints in well under a second; the bar is
  the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000750), CC BY-SA 4.0.
