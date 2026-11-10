# A001426

> Number of commutative semigroups of order n.
> — [OEIS A001426](https://oeis.org/A001426)

Offset 0: 1, 1, 3, 12, 58, 325, 2143, 17291, …

A commutative semigroup is a set with an associative and commutative
operation; a(n) counts them on n points up to isomorphism (relabelling
the points). a(0) = 1 is the empty semigroup.

### Python 3 — 357 bytes

```python
from itertools import*
def g(T):
 N=n*n;U=T+[N]*-~N*n;R=range(n)
 return all(len({U[U[a*n+b]*n+c],U[a*n+U[b*n+c]],N})<3>len({U[a*n+b],U[b*n+a],N})for a,b,c in product(R,R,R))and all(next((w>t for j,t in enumerate(T)if(w:=(*i,N).index(U[i[j//n]*n+i[j%n]]))-t),1)for i in permutations(R))and(len(T)==N or sum(g(T+[v])for v in R))
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
- The symmetries are the relabellings (a commutative table is its own
  transpose, so isomorphism and anti-isomorphism agree). For each
  permutation i of the points, `U[i[j//n]*n+i[j%n]]` is the entry at
  (i(x), i(y)), where cell j = (x, y); the image of T under the
  relabelling i⁻¹ has at cell j that entry mapped by i⁻¹.
  `(*i,N).index` applies the inverse of i to a value and sends N to n,
  larger than every symbol. The image is compared with T cell by cell
  and the generator stops at the first difference: if the image is
  smaller there, every completion of T has a smaller image and the
  branch is cut; on a full table this is the exact minimality test.
  Cutting only branches that hold no smallest table, the search counts
  each class once.
- Commutativity is checked in the same pass, chained onto associativity:
  `…<3>len({U[a*n+b],U[b*n+a],N})` asks that x·y and y·x agree or one is
  unknown.

**Notes**

- Correct for every n: an exhaustive search with an exact minimality
  test, no theorem needed.
- The b-file is synthesized from the OEIS data (11 terms); the bar is
  6 terms (up to a(5)) in 60 s. a(5) comes after about 4 s here;
  a(6) is not done after 130 s.
- Evaluating the associativity test first and joining the tests with
  `and` (not `*`) halves the time; comparing whole image lists with `>=`
  instead of stopping at the first difference saves 23 bytes but is
  already 1.7 times slower at n = 4, and the gap grows with n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 357 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001426), CC BY-SA 4.0.
