# A000098

> Number of partitions of n if there are two kinds of 1, two kinds of 2 and two kinds of 3.
> — [OEIS A000098](https://oeis.org/A000098)

Offset 0: 1, 2, 5, 10, 19, 33, 57, 92, 147, 227, 345, 512, 752, 1083, 1545, …

### Python 3 — 87 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(sum(a[d::d])*d<<(d>-4)for d in range(n,0))//n,
```

**How it works**

- The g.f. is 1/((1 − x)(1 − x²)(1 − x³)·Π (1 − xᵏ)) = Π (1 − xᵏ)^(−b(k))
  with b = 2, 2, 2, 1, 1, 1, …: one factor per kind of part. Its log
  derivative gives **N·a(N) = Σ_d b(d)·d·Σ_j a(N − dj)** over d = 1…N and
  j ≥ 1 with dj ≤ N, the same recurrence as for the partition numbers with
  each part size weighted by its number of kinds.
- The loop is the one from [A000041](../A000041/): `a` is
  [a(0), …, a(N − 1)], `n` is −N, `d` runs over −N…−1, and the slice
  `a[d::d]` is a(N − |d|), a(N − 2|d|), …. The sum comes out as −N·a(N),
  and `//n` divides it exactly.
- The only change is the weight. `*` binds tighter than `<<`, so
  `sum(a[d::d])*d<<(d>-4)` is the term shifted left by one place, that is
  doubled, exactly when d is −1, −2 or −3. Shifting a negative int left is
  still multiplication by 2.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.11·√n digits (35 at n = 1000), so the 4300-digit int-to-str limit
  is reached only near n = 1.5·10⁷.
- The whole b-file (1001 terms) prints in under half a second here; the bar
  is all of it within 60 s.
- Doubling by list repetition, `d*sum(a[d::d]*-~(d>-4))`, is 88 bytes, and
  `~` on a bool is deprecated. Adding the three extra part sizes to the range
  instead, `for d in[*range(n,0),-1,-2,-3]`, is 90 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000098), CC BY-SA 4.0.
