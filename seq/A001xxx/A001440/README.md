# A001440

> Number of symmetric Costas arrays of order n that are inequivalent under dihedral group.
> — [OEIS A001440](https://oeis.org/A001440)

Offset 1: 1, 1, 1, 1, 2, 5, 10, 9, 10, 14, 18, 17, 25, 23, 31, 20, 19, 10, 6, 4, …

A Costas array of order n is an n × n permutation array (one dot per row
and column) whose dots have pairwise distinct displacement vectors. It is
symmetric when it is its own mirror image in a diagonal; the term counts
these up to the eight symmetries of the square (the classes of
[A001441](../A001441/) that contain a symmetric array).

### Python 3 — 200 bytes

```python
g=lambda P,i=-1,*U:i<0 or sum(g(Q,*[u for u in U if u-j])for j in(i,*U)for Q in[{*P,K*i+j,K*j+i}]if len({a-b for a in Q for b in Q})>len(Q)*~-len(Q))
n=1
while[K:=2*n,print(g((),*range(n))+1>>1)]:n+=1
```

**How it works**

- **Costas test.** The dot in column x and row y is the number K·x + y with
  K = 2n. Since |Δy| < n, the difference of two codes, K·Δx + Δy, determines
  the displacement (Δx, Δy), so a set of k dots has distinct displacements
  exactly when its codes have k(k − 1) + 1 distinct differences a − b
  (zero included): `len({a-b for a in Q for b in Q})>len(Q)*~-len(Q)`. A
  part of a Costas array passes too, so the test prunes as dots are added.
- **Symmetric arrays.** An array is symmetric about the main diagonal when
  its permutation is an involution. `g` gets the unassigned columns, the
  smallest one i first, and pairs i with itself or with a later unassigned
  j, adding the dots (i, j) and (j, i) (one dot when j = i); every
  involution is built exactly once, and S(n), the number of symmetric
  Costas arrays, is the count of completed ones (`i<0` once no column is
  left).
- **Classes.** For n ≥ 3 no Costas array is fixed by the half-turn: it
  would give the dot pairs in columns 0, 1 and in columns n − 2, n − 1 the
  same displacement. Hence none is fixed by a quarter-turn either, nor by
  both diagonal reflections (their product is the half-turn), and the
  reflections in the middle row or column fix no permutation array at all.
  So a symmetric array f has exactly the stabiliser {1, transpose}, its
  class has 4 arrays (f, its half-turn and their quarter-turns), and
  exactly two of them, f and its half-turn, are symmetric about the main
  diagonal; an array symmetric about the other diagonal turns into one
  that is by a quarter-turn. So a(n) = S(n)/2 for n ≥ 3, and
  `g(…)+1>>1` = ⌈S(n)/2⌉ also gives a(1) = a(2) = 1 (S = 1 and 2).

**Notes**

- Exact integers, no stored terms; the class count rests on the short
  argument above. It agrees with the table of Drakakis (Open problems in
  Costas arrays, 2011), which lists two symmetric arrays per class.
- Searching involutions only is far faster than searching all Costas
  arrays ([A001441](../A001441/)): a(16) = 20 after about 23 s here, each
  term taking about 2.7 times the one before. The bar is 16 terms in 60 s
  (the b-file has 32).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 200 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001440), CC BY-SA 4.0.
