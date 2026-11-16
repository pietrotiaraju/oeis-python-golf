# A001793

> a(n) = n*(n+3)*2^(n-3).
> — [OEIS A001793](https://oeis.org/A001793)

Offset 1: 1, 5, 18, 56, 160, 432, 1120, 2816, 6912, 16640, 39424, 92160, …

### Python 3 — 36 bytes

```python
n=1
while[print(n*n+3*n<<n>>3)]:n+=1
```

**How it works**

- `n*n+3*n` is n(n + 3) (arithmetic binds tighter than the shifts);
  `<<n>>3` multiplies by 2ⁿ and divides by 8.
- The division is exact: n(n + 3) is always even, so n(n + 3)·2ⁿ is a
  multiple of 8 for n ≥ 2, and for n = 1 (the offset) it is 4·2 = 8.

**Notes**

- `n*(n+3)` has the same length as `n*n+3*n`.
- Exact integer arithmetic, so the program is right for every n.
- Relatives: [A001787](../A001787/) n·2ⁿ⁻¹, [A001788](../A001788/)
  n(n + 1)·2ⁿ⁻², [A001792](../A001792/) (n + 2)·2ⁿ⁻¹.
- The b-file has 500 terms (n = 1 to 500); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001793), CC BY-SA 4.0.
