# A001983

> Numbers that are the sum of 2 distinct squares: of form x^2 + y^2 with 0 <= x < y.
> — [OEIS A001983](https://oeis.org/A001983)

Offset 1: 1, 4, 5, 9, 10, 13, 16, 17, 20, 25, 26, 29, 34, 36, 37, 40, 41, 45, 49, …

### Python 3 — 76 bytes

```python
n=0
while[n in{a*a+b*b for a in range(n+1)for b in range(a)}==print(n)]:n+=1
```

**How it works**

- For each n the set comprehension lists every a² + b² with
  0 ≤ b < a ≤ n, and n is printed when it is in that set. A sum x² + y²
  with x < y equal to n has y ≤ √n ≤ n, so it appears as (b, a) = (x, y)
  and nothing is missed; 0 is never printed (it needs a = b = 0).
- `n in S==print(n)` is a chained comparison: `print` runs only when
  `n in S` holds, and the list `[False]` keeps the loop going.

**Notes**

- Exact integer arithmetic and an exhaustive search, so the program is
  right for every n.
- The set has about n²/2 elements, so the time grows like n³. Keeping
  only a² ≤ n (`for a in range(n+1)if a*a<=n`) is 10 bytes longer and
  prints the whole b-file in about a second; the loops of
  [A001974](../A001974/) do that for three squares, where the short form
  would be far too slow.
- About 250 terms (up to 784) in 24 s here. The b-file has 1000 terms (up
  to 3464); the bar is 240 terms (a(240) = 746) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001983), CC BY-SA 4.0.
