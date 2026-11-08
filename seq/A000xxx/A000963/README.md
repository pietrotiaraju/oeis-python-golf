# A000963

> The convergent sequence B_n for the ternary continued fraction (3,1;2,2) of period 2.
> — [OEIS A000963](https://oeis.org/A000963)

Offset 0: 0, 1, 0, 3, 7, 16, 49, 104, 322, 683, 2114, 4485, 13881, 29450, 91147, 193378, …

### Python 3 — 56 bytes

```python
b=k=1;a=c=0
while[print(a)]:a,b,c=b,c,a+k*c+(4-k)*b;k^=3
```

**The recurrence**

The convergents of a ternary continued fraction satisfy a three-term
recurrence X(n) = p·X(n−1) + q·X(n−2) + X(n−3), with the partial quotients
(p, q) repeating; A, B, C start from the rows of the identity,
(1,0,0), (0,1,0), (0,0,1). The data fit (p, q) = (1, 3) for odd n and
(2, 2) for even n:

- odd n: X(n) = X(n−1) + 3X(n−2) + X(n−3), e.g. B(5) = 7 + 3·3 + 0 = 16;
- even n: X(n) = 2X(n−1) + 2X(n−2) + X(n−3), e.g. B(6) = 2·16 + 2·7 + 3 = 49.

This is the OEIS g.f. for all n: two steps multiply the state by the
product of the two companion matrices, whose characteristic polynomial is
λ³ − 7λ² + 3λ − 1, so by Cayley–Hamilton every sequence of this kind
satisfies X(n) = 7X(n−2) − 3X(n−4) + X(n−6), the denominator
1 − 7x² + 3x⁴ − x⁶ of the g.f.; the first six terms agree with it, so all
terms do.

**How it works**

- `a,b,c` = X(n), X(n+1), X(n+2); the loop prints `a` and shifts in
  X(n+3) = `a+k*c+(4-k)*b`, with (p, q) = (k, 4−k).
- `k` is 1 when the new index n+3 is odd and 2 when it is even, and
  `k^=3` swaps 1 ↔ 2 each pass. It starts at 1 because X(3) has an odd
  index.
- `b=k=1;a=c=0` is the start (0, 1, 0); [A000962](../A000962/) and
  [A000964](../A000964/) are the same program from (1, 0, 0) and (0, 0, 1).

**Notes**

- Exact integer arithmetic, correct for every n.
- Writing the step as p·c + q·b with q = 4 − p, one toggling variable is
  enough. The order-6 recurrence needs six state variables and six seeds
  (71 bytes); two steps per pass with two prints is 64.
- 10525 terms print, in a fraction of a second, before a(10525) passes the
  4300-digit limit of `str()` (Python 3.11+) and stops the program.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000963), CC BY-SA 4.0.
