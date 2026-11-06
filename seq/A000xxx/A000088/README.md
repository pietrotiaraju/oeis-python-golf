# A000088

> Number of simple graphs on n unlabeled nodes.
> — [OEIS A000088](https://oeis.org/A000088)

Offset 0: 1, 1, 2, 4, 11, 34, 156, 1044, 12346, 274668, 12005168, 1018997864, 165091172592, 50502031367952, 29054155657235488, …

### Python 3 — 169 bytes

```python
import math,functools as F
f=F.cache(lambda r,*L:r<1or sum(f(r+k,*sorted(L+(k,)))<<-k//2+sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r)
n=0
while[print(+f(n))]:n+=1
```

**How it works**

- Burnside's lemma: a(n) = (1/n!)·Σ_π 2^e(π) over the permutations π of the
  n nodes, where e(π) is the number of orbits π has on the C(n, 2) possible
  edges. e depends only on the cycles of π: two cycles of lengths a and b
  move their a·b connecting edges in orbits of length lcm(a, b), so there are
  gcd(a, b) of them, and one a-cycle has ⌊a/2⌋ orbits on its own C(a, 2)
  edges.
- Instead of summing over partitions with the weights 1/z_λ, `f` builds π
  one cycle at a time: the cycle through a fixed point of the r points still
  free has length k with probability 1/r for each k = 1 … r. So
  f(r, L) = (1/r)·Σ_k 2^(⌊k/2⌋ + Σ_{j∈L} gcd(k, j))·f(r − k, L + k), where
  `L` holds the cycles already chosen and the shift is the number of edge
  orbits the new cycle adds (inside itself and towards each earlier cycle).
  f(0, L) = 1 and a(n) = f(n, ()). This is the recursion of the A000273
  (digraph) record with the graph exponent in place of the digraph one.
- `//r` at every level is exact: f(r, L) is (1/r!)·Σ_{σ∈S_r} of 2 to the
  number of orbits that σ×τ adds, with τ any permutation of cycle type L
  on the points already used. That average counts the S_r-orbits of sets of
  edges touching the r free points that τ maps to themselves, so it is an
  integer (de Bruijn's form of Burnside's lemma, as in A000171).
- Cycle lengths are stored negated, `for k in range(-r,0)`: `f(r+k,…)`,
  `-k//2` = ⌊|k|/2⌋, and gcd ignores the sign. `map(math.gcd,L,[k]*n)` uses
  the global n, which works because L never has more than n parts.
- The recursion on its own visits every composition of n, 2^(n−1) of them,
  and gets only 22 terms in 60 s. But f(r, L) depends only on the multiset
  L, so `functools.cache` with L kept sorted, `*sorted(L+(k,))`, cuts the
  states to the pairs (r, partition of a number ≤ n − r) and the cache is
  shared by all n. `import math,functools as F` and `F.cache` are 3 bytes
  under the separate imports.
- `r<1or` returns True for r = 0, and `print(+f(n))` turns it into 1 for
  a(0).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- a(0) … a(39) print in about 16 s and about 45 terms in 60 s, with about
  0.45 GB of cache at 44 terms. The bar is 40 terms in 60 s. The b-file goes
  to n = 87, out of reach of any partition sum in Python.
- The previous record (172 bytes) walked the partitions with weights
  2^e·n!/z_λ and was faster (about 58 terms in 60 s):
  `f=lambda n,k,L,w,d=1:n>=k and f(n,k+1,L,w)+f(n-k,k,L+[k],w//k//d<<sum(math.gcd(k,j)for j in L)+k//2,d+1)or 0**n*w`
  started at w = n! and divided by n! at the end.
- The recursion is about n calls deep, and a(n) ~ 2^C(n,2)/n! passes
  Python's 4300-digit int-to-str limit from n = 176; neither is reached in
  practice.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 172 | first entry |
| 2026-11-06 | Python 3 | 169 | A000273's divide-by-r cycle recursion, cached on the sorted cycle list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000088), CC BY-SA 4.0.
