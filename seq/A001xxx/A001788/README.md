# A001788

> a(n) = n*(n+1)*2^(n-2).
> — [OEIS A001788](https://oeis.org/A001788)

Offset 0: 0, 1, 6, 24, 80, 240, 672, 1792, 4608, 11520, 28160, 67584, 159744, …

### Python 3 — 34 bytes

```python
n=0
while[print(n*-~n<<n>>2)]:n+=1
```

**How it works**

- `-~n` is n + 1, so `n*-~n` is n(n + 1); `<<n>>2` multiplies by 2ⁿ and
  divides by 4 (arithmetic binds tighter than the shifts, which go left to
  right).
- The division is exact: n(n + 1) is even and 2ⁿ is even for n ≥ 1, so
  n(n + 1)·2ⁿ is a multiple of 4, and for n = 0 it is 0.

**Notes**

- `n*n+n` has the same length as `n*-~n`.
- Exact integer arithmetic, so the program is right for every n.
- Relatives: [A001787](../A001787/) n·2ⁿ⁻¹, [A001789](../A001789/)
  C(n, 3)·2ⁿ⁻³, [A001793](../A001793/) n(n + 3)·2ⁿ⁻³.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001788), CC BY-SA 4.0.
