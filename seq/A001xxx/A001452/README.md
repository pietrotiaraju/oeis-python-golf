# A001452

> Number of 5-line partitions of n.
> — [OEIS A001452](https://oeis.org/A001452)

Offset 0: 1, 1, 3, 6, 13, 24, 47, 83, 152, 263, 457, 768, 1292, 2118, 3462, 5564, …

### Python 3 — 89 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])*min(5,-d)for d in range(n,0))//n,
```

**How it works**

- **MacMahon's generating function.** Plane partitions with at most five
  rows (5-line partitions) have the g.f. 1/Π_{k≥1} (1 − x^k)^min(k,5),
  as in the entry: the Euler transform of b(k) = min(k, 5) (k kinds of
  parts k for k ≤ 4, five kinds of every larger part).
- The Euler transform s of b satisfies the log-derivative recurrence
  **m·s(m) = Σₖ k·b(k)·Σⱼ s(m − jk)**, the template of
  [A000041](../A000041/) and the 3-line case [A000991](../A000991/): `a`
  holds s(0), …, s(m−1), `n` = −m, and with d = −k the slice `a[d::d]` is
  s(m − k), s(m − 2k), … The signs of d and n cancel in the division, and
  the weight is `min(5,-d)`.

**Notes**

- Exact integer arithmetic, and the divisions by m are exact, so the
  program is right for every n.
- `max(5*d,-d*d)` for d·min(5, −d), or counting n up with `range(-n,0)`,
  are a byte longer.
- The slices cost about m·ln m additions for s(m), so the run time is
  quadratic: about 8000 terms in 60 s here. The b-file has 10001 terms;
  the bar is 6000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001452), CC BY-SA 4.0.
