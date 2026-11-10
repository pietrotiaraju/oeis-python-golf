# A001423

> Number of semigroups of order n, considered to be equivalent when they are isomorphic or anti-isomorphic (by reversal of the operator).
> — [OEIS A001423](https://oeis.org/A001423)

Offset 0: 1, 1, 4, 18, 126, 1160, 15973, 836021, …

A semigroup is a set with an associative operation. a(n) counts the
operations on n points up to relabelling the points and up to reversing
the operation (x∘y ↦ y∘x); a(0) = 1 is the empty semigroup.

### Python 3 — 348 bytes

```python
from itertools import*
def g(T):
 N=n*n;U=T+[N]*-~N*n;R=range(n)
 return all(len({U[U[a*n+b]*n+c],U[a*n+U[b*n+c]],N})<3for a,b,c in product(R,R,R))and all(next((w>t for j,t in enumerate(T)if(w:=(*i,N).index(U[i[j//n]*s+i[j%n]*n//s]))-t),1)for i in permutations(R)for s in(1,n))and(len(T)==N or sum(g(T+[v])for v in R))
n=0
while[print(+g([]))]:n+=1
```

**How it works**

- A table is the list T of the n² products in row-major order, x·y at
  index x·n + y. The search fills it one cell at a time and keeps only
  tables that are smallest, read in that order, among all their images
  under the symmetries: exactly one table per class.
- Unknown cells hold the sentinel N = n², and `U` pads the partial table
  with n·(N + 1) more sentinels, so a product with an unknown factor or an
  unknown cell, such as U[N·n + c] or U[a·n + N], reads N too. Then
  associativity is `len({(ab)c, a(bc), N})<3`: the two sides agree or one
  of them is still unknown.
- The symmetries are the relabellings and, for anti-isomorphism, the
  relabellings followed by reversing the operation (x∘y ↦ y∘x, the
  transposed table). For each permutation i of the points and s ∈ {1, n},
  `U[i[j//n]*s+i[j%n]*n//s]` is the entry at (i(x), i(y)) for s = n and
  at (i(y), i(x)) for s = 1, where cell j = (x, y); so the image of T
  under the relabelling i⁻¹, reversed or not, has at cell j that entry
  mapped by i⁻¹.
  `(*i,N).index` applies the inverse of i to a value and sends N to n,
  larger than every symbol. The image is compared with T cell by cell
  and the generator stops at the first difference: if the image is
  smaller there, every completion of T has a smaller image and the
  branch is cut; on a full table this is the exact minimality test.
  Cutting only branches that hold no smallest table, the search counts
  each class once.

**Notes**

- Correct for every n: an exhaustive search with an exact minimality
  test, no theorem needed.
- The b-file is synthesized from the OEIS data (11 terms); the bar is
  6 terms (up to a(5)) in 60 s. a(5) comes after about 18 s here (about 9 reference seconds);
  a(6) would take hours.
- Evaluating the associativity test first and joining the tests with
  `and` (not `*`) halves the time; comparing whole image lists with `>=`
  instead of stopping at the first difference saves 23 bytes but is
  already 1.7 times slower at n = 4, and the gap grows with n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 348 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001423), CC BY-SA 4.0.
