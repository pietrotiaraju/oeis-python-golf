# A000712

> a(n) = number of partitions of n into parts of 2 kinds.
> — [OEIS A000712](https://oeis.org/A000712)

Offset 0: 1, 2, 5, 10, 20, 36, 65, 110, 185, 300, 481, 752, 1165, 1770, 2665, 3956, …

### Python 3 — 81 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=2*sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- The g.f. is Π 1/(1 − xᵏ)², the Euler transform of b = [2, 2, 2, …]. Its
  log derivative gives **N·a(N) = 2·Σ_d d·Σ_j a(N − dj)** over d = 1…N
  and j ≥ 1 with dj ≤ N (the divisor sum σ(i) = Σ_{d|i} d grouped by d),
  the partition-number recurrence with every group counted twice.
- This is the [A000041](../A000041/) program with `2*` in front of the sum.
  `n` is −N, `d` runs over −N…−1, and the slice `a[d::d]` is a(N − |d|),
  a(N − 2|d|), …; `//n` divides −N·a(N) by −N, and the division is exact.
- Convolving the partition numbers with themselves at print time,
  `sum(map(int.__mul__,a,a[::-1]))`, costs far more than the 2 bytes.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.58·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 7·10⁶.
- Term N costs N Python steps plus about N·ln N additions inside the slice
  sums: 8700–9400 terms in 60 s here. The b-file has 10 001 terms; the bar is
  7000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000712), CC BY-SA 4.0.
