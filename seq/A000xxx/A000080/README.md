# A000080

> Number of nonisomorphic minimal triangle graphs.
> — [OEIS A000080](https://oeis.org/A000080)

Offset 3: 1, 1, 2, 4, 9, 19, 48, 117, 307, 821, 2277, 6437, 18634, …

Take a set T of triples on n points and join two points when some triple
contains both. T is a minimal triangle system when that graph is connected
and dropping any one triple disconnects it. There is no formula: the known
terms (n ≤ 25) come from Martin Fuller's C program, which builds the
systems with nauty. A short program can only enumerate, so it gets a
handful of terms.

### Python 3 — 340 bytes

```python
from itertools import*
e=lambda T,s=1:2**n-1in[s:=s|t for t in T*n if s&t]
n=3;C=combinations
while 1:R=range(n);D={0};print(sum(e(T:=(7,)+U)>any(map(e,C(T,k)))==(T in D)!=D.update((*sorted(sum((t>>i&1)<<p[i]for i in R)for t in T),)for p in permutations(R))for k in R[:-2]for U in C([2*x for x in range(1<<n-1)if x.bit_count()==3],k)));n+=1
```

**How it works**

- **Masks.** Point i is bit i and a triple is a 3-bit mask. `e(T)` grows the
  set of points reachable from point 0, adding every triple that meets it,
  and says whether all n points (mask 2ⁿ − 1) are reached. n passes over T
  are enough: each pass adds at least one triple until nothing changes, and
  T has fewer than n triples.
- **A leaf can be put first.** Every minimal system has a point that lies in
  only one triple. Take a triple t and a piece C of T − t with as few
  triples as possible. If C held a triple t′, then T − t′ would have a piece
  that avoids t; it lies inside C and has fewer triples, which is impossible.
  So C is a single point, in t only. Relabelling that point 0 and its triple
  {0, 1, 2} (mask 7), the program takes T = (7,) + U with U made of triples
  that avoid point 0: even masks 2x, x a 3-bit number below 2ⁿ⁻¹.
- **At most n − 2 triples.** A triple whose points are not joined without it
  stays that way when other triples go, so minimality passes to pieces. If
  v is the leaf of t = {v, a, b} and a, b are still joined in T − t, then
  T − t is a minimal system on n − 1 points. Otherwise T − t splits into the
  piece of a and the piece of b, each a single point or a minimal system.
  Induction gives the bound in both cases, so `k` runs over `R[:-2]`,
  that is 0 … n − 3 triples in U. The bound is reached by n − 2 triples
  sharing one pair.
- **One chain of comparisons** does the rest, stopping at the first false
  link:
  - `e(T)>any(map(e,C(T,k)))`: T is connected and no T minus one
    triple is (T has k + 1 triples).
  - `==(T in D)`: `any(…)` is `False` here, so this holds when T is not in
    `D`, the set of every relabelling of the systems counted so far.
  - `!=D.update(…)` adds the n! relabellings of the new class. `update`
    returns `None`, so this link is always true, and `sum` counts 1.

  `combinations` keeps U in increasing order, so T is a sorted tuple, and
  the relabellings are stored as sorted tuples of masks too.
- **Triples or graphs.** The OEIS counts graphs and the program counts
  triple systems up to relabelling. They agree because the graph determines
  a minimal system. A point lies in only one triple exactly when it has
  degree 2, so two systems with the same graph share their leaf triples.
  Removing one of them (and merging a and b when they fall apart) leaves
  two smaller minimal systems that again have the same graph, and induction
  on n finishes the proof. The counts also match Fuller's graph counts for
  every n the program reaches.
- **Imports.** `combinations` is used twice, so `;C=combinations` (15
  bytes) pays for itself and saves 7. `permutations` is used once and keeps
  its name. Dropping the `*` costs more: `import itertools as I` gives 352
  bytes, `from itertools import combinations as C,permutations` gives 355,
  and plain `import itertools` gives 371.
- `2**n-1in` prints a `SyntaxWarning` (invalid decimal literal) on stderr.

**Limits**

- For n = 8 the program tries 384 168 sets U and prints a(3)…a(8) in about
  7 s. For n = 9 it needs 36 684 859 sets and prints the right a(9) = 48
  after about 7 minutes, so the bar is 6 terms in 60 s.
- `D` keeps every labelled copy of every class of the current n: about
  250 MB by the time the check stops the program during n = 9.
- Other shapes tried, measured before the `C=` alias: triples as tuples
  with set closures (382 bytes, n = 8
  in 25 s); `if 1==e(T)>any(…)` as a filter with `T not in D!=D.update(…)`
  as the term (353 bytes, a little faster); orbit removal from a set S of
  all valid T instead of `D` (361 bytes, little memory); triple masks from
  `map(sum,combinations(powers,3))` (1 byte shorter, but the masks come out
  of order, T is no longer sorted, and classes get counted twice).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 347 | first entry |
| 2026-11-05 | Python 3 | 340 | `C=combinations` alias (pietrotiaraju) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000080), CC BY-SA 4.0.
