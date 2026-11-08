# A000001

> Number of groups of order n.
> — [OEIS A000001](https://oeis.org/A000001)

Offset 0: 0, 1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, …

The program enumerates multiplication tables and counts their isomorphism
classes. It computes each term from the definition, without embedding a
table of known group counts.

### Python 3 — 221 bytes

```python
from itertools import*
print(0);n=k=1;Q=product
while P:=[*permutations(R:=range(n))]:print(sum(all(t[p[t[a][b]]][p[c]]==p[t[a][t[b][c]]]for a,b,c in Q(R,R,R))for t in Q([R],*batched(P[k:],k))for p in P[:k])//k);k*=n;n+=1
```

**How it works**

- A table on {0, …, n−1} is a tuple of rows, with row x the permutation
  y ↦ x·y. `P` lists all permutations in lexicographic order. The rows
  beginning with x form block x of length k = (n−1)!, so choosing row x
  from that block guarantees x·0 = x. Row 0 is fixed to `R`, giving
  0·x = x too. `Q([R],*batched(P[k:],k))` enumerates these tables;
  `batched` requires Python 3.12.
- A single equality checks both associativity and the automorphism p:

  ```text
  p(a·b) · p(c) = p(a·(b·c)).
  ```

  Setting b = 0 gives p(a)·p(c) = p(a·c), since 0 is a two-sided
  identity. Thus p preserves multiplication. Using that fact in the
  equality gives p((a·b)·c) = p(a·(b·c)); p is a permutation, so this is
  exactly associativity. Conversely, every associative table and its
  automorphisms satisfy the equality.
- `p` runs over `P[:k]`, the (n−1)! permutations with p(0) = 0. An
  automorphism always maps the identity to itself (p(0)·p(c) = p(c) for
  every c makes p(0) a left identity, so p(0) = p(0)·0 = 0), so the other
  permutations never pass, and skipping them changes no count.
- Each accepted table is a group: it is a finite monoid whose rows are
  permutations, so every element has a right inverse. If xy = 0 and
  yz = 0, then x = x(yz) = (xy)z = z, hence yx = yz = 0 too.
- Counting up to isomorphism uses the orbit-stabilizer theorem. A group G
  has (n−1)!/|Aut G| labelled tables with identity 0. Each contributes
  |Aut G| successful permutations p, so summing over pairs (table, p)
  and dividing by k counts each isomorphism class once.
- Initially k = 1 = 0!. Updating `k*=n` before incrementing n preserves
  k = (n−1)! at the start of each iteration. The list of permutations
  is never empty, so the `while` condition keeps going. a(0) = 0 is
  printed separately: there is no group of order zero.

**Limits**

- Fixing row 0 reduces the candidate tables from kⁿ to kⁿ⁻¹: 216 for
  n = 4 and 331 776 for n = 5. There are (n−1)! permutations p per table,
  hence 7 962 624 pairs at n = 5.
- The bar is six terms in 120 s, and it must come within half the
  timeout, in reference seconds. The 217-byte version, which tried all n!
  permutations, needed about 66 s on the GitHub runners; on the same local
  machine this one is 2.4 times faster, about 27 s.
- The search is still exhaustive: n = 6 already has 24 883 200 000
  candidate tables. Every term is computed by a finite search, but later
  terms quickly become impractical. Interpreter memory limits are not
  counted as correctness failures under the repository rules.
- 221 bytes is an upper bound on the shortest valid program, not a proof
  of minimality.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 260 | first entry |
| 2026-11-05 | Python 3 | 256 | `for a,b in Q(R,R)` (pietrotiaraju) |
| 2026-11-05 | Python 3 | 255 | value named in the while condition |
| 2026-11-06 | Python 3 | 217 | fix the identity row, fuse the two checks, update the factorial incrementally |
| 2026-11-08 | Python 3 | 221 | fix: only permutations fixing the identity, so the bar comes within half the timeout |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000001), CC BY-SA 4.0.
