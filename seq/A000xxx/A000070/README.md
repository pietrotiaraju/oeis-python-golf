# A000070

> a(n) = Sum_{k=0..n} p(k) where p(k) = number of partitions of k (A000041).
> — [OEIS A000070](https://oeis.org/A000070)

Offset 0: 1, 2, 4, 7, 12, 19, 30, 45, 67, 97, 139, 195, 272, 373, 508, 684, …

### Python 3 — 80 bytes

```python
*a,n=1,0
while[print(sum(a))]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- This is the [A000041](../A000041/) program with `a[-1]` changed to
  `sum(a)`. `a` holds p(0), …, p(N), the partition numbers, so its sum is
  a(N).
- Each p(N) comes from **N·p(N) = Σ_d d·Σ_j p(N − dj)** over d = 1…N and
  j ≥ 1 with dj ≤ N, the σ recurrence with the divisors grouped by d. `n`
  is −N and `d` runs over −N…−1, so the slice `a[d::d]` is exactly
  p(N − |d|), p(N − 2|d|), …, and `//n` divides the sum, −N·p(N), by −N
  exactly. The A000041 page explains each step.
- Printing comes first in the loop condition (`[None]` is true), so the
  first line is sum([1]) = a(0) = 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.1·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 1.5·10⁷, far beyond what the program gets to.
- `sum(a)` adds up the whole list for every term, but that costs far less
  than the recurrence. The whole b-file (1001 terms) prints in about 0.4 s
  and 10 001 terms in about 30 s.
- Keeping a(n) itself in the list is longer. The g.f. is
  1/(1 − x)·Π 1/(1 − xᵏ), the Euler transform of [2, 1, 1, …], which gives
  **N·a(N) = Σ (σ(k) + 1)·a(N − k)** on the OEIS page. The extra
  Σ a(N − k) is the d = 1 slice again, so the d = −1 term needs weight −2.
  Writing it as `(d<<(d>-2))` is 89 bytes, and subtracting `sum(a)` before
  the division is 88.

### Python 3 + sympy — 61 bytes

```python
from sympy import*
s=n=0
while[print(s:=s+partition(n))]:n+=1
```

- `partition(n)` is sympy's exact partition function, and `s` keeps the
  running sum. The walrus adds p(n) and prints the new total in one step.
- Asked for n in order, as here, `partition` extends a cached recurrence.
  The whole b-file prints in about 2 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 80 | first entry |
| 2026-11-05 | Python 3 + sympy | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000070), CC BY-SA 4.0.
