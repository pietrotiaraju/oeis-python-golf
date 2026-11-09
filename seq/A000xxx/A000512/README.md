# A000512

> Number of equivalence classes of n X n matrices over {0,1} with rows and columns summing to 3, where equivalence is defined by row and column permutations.
> — [OEIS A000512](https://oeis.org/A000512)

Offset 1: 0, 0, 1, 1, 2, 7, 16, 51, 224, 1165, …

a(n) counts n×n 0-1 matrices with three ones in every row and every column,
two of them being the same when one becomes the other by permuting the rows
and permuting the columns (not by transposing). Equivalently: 3-regular
bipartite graphs on n + n vertices, up to isomorphisms that keep each side
in place.

### Python 3 — 436 bytes

```python
from math import*
from functools import*
P=lambda n,m=1:[((j,*p),-z*j*~p.count(j))for j in range(m,n+1)for p,z in P(n-j,j)]if n else[((),1)]
n=H=1
while[print(sum(H//r//s*(f:=cache(lambda R,C,h:R==()or C[-1]>(0,)and(sum(comb(g:=gcd(r:=R[0],s),t)*f(R,C[1:]+((C[0][0]-t*r//g,s),),h-t*s//g)for t in range(h+1))if(s:=C[0][1])else h==0and f(R[1:],(*sorted(C),),3))))(R,(*zip([3]*n,S),(9,0)),3)for R,r in P(n)for S,s in P(n))//H)]:n+=1;H*=n*n
```

**How it works**

- Burnside's lemma over the group S_n×S_n of row and column permutations:
  the number of classes is the average number of matrices fixed by a pair
  (ρ, σ). That number F(R, S) depends only on the cycle types R and S, and
  the cycle type with m_j cycles of length j has n!/z elements, where
  z = ∏ j^(m_j)·m_j!. With H = n!²,

  classes = (1/H)·Σ_{R,S} (H/z_R/z_S)·F(R, S),

  and each weight H/z_R/z_S is an integer (a product of class sizes).
  `n=H=1` and `H*=n*n` keep H = n!².
- `P(n)` lists the partitions of n, parts in increasing order, each with
  its z: a part j put in front of a partition whose parts are all ≥ j
  multiplies z by j times the new multiplicity of j, which is
  `-z*j*~p.count(j)`.
- A fixed matrix is constant on the orbits of ⟨(ρ, σ)⟩ on the cells. A row
  cycle of length r and a column cycle of length s hold r·s cells in
  g = gcd(r, s) orbits of length lcm(r, s); filling one orbit puts s/g
  ones in every row of the row cycle and r/g ones in every column of the
  column cycle, and t of the g orbits can be picked in C(g, t) ways. So
  F(R, S) is the sum, over the choices of t for every (row cycle, column
  cycle) pair that give every row and every column the right number of
  ones, of the products of the C(g, t).
- `f(R,C,h)` takes the row cycles one at a time (r = R[0]) and, for the
  current one, walks through the column slots in C. A slot is
  (deficit e, cycle length s), e being the ones still missing in each
  column of that cycle. The first slot is used: t orbits are chosen, h
  (the ones still missing in each row of the current cycle) drops by
  t·s/g, the slot's deficit by t·r/g, and the updated slot goes to the
  back. After the n column slots comes a sentinel (9, 0): its length 0 makes
  `if(s:=C[0][1])` false, so the row cycle ends there, which needs h = 0.
  The slots are then sorted, which brings the sentinel back to the end
  (every deficit is at most 3 < 9) and puts the state in a canonical
  form: the later rows treat the column slots alike, so only their
  multiset matters.
  The next row cycle starts again with h = 3.
- `C[-1]>(0,)` tests the deficit of the slot just updated: a pair (e, s)
  is above the one-tuple (0,) exactly when e ≥ 0. So an overfilled column
  is cut at once, and a negative h leaves `range(h+1)` empty. When R is
  empty every row has its ones, 3n in all; the column deficits
  started at 3n in total and none is negative, so all of them are 0
  and `R==()` returns True, a count of 1.
- Each (R, S) pair gets a fresh cache, made inside the sum with a walrus,
  `(f:=cache(lambda …))(…)`; the lambda looks f up when it runs, so it
  calls the current one. Peak memory stays near 100 MB.
- For n < 3 no row can hold three ones, so the sum is 0 without a
  special case.

**Notes**

- One shared cache, `f=cache(…)` on its own line (the key (R, C, h)
  already tells the pairs apart): 435 bytes, but it keeps every state of
  every pair, and an earlier form of it passed 1.2 GB within a minute on
  the degree-4 case here. H = n!² as `(H:=factorial(n)**2)` inside the
  sum: 446 bytes.
  The previous program (a `def a(n,k)` with a nested `@cache def
  f(i,j,h,D)` that indexed R and S and transposed sorted (length, deficit)
  pairs at every row end): 596 bytes.
- Exact integer arithmetic, so the program is right for every n. Only row
  and column permutations are used, as in the OEIS definition:
  no transposition and no complementation in the equivalence.
- 10 terms in 60 s here: a(9) after about 7.5 s, a(10) after about 25 s.
- a(28) has 24 digits, so the 4300-digit int-to-str limit is
  far out of reach.
- The b-file has 28 terms (up to a(28)); the bar is 8 terms in 60 s.

## First six terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(6) have to arrive in time.

### Python 3, 6 terms — 224 bytes

```python
from itertools import*
n=1
while R:=range(n):print(len({min(sum(4**sum(1<<q[j]for j in r)for r in M)for q in permutations(R))for M in combinations_with_replacement(combinations(R,3),n)if max(map(sum(M,()).count,R))<4}));n+=1
```

**How it works**

- A matrix is taken as its n rows, each the 3-subset of the columns that
  holds its ones. Permuting the rows only reorders them, so
  `combinations_with_replacement(combinations(R,3),n)` hands over every
  matrix with row sums 3 exactly once up to row order, as a sorted multiset
  of rows.
- `sum(M,())` lists the column of every one, and
  `max(map(sum(M,()).count,R))<4` keeps M when no column holds more than
  three ones. The 3n ones then fill the n columns with exactly three each, so
  this is the column condition.
- For a column permutation q, `sum(1<<q[j]for j in r)` is row r as a bitmask
  after the permutation, and `sum(4**…for r in M)` writes the multiset of
  these bitmasks as base-4 digits. A row occurs at most three times (its
  columns hold three ones each), so every digit is 0…3 and the number
  determines the multiset of rows.
- So the minimum over all n! column permutations is the same for two
  matrices exactly when one becomes the other by permuting columns and then
  rows: the set of minima has one element per equivalence class, and its
  size is a(n).
- For n < 3 there is no 3-subset, nothing is enumerated, and the count
  is 0, with no special case.

**Limits**

- a(6) takes C(25, 6) = 177 100 row multisets, and 720 column permutations
  for each one that passes. The six terms arrive in about 2.2 reference
  seconds (4.9 s on this PC).
- a(7) would take C(41, 7) ≈ 2.2·10⁷ multisets before any column
  permutation, minutes instead of seconds, which is why the main record
  counts with Burnside's lemma over cycle types instead of listing matrices.
- Everything is exact and exhaustive, so the program is right for every n;
  it is only slow.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-06 | 776 | first entry |
| 2026-11-06 | 607 | carry cycle-type denominators and merge the orbit recurrences |
| 2026-11-06 | 596 | transpose sorted residual pairs and short-circuit the zero-degree test |
| 2026-11-07 | 436 | slot list with a sentinel, one cache per cycle-type pair |

**Python 3, 6 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 224 | first entry: row multisets, minimum over column permutations |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000512), CC BY-SA 4.0.
