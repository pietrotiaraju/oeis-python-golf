# A000843

> Number of quartic bicolored graphs on n unlabeled nodes admitting an automorphism exchanging the colors.
> — [OEIS A000843](https://oeis.org/A000843)

Offset 1: 0, 0, 0, 1, 1, 4, 12, 66, 433, 3442, 30404, 294951, 3093770, 34846185, 419020738, 5355289843, 72466668921, 1034818990771, 15548633703424, 245182764121059, …

### Python 3 — 388 bytes

```python
from math import*
from functools import*
f=cache(lambda n,R:sum(perm(n-1,p)*f(n+~p,(*sorted(R+((4,p+1),)),))for p in range(n))if n else R==()or g(R[1:],*R[0]))
def g(R,e,a,N=[]):
 if R:(s,b),*R=R;G=gcd(a,b);return sum(comb(G,m)*g(R,e-m*b//G,a,N+[(s-m*a//G,b)])for m in range(min(e*G//b,s*G//a)+1))
 return(a|~e)%2*comb(a//2,e//2)*f(0,(*sorted(N),))
n=1
while[print(f(n,())//perm(n))]:n+=1
```

**The count**

A quartic bicolored graph with n nodes of each colour is an n×n 0/1 matrix M
(rows = one colour, columns = the other) with every row and column sum 4,
taken up to independent row and column permutations, the group
H = S_n × S_n. It has an automorphism exchanging the colours exactly when
its H-orbit is fixed by transposition τ, and by Burnside's lemma for
H ∪ Hτ the number of H-orbits fixed by τ is the average number of fixed
matrices over the coset Hτ. Conjugating by H turns (α, β)τ into (αβ, 1)τ,
so

a(n) = (1/n!) · Σ_{γ ∈ S_n} #{M : M = (γ, 1)τ·M}.

The matrices fixed by (γ, 1)τ satisfy M(i, j) = M(j, ψ(i)) for a
permutation ψ with the cycle type of γ (so also M(ψi, ψj) = M(i, j), and
row i has the sum of column ψ(i)). The cells split into orbits:

- inside one cycle of length a, with ψ(i) = i + 1 (mod a), the cells
  (i, i + δ) for one δ form a class meeting every row once, and the
  relation pairs δ with 1 − δ: there are ⌊a/2⌋ orbits giving each row 2,
  and for odd a one more (2δ ≡ 1) giving each row 1;
- between cycles of lengths a and b there are g = gcd(a, b) orbits, each
  giving every row of the a-cycle b/g and every row of the b-cycle a/g.

So the term for γ depends only on its cycle type, and counts the sets of
orbits that give every cycle the row sum 4.

**How it works**

- `f(n,R)` with n > 0 is the sum over γ: the cycle through the smallest of
  the n remaining points has length p + 1, in perm(n−1, p) ways. `R` holds
  the cycles as pairs (row sum still needed, length), sorted so that every
  multiset is cached once; the main loop divides by n!.
- `f(0,R)` takes the first cycle (e, a) and `g` walks through the others.
  For a cycle (s, b) it chooses m of the G = gcd(a, b) orbits, in C(G, m)
  ways, taking m·b/G from e and m·a/G from s; the range bound stops either
  from going below 0. The visited cycles collect in `N`.
- When the walk is over, the orbits inside the current cycle must give the
  last e: C(⌊a/2⌋, ⌊e/2⌋) ways, and none when a is even and e odd, which is
  `(a|~e)%2`. The other cycles go back, sorted, to the cached `f`; those
  that already have their 4 simply pass through.
- Only `f` is cached: one cached function for every step of the walk is
  shorter, but it was slower and used ten times the memory.

**Notes**

- Exact integer arithmetic, correct for every n (Burnside's lemma and the
  orbit count above; the output matches every OEIS term it reaches).
- The b-file is the OEIS data, n = 1 to 25 (a(11) onwards from Andrew
  Howroyd's computation). On this PC the program prints 20 terms in 60 s,
  using about 105 MB; the bar is 16 terms in 60 s.
- The recursion is about n²/2 calls deep for the identity (n cycles of
  length 1), so Python's default limit of 1000 frames stops it near n = 32.
- [A000840](../A000840/) is the same program for the cubic case
  (`3` in place of `4`).

## First six terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(6) have to arrive in time.

### Python 3, 6 terms — 292 bytes

```python
from itertools import*
n=1
while R:=range(n):c=lambda M:min(sum(5**sum(r[j]<<q[j]for j in R)for r in M)for q in permutations(R));print(len({x for M in combinations_with_replacement([[j in t for j in R]for t in combinations(R,4)],n)if max(map(sum,zip(*M)))<5and(x:=c(M))==c([*zip(*M)])}));n+=1
```

**How it works**

- As in the main record, a quartic bicolored graph with n nodes of each
  colour is an n×n 0-1 matrix M with every row and column sum 4 (rows are
  one colour,
  columns the other), up to row and column permutations.
- Rows are 0-1 lists `[j in t for j in R]` of the 4-subsets t of the
  columns. Permuting rows only reorders them, so
  `combinations_with_replacement(…,n)` hands over every matrix with row sums
  4 exactly once up to row order. `zip(*M)` gives the columns, and
  `max(map(sum,zip(*M)))<5` keeps M when no column holds more than
  four ones, hence exactly four each (4n ones in n columns).
- `c(M)` is a canonical number for the class. For a column permutation q,
  `sum(r[j]<<q[j]for j in R)` is row r as a bitmask after the permutation,
  and `sum(5**…for r in M)` writes the multiset of these bitmasks as
  base-5 digits; a row occurs at most four times (its columns hold
  four ones each), so the number determines the multiset. The minimum over
  all n!
  column permutations is the same for two matrices exactly when one becomes
  the other by permuting rows and columns.
- An automorphism exchanging the colours sends row i to some column α(i) and
  column j to some row β(j), and keeps edges: M(i, j) = M(β(j), α(i)). That
  says the transpose, rows permuted by α and columns by β, is M. So the class
  has such an automorphism exactly when the transpose `[*zip(*M)]` (again a
  matrix with line sums 4) is in it, that is when `c(M)==c([*zip(*M)])`.
  The set collects c(M) for those M: one element per class with the
  property, and its size is a(n).
- For n < 4 there is no 4-subset, nothing is enumerated, and the count is
  0.

**Limits**

- a(6) takes C(20, 6) = 38 760 row multisets, and two canonical numbers
  (720 column permutations each) for each one that passes.
  The six terms arrive in about 1.6 reference seconds (3.1 s on this PC).
- a(7) would take C(41, 7) ≈ 2.2·10⁷ multisets before any canonical number,
  minutes instead of seconds; the main record, with Burnside's lemma over
  cycle types, reaches sixteen terms.
- Everything is exact and exhaustive, so the program is right for every n;
  it is only slow.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 388 | first entry |

**Python 3, 6 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 292 | first entry: row multisets, canonical number of the matrix and of its transpose |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000843), CC BY-SA 4.0.
