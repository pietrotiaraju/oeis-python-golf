# A001847

> Crystal ball sequence for 5-dimensional cubic lattice.
> — [OEIS A001847](https://oeis.org/A001847)

Offset 0: 1, 11, 61, 231, 681, 1683, 3653, 7183, 13073, 22363, 36365, …

### Python 3 — 46 bytes

```python
k=1
while[print(k*(k**4+30*k*k+89)//120)]:k+=2
```

**How it works**

- The crystal ball of the 5-dimensional cubic lattice is the Delannoy
  number D(n, 5) = Σₖ 2ᵏ·C(5, k)·C(n, k), generating function
  (1 + x)⁵/(1 − x)⁶: a quintic in n, equal to
  (4n⁵ + 10n⁴ + 40n³ + 50n² + 46n + 15)/15 (the OEIS formula; two quintics
  that agree at n = 0 … 5 agree everywhere).
- With k = 2n + 1 the quintic is odd in k: a(n) = k(k⁴ + 30k² + 89)/120, an
  exact division. `k` runs over the odd numbers.

**Notes**

- The crystal-ball recurrence of [A001848](../A001848/),
  `a,b=b,a+(11*b-a)//n`, is 50 bytes here.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001847), CC BY-SA 4.0.
