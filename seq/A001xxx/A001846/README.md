# A001846

> Centered 4-dimensional orthoplex numbers (crystal ball sequence for 4-dimensional cubic lattice).
> — [OEIS A001846](https://oeis.org/A001846)

Offset 0: 1, 9, 41, 129, 321, 681, 1289, 2241, 3649, 5641, 8361, 11969, …

### Python 3 — 39 bytes

```python
k=1
while[print((k*k+7)**2//24-1)]:k+=2
```

**How it works**

- The crystal ball of the 4-dimensional cubic lattice is the Delannoy
  number D(n, 4) = Σₖ 2ᵏ·C(4, k)·C(n, k), generating function
  (1 + x)⁴/(1 − x)⁵: a quartic in n, equal to (2n⁴ + 4n³ + 10n² + 8n + 3)/3
  (the OEIS formula; two quartics that agree at n = 0 … 4 agree everywhere).
- With k = 2n + 1 this is (k⁴ + 14k² + 9)/24 = ((k² + 7)² − 40)/24. So
  (k² + 7)² = 24·a(n) + 40 = 24·(a(n) + 1) + 16, and
  ⌊(k² + 7)²/24⌋ − 1 = a(n). `k` runs over the odd numbers.

**Notes**

- The factored form `(k*k+1)*(k*k+13)//24` (the product is 24·a(n) + 4) is
  43 bytes; the crystal-ball recurrence of [A001848](../A001848/) is 49.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001846), CC BY-SA 4.0.
