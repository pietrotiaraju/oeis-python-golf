# A001419

> Number of n-celled polyominoes with holes.
> — [OEIS A001419](https://oeis.org/A001419)

Offset 1: 0, 0, 0, 0, 0, 0, 1, 6, 37, 195, 979, 4663, 21474, 96496, 425449, …

The polyominoes are free (counted up to rotations and reflections), as in
[A000105](../../A000xxx/A000105/), and a(n) = A000105(n) − A000104(n). A
hole is a bounded region of the complement, where two empty cells that
meet only at a corner are not joined: the one heptomino with a hole is the
3 × 3 square without its centre and one corner.

### Python 3 — 413 bytes

```python
def f(n,U,S,P):
 while U:c=U.pop();N={c+1,c-1,c+K,c-K};Q=P+[c];yield from n>1and f(n-1,U+[*N-S],S|N,Q)or[Q]
m=1
while[K:=3*m,print(sum(3*m-sum(c+d in Q for c in Q for d in(1,K))>=len({c+d for c in Q for d in(0,1,K,K+1)})and sorted(Q)==min(sorted(c-min(C)for c in C)for r in(0,1)for s in(K,-K)for t in(1,-1)for C in[[s*Y[r]+t*Y[r-1]for c in Q for Y in[divmod(c+m,K)]]])for Q in f(m,[0],{*range(-2*K,1)},[])))]:m+=1
```

**How it works**

- **Fixed polyominoes.** `f` is Redelmeier's algorithm, as in
  [A001168](../A001168/), turned into a generator: cell (x, y) is the
  integer x + K·y, every fixed polyomino with m cells comes out exactly
  once, as the list Q of its codes, translated so that its least cell
  (lowest row, then leftmost) is 0 and all others are positive. U holds the
  untried frontier, S every cell seen so far; `S` starts with all codes
  from −2K to 0, the cells before the start that the search can reach, so
  they are never offered (as in [A001207](../A001207/)). K = 3m keeps the
  codes of all cells it can reach distinct.
- **Holes by Euler's formula.** The union of the closed squares has V
  corners, E unit edges and m squares, and V − E + m = 1 − h, where h is
  the number of holes (bounded components of the complement; at a corner
  shared by two diagonal cells the union is pinched, so the empty cells on
  the other diagonal are not joined, as the definition wants). With A the
  number of pairs of side-adjacent cells, E = 4m − A, so the polyomino has
  a hole exactly when 3m − A ≥ V: `3*m-sum(c+d in Q for c in Q for d in(1,K))>=len({c+d for c in Q for d in(0,1,K,K+1)})`,
  the corners of cell c being c, c + 1, c + K and c + K + 1.
- **Free polyominoes.** A free polyomino is counted through one of its
  fixed versions only: Q counts when its sorted code list (least code 0)
  is the smallest of the eight lists of its rotations and reflections.
  `divmod(c+m,K)` gives (y, x + m), both from 0 to K − 1; the code
  s·first + t·second with s = ±K and t = ±1, or with the two swapped
  (`Y[r]`, `Y[r-1]`), is a symmetry of the square followed by a
  translation. A polyomino spans fewer than m columns, so these codes
  compare like (row, column) pairs and translating a list adds the same
  number to each code: after subtracting the least code, two lists are
  equal exactly when the shapes are translates. The identity gives the
  sorted list of Q itself, so `sorted(Q)==min(…)` holds for exactly one
  fixed version of each free polyomino (holes are kept by every symmetry).

**Notes**

- Exact integers, no stored terms; nothing beyond the definition,
  Redelmeier's algorithm and Euler's formula.
- The search visits every fixed polyomino (about four times more per
  term) and tests each for holes: a(13) = 21474 comes after about 62 s
  here. The bar is 13 terms in 120 s (the b-file has 40).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 413 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001419), CC BY-SA 4.0.
