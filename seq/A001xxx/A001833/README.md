# A001833

> Number of labeled graded partially ordered sets with n elements.
> — [OEIS A001833](https://oeis.org/A001833)

Offset 0: 1, 1, 3, 19, 219, 3991, 106623, 3964339, 199515459, 13399883551, …

### Python 3 — 216 bytes

```python
import math,functools as F
g=F.cache(lambda m,j,p=0:sum(math.comb(m,q)*g(m-q,j-1,q)<<p*q for q in range(m+1)if j)or m<1)
a=[]
while[print(x:=g(n:=len(a),n)-sum(math.comb(n,j)*a[j]*g(n-j,n-1)for j in range(n)))]:a+=x,
```

**How it works**

- **Graded.** As the OEIS comment says, a poset is graded here when it has
  a rank function rk with rk(v) = rk(w) + 1 whenever v covers w. On a
  connected poset such a function is fixed up to a shift, so each graded
  poset has exactly one rank function whose minimum on every connected
  component is 0.
- **Levelled structures.** Let c(K, n) count the ways to put n labeled
  points on levels 0, …, K − 1 and join points of neighbouring levels by any
  set of edges (Klarner's c(K, n); [A001827](../A001827/) to
  [A001830](../A001830/) are K = 4 to 7). The edges are exactly the cover
  relations of a poset, and the levels a rank function. So a graded poset
  on n points is the same as a levelled structure in which every
  component meets level 0.
- **Dividing.** A levelled structure on K levels splits uniquely into the
  components that meet level 0 and the rest, a levelled structure on levels
  1, …, K − 1. Writing P_K(j) for the structures on j points whose
  components all meet level 0, c(K, n) = Σⱼ C(n, j)·P_K(j)·c(K − 1, n − j).
  A component on j points spans at most j levels, so P_K(j) = a(j) when
  K ≥ j. With K = n:
  a(n) = c(n, n) − Σⱼ₌₀..ₙ₋₁ C(n, j)·a(j)·c(n − 1, n − j).
- **The program.** `g(m,j,p)` counts the ways to spread m points over j more
  levels below a level of p points:
  g(m, j, p) = Σ_q C(m, q)·2^(pq)·g(m − q, j − 1, q), g(m, 0, p) = [m = 0],
  so c(K, m) = g(m, K), memoized with `F.cache` and shared by all n. In
  `sum(…if j)or m<1` the `if j` empties the sum on the last level, where
  `or m<1` gives True or False; above it the sum is at least 1. The list
  `a` holds the earlier terms, and `n:=len(a)` is the next index. For
  n = 0, `g(0,0)` is True, and True − 0 prints as 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The cache
  holds O(n³) values and the time grows like n⁴. The recursion is n levels
  deep, so it would stop with RecursionError near n = 490, long after the
  4300-digit int-to-str limit (near n = 236).
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s. All of it takes about 27 s on the PC it was written on.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 216 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001833), CC BY-SA 4.0.
