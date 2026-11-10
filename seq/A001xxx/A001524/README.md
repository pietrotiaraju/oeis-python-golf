# A001524

> Number of stacks, or arrangements of n pennies in contiguous rows, each touching 2 in row below.
> — [OEIS A001524](https://oeis.org/A001524)

Offset 0: 1, 1, 1, 2, 3, 5, 8, 12, 18, 26, 38, 53, 75, 103, 142, 192, 260, …

### Python 3 — 122 bytes

```python
from functools import*
G=cache(lambda i,n:(n%i<1)+sum(d*G(i+1,n-i*d)for d in range(1,n//i)))
n=0
while[print(G(1,n))]:n+=1
```

**How it works**

- Rows of pennies, from the bottom up, have lengths r₁ > r₂ > … > r_m ≥ 1:
  a penny touching two pennies of the row below sits in one of the r − 1
  gaps of a row of r, and a contiguous row of s pennies on it covers s
  consecutive gaps, so s ≤ r − 1 and there are **r − s** places for it.
  (The empty stack gives a(0) = 1, as in the current data.)
- With d_i = r_i − r_{i+1} ≥ 1 (r_{m+1} = 0) the stack has Σ i·d_i pennies
  and r_i − r_{i+1} = d_i, so a(n) is the sum over m ≥ 0 and
  d_1, …, d_m ≥ 1 with Σ i·d_i = n of d_1·d_2·…·d_{m−1} (the top row has
  one place). This is the generating function
  1 + Σ_{m≥1} q^(m(m+1)/2) / ((q;q)_{m−1}²·(1 − q^m)) on the OEIS page,
  but the program counts directly.
- `G(i,n)` sums over d_i, d_{i+1}, … with Σ_{j≥i} j·d_j = n: row i is
  either the top (d_i = n/i, the `(n%i<1)` term) or it has weight d and
  the rows above it make up n − i·d: **G(i, n) = [i | n] + Σ_d d·G(i+1, n − i·d)**
  over 1 ≤ d < n/i. Then a(n) = G(1, n); for n = 0 the first term gives
  G(1, 0) = 1, which is a(0).
- `range(1,n//i)` stops before n − i·d drops to 0 (that case is the top
  term) or below i+1, where G(i+1, ·) would be 0 anyway, so every call has
  1 ≤ n and i ≤ √(2n). The terms are asked for in increasing n, so each new
  term only recurses along one fresh chain of about √(2n) levels; the
  rest comes from the cache.

**Notes**

- Unlike [A001522](../A001522/) (S/P) and [A001523](../A001523/) (S/P²),
  neither (a − 1)·P nor (a − 1)·P² is a sparse series (checked to
  n = 60), so there is no pentagonal shortcut.
- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.2·√n digits (log a(n) ~ 2π·√(n/5), Wright 1971), far from the
  4300-digit int-to-str limit.
- The cache holds about ⅔·n·√(2n) values (86 MB at 5000 terms). 3000
  terms take about 8 reference seconds, and in 60 s it gets to about 7000
  terms. The bar is 3500 terms in 60 s (about 13 reference seconds).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 122 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001524), CC BY-SA 4.0.
