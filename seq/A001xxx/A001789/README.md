# A001789

> a(n) = binomial(n,3)*2^(n-3).
> — [OEIS A001789](https://oeis.org/A001789)

Offset 3: 1, 8, 40, 160, 560, 1792, 5376, 15360, 42240, 112640, 292864, 745472, …

### Python 3 — 38 bytes

```python
m=2
while[print((m**3-m<<m)//24)]:m+=1
```

**How it works**

- The loop runs over m = n − 1, from 2 (n = 3, the offset). Then
  m³ − m = (m − 1)m(m + 1) = (n − 2)(n − 1)n = 6·C(n, 3).
- `<<m` multiplies by 2ᵐ = 2ⁿ⁻¹ and `//24` divides by 6·4, leaving
  C(n, 3)·2ⁿ⁻³. The division is exact: 6 divides m³ − m and 4 divides 2ᵐ for
  m ≥ 2. The parentheses are needed because `//` binds tighter than `<<`.

**Notes**

- `(m**3-m)//6<<m-2` is one byte longer; in n itself,
  `(n*~-n*(n-2)<<n)//48` is 5 bytes longer.
- Exact integer arithmetic, so the program is right for every n.
- Relatives: [A001787](../A001787/) n·2ⁿ⁻¹, [A001788](../A001788/)
  n(n + 1)·2ⁿ⁻² = C(n + 1, 2)·2ⁿ⁻¹.
- The b-file has 498 terms (n = 3 to 500); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001789), CC BY-SA 4.0.
