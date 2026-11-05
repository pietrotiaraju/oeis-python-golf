# A000097

> Number of partitions of n if there are two kinds of 1's and two kinds of 2's.
> — [OEIS A000097](https://oeis.org/A000097)

Offset 0: 1, 2, 5, 9, 17, 28, 47, 73, 114, 170, 253, 365, 525, 738, 1033, …

### Python 3 — 87 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])<<(d>-3)for d in range(n,0))//n,
```

**How it works**

- The g.f. is Π 1/(1 − xᵏ) times 1/((1 − x)(1 − x²)): the Euler transform
  of b = [2, 2, 1, 1, 1, …]. Its log derivative gives
  **N·a(N) = Σ_d d·b(d)·Σ_j a(N − dj)** over d = 1…N and j ≥ 1 with
  dj ≤ N, the same recurrence as for the partition numbers with the
  divisors grouped by d, except that the d = 1 and d = 2 groups count
  twice.
- This is the [A000041](../A000041/) program with `<<(d>-3)` added. `n` is
  −N, `d` runs over −N…−1, and the slice `a[d::d]` is a(N − |d|),
  a(N − 2|d|), …. `*` binds tighter than `<<`, so the shift doubles the
  whole term `d*sum(…)` exactly when d is −1 or −2 (a left shift of a
  negative int is still multiplication by 2). `//n` divides −N·a(N) by −N,
  and the division is exact.
- The shift costs 8 bytes. Listing the extra steps instead,
  `for d in[*range(n,0),-1,-2]`, costs 9, and subtracting
  `sum(a)+2*sum(a[-2::-2])` after the sum costs more.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.1·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 1.5·10⁷, far beyond what the program gets to.
- Term N costs N Python steps plus about N·ln N additions inside the slice
  sums, as for A000041. The whole b-file (10 001 terms) prints in about
  34 s here and 5000 terms in about 7 s; the bar is 5000 terms in 60 s.
- Keeping the partition numbers in the list and adding the
  1/((1 − x)(1 − x²)) factor at print time, as [A000070](../A000070/) does
  with `sum(a)`, is longer: the double running sum needs extra state.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000097), CC BY-SA 4.0.
