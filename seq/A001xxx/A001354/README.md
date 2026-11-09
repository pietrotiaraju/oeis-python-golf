# A001354

> Coordination sequence for hyperbolic tessellation 3^7 (from triangle group (2,3,7)).
> — [OEIS A001354](https://oeis.org/A001354)

Offset 0: 1, 7, 21, 56, 147, 385, 1008, 2639, 6909, 18088, 47355, 123977, 324576, …

### Python 3 — 38 bytes

```python
a=0;b=7
while[print(a or 1)]:a+=b;b+=a
```

**How it works**

- The growth series of the {3,7} tessellation is
  (1 + 4x + x²)/(1 − 3x + x²) = 1 + 7x/(1 − 3x + x²), so a(n) = 7·F(2n)
  for n ≥ 1 (F = Fibonacci) and a(0) = 1.
- `a+=b;b+=a` steps a pair of consecutive Fibonacci numbers two places at
  once: from 7·(F(2n), F(2n+1)) it makes 7·(F(2n+2), F(2n+3)). Started at
  7·(F(0), F(1)) = (0, 7), `a` runs through 7·F(2n), and `or 1` prints the
  first 0 as a(0) = 1.

**Notes**

- The walrus form `a=b=-7` / `while[print((a:=a-b)or 1)]:b-=a` is also
  38 bytes. Some nonlinear touch is needed: 1, 7, 21 break the order-2
  recurrence a(n+1) = 3a(n) − a(n−1) that every later term follows.
- The partial sums are [A001360](../A001360/) = 7·F(2n+1) − 6.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (a(0) to a(1000)); the whole of it prints
  instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001354), CC BY-SA 4.0.
