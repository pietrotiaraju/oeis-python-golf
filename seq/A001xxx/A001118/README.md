# A001118

> Number of labeled ordered set partitions into 5 parts for n>=1, a(0)=1.
> — [OEIS A001118](https://oeis.org/A001118)

Offset 0: 1, 0, 0, 0, 0, 120, 1800, 16800, 126000, 834120, 5103000, …

### Python 3 — 51 bytes

```python
n=0
while[print(5**n-5*4**n+10*(3**n-2**n)+5)]:n+=1
```

**How it works**

- a(n) = Σ_{i=0}^{4} (−1)^i·C(5, i)·(5 − i)ⁿ = 5ⁿ − 5·4ⁿ + 10·3ⁿ − 10·2ⁿ + 5,
  the inclusion–exclusion count of surjections onto 5 values with the i = 5
  term (−0ⁿ) left out. That term is exactly what turns 5!·S(0, 5) = 0 into
  a(0) = 1, so the formula needs no special case.
- The two tens share a factor: `10*(3**n-2**n)` is 1 byte under
  `10*3**n-10*2**n`.

**Notes**

- The whole b-file (1001 terms) prints instantly; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001118), CC BY-SA 4.0.
