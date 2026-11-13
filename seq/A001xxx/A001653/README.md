# A001653

> Numbers k such that 2*k^2 - 1 is a square.
> — [OEIS A001653](https://oeis.org/A001653)

Offset 1: 1, 5, 29, 169, 985, 5741, 33461, 195025, 1136689, 6625109, …

### Python 3 — 33 bytes

```python
a=b=1
while[print(b)]:a,b=b,6*b-a
```

**How it works**

- 2k² − 1 = x² is the negative Pell equation x² − 2k² = −1. Every
  solution in positive integers has x + k√2 = (1 + √2)^(2j+1) for some
  j ≥ 0: the units of ℤ[√2] are ±(1 + √2)^m, and the norm
  x² − 2k² = (−1)^m is −1 exactly for odd m. So the terms are the
  √2-parts of the odd powers: 1, 5, 29, 169, … (k = 0 gives −1, not a
  square).
- Going from one odd power to the next multiplies by u = (1 + √2)² =
  3 + 2√2, a root of x² − 6x + 1, so both parts satisfy
  k(j+1) = 6k(j) − k(j−1).
- The power j = −1, (1 + √2)⁻¹ = −1 + √2, has k = 1, so the window starts
  at `a=b=1`: the first pass prints k(0) = 1, then 6·1 − 1 = 5, …

**Notes**

- The entry is marked "changed"; the data and b-file are the odd-index
  Pell numbers, which is what the definition gives.
- The 2×2 step (x, k) → (3x + 4k, 2x + 3k) in place (`x+=k;k+=2*x;x+=k`)
  is 5 bytes longer than the second-order recurrence.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1000 terms; the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001653), CC BY-SA 4.0.
