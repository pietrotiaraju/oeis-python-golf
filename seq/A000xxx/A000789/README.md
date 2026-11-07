# A000789

> Maximal order of a triangle-free cyclic graph with no independent set of size n.
> — [OEIS A000789](https://oeis.org/A000789)

Offset 2: 2, 5, 8, 13, 16, 21, 26, 35, 38, 45, 48, …

### Python 3 — 201 bytes

```python
h=lambda c,j:j<1or c>0<(h(c-(b:=c&-c),j)or h(c-b&~D*b,j-1))
n=2
while[print(max(m for m in range(n*-~n//2)for x in range(1<<m//2)if h(D:=x*2|int(f'{x:0{m}b}'[::-1],2),D.bit_count())>h(2**m-1,n)))]:n+=1
```

**What is searched**

A cyclic (circulant) graph on m vertices has vertex set Z_m, and v ~ w when
w − v (mod m) lies in a connection set D ⊆ {1, …, m−1} with D = −D. The
program tries every m and every D, keeps the graphs that are triangle-free
with independence number below n, and prints the largest m.

**How it works**

- **Every connection set once.** D is fixed by its part S = D ∩ [1, m/2].
  The bits of x stand for s = 1, 2, …, ⌊m/2⌋, so `x*2` has the bits of S, and
  reversing x as an m-digit binary string, `int(f'{x:0{m}b}'[::-1],2)`, sends
  bit s−1 to bit m−s, the mirror −S. Their OR is D as a bitmask; for even m
  the middle bit m/2 is its own mirror.
- **Independent sets.** `h(c,j)` asks whether the vertex set c (a bitmask)
  contains j pairwise non-adjacent vertices. It branches on the lowest vertex
  v of c, with b = 2^v: leave it out (`c-b`), or take it and drop its
  neighbours above it, which are v + d for d in D, the bits of `D*b`.
  `~D*b` is (~D)·b, which equals ~(D·b) above bit v, and that is all `c-b`
  can hold. Lower neighbours have already been decided, so no wrap-around is
  needed. `c>0<(…)` is `c>0 and (…)` in two bytes less.
- **Triangle-free.** A triangle through 0 is 0, a, b with a, b and b − a in
  D, i.e. an edge inside D; by symmetry every triangle can be moved to 0. So
  the graph is triangle-free exactly when D itself is independent,
  `h(D,D.bit_count())`.
- **No independent n-set.** `h(2**m-1,n)` must be False; the test reads
  True > False.
- **How far to look.** Such a graph has fewer than R(3,n) vertices, and
  R(3,n) ≤ C(n+1,2) (Erdős–Szekeres), so m runs below n(n+1)/2. No value of
  R(3,n) or of the sequence is assumed.

**Speed**

All 2^⌊m/2⌋ sets D are tried for every m below n(n+1)/2: the 6th term
(m < 28) arrives after about 30 s here; the 7th needs m < 36, about 16 times as
many sets. The bar is 6 terms within 120 s.

**Notes**

- Starting the independent-set search inside the non-neighbours of 0
  (`h(2**m-2&~D,n-1)`, using that the graph is vertex-transitive) is 5 bytes
  longer and does the 6 terms in about 6 s.
- With D as a Python set and a degree filter `len(D)<n` (a triangle-free
  graph has independent neighbourhoods, so every degree is below n), a
  251-byte version reaches the 7th term, 26, in about 33 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 201 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000789), CC BY-SA 4.0.
