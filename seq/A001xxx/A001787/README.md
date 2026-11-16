# A001787

> a(n) = n*2^(n-1).
> — [OEIS A001787](https://oeis.org/A001787)

Offset 0: 0, 1, 4, 12, 32, 80, 192, 448, 1024, 2304, 5120, 11264, 24576, 53248, …

### Python 3 — 30 bytes

```python
n=0
while[print(n<<n>>1)]:n+=1
```

**How it works**

- `n<<n` is n·2ⁿ and `>>1` halves it: n·2ⁿ⁻¹. The shifts are evaluated left
  to right, and the halving is exact because n·2ⁿ is even for n ≥ 1 and 0
  for n = 0.
- The list `[…]` around the print is non-empty, so the loop never ends.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Relatives: [A001788](../A001788/) n(n + 1)·2ⁿ⁻², [A001789](../A001789/)
  C(n, 3)·2ⁿ⁻³, [A001792](../A001792/) (n + 2)·2ⁿ⁻¹, [A001793](../A001793/)
  n(n + 3)·2ⁿ⁻³.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001787), CC BY-SA 4.0.
