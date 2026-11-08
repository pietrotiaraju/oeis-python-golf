# A001057

> Canonical enumeration of integers: interleaved positive and negative integers with zero prepended.
> — [OEIS A001057](https://oeis.org/A001057)

Offset 0: 0, 1, -1, 2, -2, 3, -3, 4, -4, 5, …

### Python 3 — 29 bytes

```python
n=0
while[print(n)]:n=(n<1)-n
```

**How it works**

- The map n ↦ (n<1) − n sends 0 → 1 → −1 → 2 → −2 → 3 → …: a positive
  term becomes its negative, and a term ≤ 0 becomes 1 minus itself, the
  next positive integer.
- `n<1` is a `bool`, which adds as 0 or 1, so one comparison does the case
  split; the value is the whole state, with no index.

**Notes**

- The closed form a(n) = (−1)ⁿ⁺¹·⌈n/2⌉ needs a counter and a sign and is
  longer; `n=-n+(n<1)` is one byte more than `n=(n<1)-n`.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s.
- The same step enumerates k = 0, ±1, ±2, … for generalized polygonal
  numbers, though for the octagonal ones [A001082](../A001082/) a direct
  walk is shorter.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001057), CC BY-SA 4.0.
