# A001848

> Crystal ball sequence for 6-dimensional cubic lattice.
> — [OEIS A001848](https://oeis.org/A001848)

Offset 0: 1, 13, 85, 377, 1289, 3653, 8989, 19825, 40081, 75517, 134245, …

### Python 3 — 50 bytes

```python
a=n=0;b=1
while[print(b)]:n+=1;a,b=b,a+(13*b-a)//n
```

**How it works**

- The crystal ball of the 6-dimensional cubic lattice is the Delannoy
  number D(n, 6) = Σₖ 2ᵏ·C(6, k)·C(n, k), with generating function
  A = (1 + x)⁶/(1 − x)⁷.
- A′/A = 6/(1 + x) + 7/(1 − x) = (13 + x)/(1 − x²), so
  (1 − x²)A′ = (13 + x)A. The coefficient of xⁿ⁻¹ gives
  n·a(n) − (n − 2)·a(n−2) = 13·a(n−1) + a(n−2), that is
  n·a(n) = 13·a(n−1) + (n − 1)·a(n−2)
  (for dimension d the constant is 2d + 1).
- Hence a(n) = a(n−2) + (13·a(n−1) − a(n−2))/n, where the quotient is
  a(n) − a(n−2), an integer, so `//n` is exact. `a`, `b` hold a(n−2),
  a(n−1), starting from a(−1) = 0, a(0) = 1.

**Notes**

- The same template with 7, 9 and 11 gives the dimensions 3, 4 and 5, but
  there closed forms in k = 2n + 1 are shorter ([A001845](../A001845/),
  [A001846](../A001846/), [A001847](../A001847/)). Here the polynomial is
  (k² + 9)(k⁴ + 46k² + 25)/720, 52 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001848), CC BY-SA 4.0.
