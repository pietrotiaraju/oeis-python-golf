# A001792

> a(n) = (n+2)*2^(n-1).
> — [OEIS A001792](https://oeis.org/A001792)

Offset 0: 1, 3, 8, 20, 48, 112, 256, 576, 1280, 2816, 6144, 13312, 28672, …

### Python 3 — 30 bytes

```python
m=2
while[print(m<<m>>3)]:m+=1
```

**How it works**

- The loop runs over m = n + 2, from 2. Then (n + 2)·2ⁿ⁻¹ = m·2ᵐ⁻³:
  `m<<m` is m·2ᵐ and `>>3` divides by 8.
- The division is exact: m·2ᵐ is a multiple of 8 for every m ≥ 2
  (m = 2 gives 8).

**Notes**

- Counting in n, `n+2<<n>>1`, is 2 bytes longer.
- Exact integer arithmetic, so the program is right for every n.
- Relatives: [A001787](../A001787/) n·2ⁿ⁻¹, [A001793](../A001793/)
  n(n + 3)·2ⁿ⁻³.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001792), CC BY-SA 4.0.
