# A001121

> Number of doubly-regular tournaments of order 4n-1.
> — [OEIS A001121](https://oeis.org/A001121)

Offset 2: 1, 1, 2, 2, 37, 722

### Python 3 — 788 bytes

```python
def T(r,j,Z,E):
 if~Z&K:0
 elif j<N:
  for v in(1,-1)[S[r][j-1]<0<(E[j-1]==E[j]):]:S[r][j]=v;S[j][r]=-v;T(r,j+1,Z-(E[j]<<N*(v<0)),E)
 else:
  R[r:]=[sum(2**j for j in W if S[r][j]<0)];I={};U=lambda i,B:all(I.setdefault(i,v:=[(x&X).bit_count()for X in B])<v or v==I[i]and U(i+1,[y for X in B for y in(X&~x-2**c,X&x)if y]+[0])for c,x in enumerate(R)if B[0]>>c&1)
  if U(0,[~-2**N]):T.n+=r>N-2;~r+N and T(q:=r+1,q+1,K+sum(c<<N*i for i,c in enumerate(c for m,b in[(N+~q,sum(S[q][1:q]))]for s in S[:q]for a,g in[(sum(map(int.__mul__,S[q],s[:q])),sum(s[q+1:]))]for c in(m+g-b-a,m+g+b+a,m-g-b+a,m-g+b-a))),[sum(4<<N*(4*k+1-s[j])for k,s in enumerate(S[:q]))for j in W])
N=8
while 1:W=range(N);S=[[(i<1)-(j<1)for j in W]for i in W];T.n=0;K=~-2**(4*N*N)//~-2**N<<N-1;R=[];T(0,N,K,0);print(T.n);N+=4
```

**What is counted**

- A tournament is *doubly regular* when every vertex has the same out-degree
  and every pair of vertices has the same number of common out-neighbours.
  On 4n−1 vertices these numbers are 2n−1 and n−1. Tournaments are counted
  up to isomorphism, that is, up to relabelling the vertices.
- Reid and Brown (1972): add a vertex ∞ that beats every other vertex, and
  let S be the ±1 matrix with S[i][j] = +1 when i beats j (zero diagonal,
  so S is skew-symmetric). Row ∞ is orthogonal to row i exactly when i is
  regular. Two vertices i and k agree on 2c of the other columns, where c is
  their number of common out-neighbours. So the tournament is doubly regular
  exactly when the rows of S are pairwise orthogonal, that is, when I + S is
  a skew Hadamard matrix of order 4n with its first row all +1. Here ∞ is
  row 0.
- This count is not [A001119](../A001119/). A001119 counts skew Hadamard
  matrices up to equivalence, and a single one gives a tournament for each
  row moved to the top (sign the columns so that row becomes all +1).
  Different rows can give non-isomorphic tournaments: the 37 tournaments on
  23 vertices come from 16 skew Hadamard classes.

**How it works**

Each tournament has one *smallest labelling*. To compare labellings, read the
upper triangle of S row by row, with +1 before −1 and ∞ fixed first. The
program builds only labellings that can still be the smallest of their
tournament, and counts those that are. `T` fills the cells in row order and
writes S[j][r] = −S[r][j] as it goes. Each cell has to pass three tests.

1. **Sorted columns.** Take two adjacent columns after r that are equal in
   rows 0..r−1. In the smallest labelling, a −1 in row r cannot come before
   a +1, because swapping the two vertices would give a smaller labelling.
   `E[j]` encodes column j over the finished rows, so `E[j-1]==E[j]` means
   "equal so far", and the loop then runs over `(1,-1)[True:]` = (−1,).
2. **Orthogonality counters.** For every finished row k and the new row q,
   look at the columns still to be filled. Each one pairs a sign of row k
   with a sign of row q, which gives four counts. They are fixed by the
   final dot products with row 0 and with row k. With m cells left,
   g = Σ of row k over those cells, b = the dot product with row 0 so far
   and a = the dot product with row k so far, four times the counts are
   m+g−b−a, m+g+b+a, m−g−b+a and m−g+b−a.
   - These numbers are packed into one integer `Z`, in fields of N bits.
     Each field starts at 2^(N−1) + the number, so its top bit is a guard.
   - A cell subtracts 4 from the field of every row k it uses (`E[j]`,
     shifted one field for −1). A field that drops below 0 clears its guard,
     and `~Z&K` catches that.
   - Per row k the four fields add up to 4m and lose 4 per cell. If none
     goes negative, they all end at 0. So the finished row is orthogonal to
     every earlier row, and the counts were integers.
   - A row with no cells left (the last one) is caught by the same guard
     test when it starts.
3. **Minimality test `U`, at the end of every row.** Rows 0..r are now known,
   so any choice of the first rows from vertices 0..r gives first rows that
   can be compared with ours. In each block of columns that are equal so
   far, put +1 before −1. A row is then fixed by its number of −1 in each
   block, as in A001119's canonical form.
   - `U` walks every such choice that ties with the current matrix, depth
     by depth. At each depth it takes a vertex from the first block, cuts
     every block into its +1 and −1 part, and fails as soon as some choice
     is smaller.
   - `I` holds our own counts. Our labelling is always the first path, so
     `setdefault` records them.
   - A smaller choice means no completion can be the smallest labelling, so
     the branch stops. A trailing 0 block keeps the list non-empty.

At the last row every vertex is known, so `U` is exact there: a matrix passes
exactly when it is the smallest labelling of its tournament. Every
tournament has exactly one smallest labelling, and that labelling passes all
the earlier tests. So a(n) is the number of matrices that reach the end,
`T.n`. Only exact integer and bit arithmetic is used.

**Notes**

- **Checks.**
  - On 7–19 vertices, a separate search gives the same classes. It is
    A001119's search plus a nauty-style canonical form for vertex
    relabelling, with independent pruning. Brute-force backtracking also
    shows that the representatives are pairwise non-isomorphic.
  - On 23 vertices, all 37 representatives are doubly regular, and each one
    equals the smallest labelling of its class as computed by that canonical
    form. The canonical forms are pairwise distinct and do not change under
    random relabellings.
  - Moving any row of the bordered matrix to the top (signing the columns
    so that it becomes all +1) always gives one of the 37. These moves link
    them into 16 groups, which is the number of skew Hadamard matrices of
    order 24 ([arXiv:2402.11074](https://arxiv.org/abs/2402.11074),
    Table 1).
  - Al-Azemi (2012) and Jørgensen
    ([arXiv:1410.8424](https://arxiv.org/abs/1410.8424)) give 37 and 722.
- **Speed.** 5 terms in about 25 s here, almost all of it on 23 vertices,
  with little memory. 27 vertices (722) is far out of reach. The bar is
  5 terms in 120 s. The OEIS has no real b-file; the one here is its file
  synthesized from the six data terms.
- **Recursion.** `T` recurses once per cell, about N²/2 levels. Python's
  default recursion limit would stop it at n = 12 (47 vertices), far beyond
  reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 788 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001121), CC BY-SA 4.0.
