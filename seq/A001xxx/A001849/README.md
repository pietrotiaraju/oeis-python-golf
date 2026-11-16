# A001849

> Crystal ball sequence for 7-dimensional cubic lattice.
> — [OEIS A001849](https://oeis.org/A001849)

Offset 0: 1, 15, 113, 575, 2241, 7183, 19825, 48639, 108545, 224143, …

### Python 3 — 50 bytes

```python
a=n=0;b=1
while[print(b)]:n+=1;a,b=b,a+(15*b-a)//n
```

**How it works**

- The crystal ball of the 7-dimensional cubic lattice is the Delannoy
  number D(n, 7) = Σₖ 2ᵏ·C(7, k)·C(n, k), with generating function
  A = (1 + x)⁷/(1 − x)⁸.
- A′/A = 7/(1 + x) + 8/(1 − x) = (15 + x)/(1 − x²), so
  (1 − x²)A′ = (15 + x)A. The coefficient of xⁿ⁻¹ gives
  n·a(n) − (n − 2)·a(n−2) = 15·a(n−1) + a(n−2), that is
  n·a(n) = 15·a(n−1) + (n − 1)·a(n−2)
  (for dimension d the constant is 2d + 1).
- Hence a(n) = a(n−2) + (15·a(n−1) − a(n−2))/n, where the quotient is
  a(n) − a(n−2), an integer, so `//n` is exact. `a`, `b` hold a(n−2),
  a(n−1), starting from a(−1) = 0, a(0) = 1.

**Notes**

- The polynomial in k = 2n + 1,
  k(k⁶ + 91k⁴ + 1519k² + 3429)/5040, is 59 bytes. See
  [A001848](../A001848/) for the other dimensions.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001849), CC BY-SA 4.0.
