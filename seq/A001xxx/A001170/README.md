# A001170

> Number of board-pair-pile polyominoes with n cells.
> — [OEIS A001170](https://oeis.org/A001170)

Offset 1: 1, 2, 6, 19, 63, 216, 760, 2723, 9880, 36168, 133237, 492993, …

### Python 3 — 229 bytes

```python
def f(n,U,S,P):
 t=0
 while U:c=U.pop();N={c+1,c-1,c+K,c-K};Q=P+[c];t+=f(n-1,U+[d for d in N-S if d>0],S|N,Q)if n>1else max(map((L:=[d%K for d in Q if d-K not in Q]).count,L))<3
 return t
K=3
while 1:print(f(K-2,[0],{0},[]));K+=1
```

**Which polyominoes**

- Fixed polyominoes whose every vertical cross-section has at most two
  "boards" (maximal runs of cells): the class A(2) of D. Zeilberger, *The
  umbral transfer-matrix method III: counting animals*, New York J. Math. 7
  (2001), who extended this entry to 54 terms that way. One board per column
  is the board-pile class, [A001169](../A001169/).
- The first difference from all fixed polyominoes ([A001168](../A001168/)) is
  at n = 8: 2725 − 2723 = 2, the "E" shape and its mirror image, with a column
  of three single cells.

**How it works**

- The search is Redelmeier's, as in [A001168](../A001168/): cells are
  x + K·y with K = n + 2, grown from the lowest-leftmost cell, each fixed
  polyomino once. P is the list of cells placed so far.
- On the last cell the finished polyomino Q is checked instead of counted. A
  board starts at each cell with no cell right below it (`d-K not in Q`), and
  `d%K` names the column (the x differ by less than K). L lists the columns of
  all board starts; the polyomino counts when no column appears 3 times.
- With `<2` in place of `<3` the program prints 1, 2, 6, 19, 61, 196, 629, …,
  which is A001169: a check that A(1) and A(2) are the right reading of
  "board-pile" and "board-pair-pile".

**Notes**

- Exponential, like A001168, and slower by the list and the check: 12 terms
  (to a(12) = 492993) in about 5 s here, 13 (to a(13) = 1829670) in about
  20 s. The bar is 13 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 229 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001170), CC BY-SA 4.0.
