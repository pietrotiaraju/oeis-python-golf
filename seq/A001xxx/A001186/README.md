# A001186

> Number of cubic Hamiltonian graphs with 2n nodes.
> — [OEIS A001186](https://oeis.org/A001186)

Offset 2: 1, 2, 5, 17, 80, 474, 3841, 39635, 495991, 7170657, 116171803, 2070451150, 40130198979, 839266928707, 18826133329753, …

Graphs are simple, unlabeled and connected (a Hamiltonian graph always is),
and a graph with several Hamiltonian cycles counts once.

### Python 3 — 325 bytes

```python
M=lambda s:s and({a:b,b:a,**m}for b in s if 1<b-(a:=min(s))<N-1for m in M(s-{a,b}))or[{}]
H=lambda c,F:c[N-1:]and{(*(sum(map(c.index,{-~v%N,~-v%N,m[v]}))for v in c),)}or{x for v in F-{*c}for x in H(c+[v],{-~v%N,~-v%N,m[v]})}
N=4;s={0}
while R:={*range(N)}:
 t=0
 for m in M(R):
  if H([*R],0)-s:t+=1;s|=H([],R)
 print(t);N+=2
```

**How it works**

- **Every graph, labeled.** Number the vertices of a Hamiltonian cycle
  0, 1, …, N−1 (N = 2n): the other edges form a perfect matching of chords,
  none joining two neighbours on the cycle. `M` yields all these matchings
  as partner dicts: it pairs the smallest unmatched vertex `a` with every
  `b` with 1 < b−a < N−1 and recurses on the rest. Each unlabeled graph
  appears many times, once for every Hamiltonian cycle, starting vertex and
  direction, up to its automorphisms; the matchings number 1, 4, 31, 293,
  3326, 44189, … ([A003436](https://oeis.org/A003436)).
- **A complete key.** For a Hamiltonian path c of a graph (closed or not),
  relabel each vertex by its position on c and record, for every position k,
  the sum of its neighbours' positions. An inner position k has neighbours
  k−1, k+1 and one more, q, so the sum gives q. That fixes every edge except
  a possible edge between the two ends, and that one is decided by degrees:
  position 0 has exactly three neighbours. So two (graph, path) pairs have the
  same key exactly when relabeling along the paths gives the same graph. `H`
  is a depth-first search from every start (the top call gets `F` = all
  vertices) that returns the keys of all Hamiltonian paths.
- **Grouping.** The key of a matching's own cycle is `H([*R],0)`, the path
  0, 1, …, N−1 (a set of 0…N−1 built in order iterates in order in CPython).
  If it is not in `s`, the graph is new: `t` goes up and the keys of all its
  Hamiltonian paths go into `s`. A later matching gives an isomorphic graph
  exactly when its key is there, since the isomorphism carries its cycle onto
  a Hamiltonian path of the earlier graph with the same key. Keys of paths
  that do not close lack the edge 0–(N−1), so they never match a cycle's key
  and are harmless. So the search
  runs only once per class, not once per matching.
- **Golf.** `(a:=min(s))` sits in the first condition of the comprehension, so
  it binds before `{a:b,b:a,**m}` is built; `-~v%N` and `~-v%N` are v ± 1 mod N;
  a set of one tuple is truthy, so `c[N-1:]and{…}or{…}` picks the leaf; and
  `while R:={*range(N)}:` names the vertex set in the loop condition (it is
  never empty).

**Notes**

- Exact counting of isomorphism classes, nothing assumed beyond the two facts
  above; recursion depth is about N, far from the interpreter's limit.
- a(2)…a(7) arrive in about 25 s here (13 reference seconds), using about
  50 MB; the bar is 6 terms in 60 s. a(8) would mean 673471 matchings and
  3841 searches, out of reach in that time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 325 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001186), CC BY-SA 4.0.
