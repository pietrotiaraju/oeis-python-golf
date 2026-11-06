# A000292

> Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2)/6.
> — [OEIS A000292](https://oeis.org/A000292)

Offset 0: 0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364, 455, …

### Python 3 — 34 bytes

```python
n=1
while[print((n**3-n)//6)]:n+=1
```

**How it works**

- With n + 1 in place of n the formula is (n − 1)·n·(n + 1)/6 = (n³ − n)/6,
  so starting the counter at 1 prints a(0) = 0 first. n³ − n is a product
  of three consecutive integers, so the division is exact.
- `while[print(…)]:` prints at the top of every pass; `[None]` is a
  non-empty list, so the loop never stops on its own.

**Notes**

- Same value, one byte longer: `n*~-n*-~n//6`. Running sums
  (`a=t=n=0` / `while[print(a)]:n+=1;t+=n;a+=t`) take 38 bytes, and
  `math.comb` costs more in the import than it saves.
- Exact integer arithmetic; the whole b-file (10 001 terms) prints in well
  under a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000292), CC BY-SA 4.0.
