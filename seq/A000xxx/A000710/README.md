# A000710

> Number of partitions of n, with two kinds of 1, 2, 3 and 4.
> — [OEIS A000710](https://oeis.org/A000710)

Offset 0: 1, 2, 5, 10, 20, 35, 62, 102, 167, 262, 407, 614, 919, 1345, 1952, 2788, …

### Python 3 — 87 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(sum(a[d::d])*d<<(d>-5)for d in range(n,0))//n,
```

**How it works**

- The g.f. is Π 1/(1 − xᵏ) times 1/((1 − x)(1 − x²)(1 − x³)(1 − x⁴)): the
  Euler transform of b = [2, 2, 2, 2, 1, 1, …]. Its log derivative gives
  **N·a(N) = Σ_d d·b(d)·Σ_j a(N − dj)** over d = 1…N and j ≥ 1 with
  dj ≤ N, the partition-number recurrence with the groups d = 1…4
  counted twice.
- This is the [A000098](../A000098/) program (two kinds of 1, 2, 3) with
  `-5` for `-4`. `n` is −N, `d` runs over −N…−1, and the slice `a[d::d]`
  is a(N − |d|), a(N − 2|d|), …. `*` binds tighter than `<<`, so
  `sum(…)*d<<(d>-5)` doubles the whole term exactly when d ≥ −4 (a left
  shift of a negative int is still multiplication by 2). `//n` divides
  −N·a(N) by −N, and the division is exact.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.11·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 1.5·10⁷.
- The whole b-file (1001 terms) prints in about a second; the bar is the
  whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000710), CC BY-SA 4.0.
