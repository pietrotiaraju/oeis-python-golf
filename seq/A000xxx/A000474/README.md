# A000474

> Number of nonisomorphic 1-factorizations of complete graph K_{2n}.
> — [OEIS A000474](https://oeis.org/A000474)

Offset 1: 1, 1, 1, 6, 396, 526915620, 1132835421602062347

A 1-factorization of K_{2n} splits its edges into 2n − 1 perfect matchings;
two are isomorphic when a relabeling of the vertices carries the set of
matchings of one onto that of the other.

### Python 3 — 308 bytes

```python
from itertools import*
F=frozenset
n=2
while 1:
 P=[*permutations(range(n))];L={F(zip(p,p[::-1]))for p in P};H=lambda E,j=1:[E][:not E]+[t|{M}for M in L if(0,j)in M<=E for t in H(E-M,j+1)];S={*H(F().union(*L))};c=0
 while S:c+=1;x=S.pop();S-={F(F((p[a],p[b])for a,b in M)for M in x)for p in P}
 print(c);n+=2
```

**How it works**

- `n` is the number of vertices, 2, 4, 6, …, twice the OEIS index. A
  matching is a frozenset of ordered pairs, both (a,b) and (b,a), so that
  relabeling needs no sorting. For a permutation p, `zip(p,p[::-1])` pairs
  p[i] with p[n−1−i]: a perfect matching (n is even, so no vertex meets
  itself), and every perfect matching arises this way. The set
  comprehension `L` keeps each one once.
- `H(E,j)` lists the 1-factorizations of the remaining pair set E. Vertex 0
  lies in exactly one edge of each matching, so the j-th matching chosen is
  the one through (0, j); `(0,j)in M<=E` (a chained comparison) asks for
  that and for M to be still unused. Each factorization comes out exactly
  once, as a frozenset of matchings. `[E][:not E]` is `[E]` (the empty
  set, one way to finish) when nothing is left and `[]` otherwise, so dead
  ends add nothing.
- The start E is the union of all matchings, every ordered pair a ≠ b.
- Orbits: take any factorization left in S, count one class, and delete
  its images `F(F((p[a],p[b])for a,b in M)for M in x)` under all n!
  relabelings. Every class is counted once.

**Notes**

- The previous record, 512 bytes, encoded edges as triangular bit indices
  and generated matchings recursively.
- Exhaustive and exact, so the program is right for every n.
- K₈ has 6240 labeled 1-factorizations ([A000438](../A000438/)) in 6
  classes; a(1)–a(4) take about 13 s here, most of it building the
  6·8! images. a(5) would need the 1225566720
  labeled factorizations of K₁₀ and is out of reach. The b-file has 7
  terms (up to a(7)); the bar is 4 terms in 20 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 639 | first entry |
| 2026-11-06 | Python 3 | 631 | simplify equivalent expressions |
| 2026-11-06 | Python 3 | 621 | inline the least-edge test and shorten the matching base case |
| 2026-11-06 | Python 3 | 579 | use lazy lambdas for matchings and exact covers |
| 2026-11-06 | Python 3 | 550 | read each matching bit directly while relabeling |
| 2026-11-06 | Python 3 | 512 | share the edge encoder and generate relabeling indices directly |
| 2026-11-07 | Python 3 | 308 | matchings as pair sets from `zip(p,p[::-1])`, factor through (0,j) at step j, delete orbits |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000474), CC BY-SA 4.0.
