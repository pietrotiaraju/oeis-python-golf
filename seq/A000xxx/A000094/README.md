# A000094

> Number of trees of diameter 4.
> — [OEIS A000094](https://oeis.org/A000094)

Offset 1: 0, 0, 0, 0, 1, 2, 5, 8, 14, 21, 32, 45, 65, 88, 121, 161, …

A tree of diameter 4 has a centre whose branches are leaves and stars, with
at least two stars. A star with k leaves uses k + 1 nodes, so the branches
form a partition of n − 1 with at least two parts of size 2 or more. That is
every partition except the hooks (k, 1, …, 1), of which there are n − 1 for
n ≥ 2 and one (the empty partition) for n = 1: **a(n) = p(n−1) − max(n−1, 1)**.

### Python 3 — 86 bytes

```python
*a,n=0,1,0
while[print(a[n>>-n]+n)]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- This is the [A000041](../A000041/) program, which keeps the partition
  numbers p(0), p(1), … in `a` with `n` = −m when p(m) is the last one, and
  prints p(m) + n = p(m) − m. That is a(m + 1) for every m ≥ 1, but at m = 0
  it gives 1 instead of 0.
- The fix is a 0 in front of the list: `*a,n=0,1,0` sets a = [0, 1] and
  n = 0. The recurrence never notices it, because the slices `a[d::d]` run
  from the end of the list towards the front and a 0 adds nothing to a sum.
- `a[n>>-n]` picks that 0 at m = 0 and the last term after that: 0 >> 0 is
  0, and for m ≥ 1, −m >> m is ⌊−m/2ᵐ⌋ = −1, since 0 < m/2ᵐ < 1. So the first
  line printed is 0 + 0, and every later one is p(m) − m.
- The recurrence is **N·p(N) = Σ_d d·Σ_j p(N − dj)** over d = 1…N and j ≥ 1,
  as on the A000041 page: after `n-=1`, `d` runs over −N…−1, the sum is
  −N·p(N) and `//n` divides it out exactly.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (500 terms) prints in well under a second, and about
  15 000 terms print in 60 s. The bar is the whole b-file in 60 s. p(m)
  passes Python's 4300-digit int-to-str limit only near m = 1.5·10⁷.
- `print(n and a[-1]+n)` and `print(a[-1]+n-0**-n)` fix the first term
  without the 0 in front, but both are 87 bytes. With the 0 in front,
  `a[~0**-n]` in place of `a[n>>-n]` is 87 bytes too, and `a[n and-1]` 88.

### Python 3 + sympy — 61 bytes

```python
from sympy import*
n=0
while[print(partition(n)-n-0**n)]:n+=1
```

- `partition(n)` is sympy's exact partition function. Here `n` counts up
  from 0, so `0**n` is 1 only at n = 0 and `-n-0**n` subtracts max(n, 1),
  two bytes shorter than `-max(n,1)`. The whole b-file prints in under a
  second, most of it the sympy import.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 86 | first entry |
| 2026-11-05 | Python 3 + sympy | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000094), CC BY-SA 4.0.
