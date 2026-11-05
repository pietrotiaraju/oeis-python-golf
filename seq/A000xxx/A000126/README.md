# A000126

> A nonlinear binomial sum.
> — [OEIS A000126](https://oeis.org/A000126)

Offset 1: 1, 2, 4, 8, 15, 27, 47, 80, 134, 222, 365, 597, 973, 1582, 2568, …

### Python 3 — 40 bytes

```python
a=b=c=1
while[print(c)]:a,b,c=b,c,c-~c-a
```

**How it works**

- a(n) = F(n+3) − (n+1) (Henry Bottomley, on the OEIS page). From it,

  **a(n) = 2·a(n−1) − a(n−3) + 1**:

  2(F(n+2) − n) − (F(n) − (n−2)) + 1 = 2F(n+2) − F(n) − n − 1, and
  2F(n+2) − F(n) = F(n+2) + F(n+1) = F(n+3).
- The closed form holds for every integer n with Fibonacci numbers extended
  backwards, and gives a(−1) = F(2) − 0 = 1, a(0) = F(3) − 1 = 1,
  a(1) = F(4) − 2 = 1. So `a=b=c=1` is the window a(−1), a(0), a(1),
  and `c-~c-a` is 2c + 1 − a, the next term.
- `while[print(c)]:` prints the newest term in the loop condition: the
  one-element list `[None]` is always true, and it is one byte shorter than
  `while 1:print(c);`.

**Notes**

- Exact integer arithmetic and a proved identity, so the program is right
  for every n.
- The order-3 recurrence needs no counter. The order-2 one with a counter,
  a(n) = a(n−1) + a(n−2) + n − 2, is
  `a=b=1;n=0` + `while[print(b)]:a,b=b,a+b+n;n+=1`, 42 bytes; printing
  F(n+3) − (n+1) from a Fibonacci pair and a counter is longer still.
- Two variables with an affine update cannot do it: the sequence has
  characteristic polynomial (x² − x − 1)(x − 1)², degree 4, and a 2×2 affine
  map only reaches degree 3.
- The b-file has the 201 terms a(1)..a(201), all printed at once; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000126), CC BY-SA 4.0.
