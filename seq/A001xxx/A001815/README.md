# A001815

> a(n) = binomial(n,2) * 2^(n-1).
> — [OEIS A001815](https://oeis.org/A001815)

Offset 0: 0, 0, 2, 12, 48, 160, 480, 1344, 3584, 9216, 23040, 56320, 135168, 319488, …

### Python 3 — 34 bytes

```python
n=0
while[print(n*~-n<<n>>2)]:n+=1
```

**How it works**

- C(n, 2)·2ⁿ⁻¹ = n(n − 1)·2ⁿ/4. `~-n` is n − 1, so `n*~-n` is
  n(n − 1); `<<n>>2` multiplies by 2ⁿ and divides by 4 (arithmetic binds
  tighter than the shifts, which go left to right).
- The division is exact: for n ≥ 2, 2ⁿ is a multiple of 4, and for
  n = 0, 1 the product is 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- `n*n-n` has the same length as `n*~-n`. Shifting a counter m = n − 2
  instead fails at n < 2 (a negative shift count is an error).
- Same template as [A001788](../A001788/) n(n + 1)·2ⁿ⁻², with `~-n` for
  `-~n`; relatives [A001787](../A001787/) n·2ⁿ⁻¹ and
  [A001789](../A001789/) C(n, 3)·2ⁿ⁻³.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001815), CC BY-SA 4.0.
