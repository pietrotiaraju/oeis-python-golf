# A001117

> a(n) = 3^n - 3*2^n + 3.
> — [OEIS A001117](https://oeis.org/A001117)

Offset 0: 1, 0, 0, 6, 36, 150, 540, 1806, 5796, 18150, 55980, 171006, …

### Python 3 — 36 bytes

```python
n=0
while[print(3**n-3*2**n+3)]:n+=1
```

**How it works**

- The formula in the name, 3ⁿ − 3·2ⁿ + 3, term by term (inclusion–exclusion
  for the surjections onto 3 values, 3!·S(n, 3), except that the missing
  −0ⁿ term leaves a(0) = 1 as the OEIS has it). Exact integers.

**Notes**

- `3**n-(3<<n)+3` is the same length; keeping 3ⁿ and 2ⁿ in two variables
  (`x=y=1`, `x*=3;y*=2`) is 1 byte longer.
- The whole b-file (201 terms) prints instantly; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001117), CC BY-SA 4.0.
