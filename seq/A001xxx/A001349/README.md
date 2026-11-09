# A001349

> Number of simple connected graphs on n unlabeled nodes.
> — [OEIS A001349](https://oeis.org/A001349)

Offset 0: 1, 1, 1, 2, 6, 21, 112, 853, 11117, 261080, 11716571, 1006700565, 164059830476, …

### Python 3 — 242 bytes

```python
import math,functools as F
f=F.cache(lambda r,*L:r<1or sum(f(r+k,*sorted(L+(k,)))<<-k//2+sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r)
R=C=1,;n=1
while[print(C[-1])]:R=f(n),*R;C+=R[0]-sum(d*C[d]*sum(R[d::d])for d in range(1,n))//n,;n+=1
```

**How it works**

- `f(n)` is g(n), the number of all simple graphs on n unlabeled nodes:
  the cached Burnside recursion of the [A000088](../../A000xxx/A000088/)
  record, unchanged (see that page for why it is exact). Its `[k]*n` uses
  the global n, which is never smaller than the argument of `f`.
- A graph is a multiset of connected graphs, so
  Σ g(n)·x^n = Π_{d≥1} (1 − x^d)^(−c(d)) (Euler transform), with c(n) =
  a(n). Comparing the coefficients of x·G′(x) = G(x)·Σ_d d·c(d)·x^d/(1 − x^d)
  gives n·g(n) = Σ_{d=1..n} d·c(d)·Σ_{j≥1} g(n − dj). The term d = n is
  n·c(n), so c(n) = g(n) − (Σ_{d<n} …)/n, with no Möbius function: the
  inverse Euler transform of the [A000719](../../A000xxx/A000719/) record,
  which prints g(n) − c(n).
- `R` is the tuple g(n), g(n−1), …, g(0) = 1, newest first, so
  Σ_j g(n − dj) is `sum(R[d::d])`. `C` holds c(0), c(1), …; the loop prints
  its last entry, then prepends g(n) to `R`, appends c(n) and moves on.
- The sum over d < n equals n·(g(n) − c(n)), so `//n` is exact. a(0) = 1
  is the entry's convention (the empty graph), the starting value of `C`;
  it is never used in the sums, which start at d = 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 76 terms (a(0) to a(75)). The bar is 40 terms in 60 s, as
  for A000088, whose recursion does all the work here: a(39) arrives after
  about 10 reference seconds, and 47 terms print before the timeout.
- Calling `f(n-m)` for every multiple m of d instead of keeping `R`
  (`for m in range(d,n+1,d)`) is 5 bytes longer. Storing d·c(d) as in
  [A000282](../../A000xxx/A000282/) needs a separate `print(1)` for a(0)
  and is longer too.
- a(n) ~ 2^C(n,2)/n!, so the 4300-digit int-to-str limit would only stop
  the program at a(176), far out of reach.

## First 23 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(22) have to arrive in time.

### Python 3, 23 terms — 207 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<-k//2+sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r
R=C=1,;n=1
while[print(C[-1])]:R=f(n),*R;C+=R[0]-sum(d*C[d]*sum(R[d::d])for d in range(1,n))//n,;n+=1
```

**How it works**

- The same inverse Euler transform, on the uncached graph recursion of the
  [A000719](../../A000xxx/A000719/) record: new cycles are appended as they
  come, `*L,k`, so each g(n) visits all 2^(n−1) compositions of n. The
  values are the same as with the cache, so it is right for every n.

**Limits**

- a(22) arrives after about 17 reference seconds, and each further term
  takes about twice as long, past the limit of 30 for a 24-term bar. Far
  short of the main bar of 40 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 242 | first entry |
| 2026-11-09 | Python 3, 23 terms | 207 | first entry: the graph recursion without the cache |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001349), CC BY-SA 4.0.
