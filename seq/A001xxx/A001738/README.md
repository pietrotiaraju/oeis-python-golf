# A001738

> a(n) = n^2 written in base 3.
> — [OEIS A001738](https://oeis.org/A001738)

Offset 0: 0, 1, 11, 100, 121, 221, 1100, 1211, 2101, 10000, 10201, 11111, …

### Python 3 — 61 bytes

```python
f=lambda m:m and m%3+10*f(m//3)
n=0
while[print(f(n*n))]:n+=1
```

**How it works**

- `f(m)` writes m in base 3 and reads the digits back as a decimal number:
  the last base-3 digit is m mod 3, and the digits before it are those of
  ⌊m/3⌋, shifted one decimal place, so f(m) = (m mod 3) + 10·f(⌊m/3⌋), with
  f(0) = 0 ending the recursion (`m and …`). For n = 0 that gives the term
  0.
- The loop prints f(n²) for n = 0, 1, 2, …; `while[print(…)]:` is always
  true because the list is never empty.

**Notes**

- The same lambda as in [A001357](../A001357/); the other bases of this
  family are [A001737](../A001737/), [A001739](../A001739/),
  [A001740](../A001740/), [A001741](../A001741/). Python's format specs only
  know bases 2, 8 and 16.
- Exact integer arithmetic, correct for every n. The recursion goes one
  level per base-3 digit, a few dozen levels for the b-file. The b-file has
  1001 terms (n = 0 to 1000); the bar is the whole b-file, printed in a
  fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001738), CC BY-SA 4.0.
