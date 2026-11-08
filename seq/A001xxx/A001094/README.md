# A001094

> a(n) = n + n*(n-1)*(n-2)*(n-3).
> — [OEIS A001094](https://oeis.org/A001094)

Offset 0: 0, 1, 2, 3, 28, 125, 366, 847, 1688, 3033, …

### Python 3 — 39 bytes

```python
n=0
while[print(n*((n-2)**3-n+3))]:n+=1
```

**How it works**

- n + n(n−1)(n−2)(n−3) = n·(1 + (n−1)(n−2)(n−3)), and with m = n − 2 the
  three middle factors are (m+1)·m·(m−1) = m³ − m. So the bracket is
  m³ − m + 1 = (n−2)³ − n + 3, and a(n) = n·((n−2)³ − n + 3).
- Centring the product on its middle factor replaces three brackets by one
  cube.

**Notes**

- The definition as written, `n*(n-1)*(n-2)*(n-3)+n`, makes a 44-byte
  program; pairing n(n−3) with (n−1)(n−2) gives (n² − 3n + 1)² + n − 1
  (41); walking m = n − 2 from `m=-2` instead of n costs one byte.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s.
- Siblings with five and six factors: [A001095](../A001095/) and
  [A001096](../A001096/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001094), CC BY-SA 4.0.
