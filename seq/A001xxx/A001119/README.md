# A001119

> Number of skew-symmetric Hadamard matrices of order 4n.
> — [OEIS A001119](https://oeis.org/A001119)

Offset 2: 1, 1, 2, 2, 16, 54

### Python 3 — 1063 bytes

```python
Y=int.bit_count
K=lambda v,r:[S[v][:r]]+sorted(s[:r]+[s[v]]for s in S[r:])
def D(P,B,Q):
 if(d:=len(P))==N:
  if Q<b[0]:b[:]=Q,P;return
  G.append({x^e:y^e for x,y in zip(b[1],P)for e in(0,1)});return 1
 L=[(R[u]^R[[*P,2*u][0]>>1]^F*e,2*u+e)for u in{*W}-{q>>1for q in P}for e in(0,1)]
 for X in B:z=min(Y(x&X)for x,p in L);Q+=z,;L=[c for c in L if Y(c[0]&X)==z]
 E={-1};n=len(G)
 if Q>b[0]:return
 for x,p in L:
  O={p}
  for _ in L:O|={g[o]for o in O for g in G[n:]}
  if not O&E and D(P+(p,),[y for X in B for y in(X&~x,X&x)if y],Q)and P!=b[1][:d]:return 1
  E|=O
def T(r,j,A):
 global R,G,b
 if j<N:
  for v in(1,-1)[S[r][j-1]<0<(S[j-1][:r]==S[j][:r]):]:S[r][j]=v;S[j][r]=-v;max(map(abs,B:=[a+v*s[j]for a,s in zip(A,S)]))<N-j and T(r,j+1,B)
 elif~r+N:T(q:=r+1,r+2,[sum(map(int.__mul__,S[q][:q],s))for s in S[:q]])
 elif all(K(j,r)>=K(r,r)for r in W for j in W[r:])>any(A):R=[sum(2**j for j in W if s[j]<0)for s in S];G=[];b=[(N,)]*2;D((),[F],());C[b[0]]=0
N=8
while 1:W=range(N);S=[[(i<1)-(j<1)for j in W]for i in W];C={};F=2**N-1;T(1,2,[0]);print(len(C));N+=4
```

**What is counted**

- A Hadamard matrix H of order N (entries ±1, HHᵀ = NI) is *skew* when
  H + Hᵀ = 2I, that is H = I + S with S skew-symmetric (zero diagonal, ±1
  off it). Then HHᵀ = I − S² = I + SSᵀ, so H is Hadamard exactly when the
  rows of S are pairwise orthogonal.
- Two equivalences are in use. *H-equivalence*: H′ = PHQ with P, Q signed
  permutation matrices (rows and columns permuted and negated
  independently). *SH-equivalence*: H′ = PᵀHP (one signed permutation on
  both sides, which keeps H skew). Table 1 of Araya, Harada, Kharaghani,
  Mohammadian and Tayfeh-Rezaie,
  [arXiv:2402.11074](https://arxiv.org/abs/2402.11074), counts both for
  orders 8–28: H-inequivalent skew Hadamard matrices 1, 1, 2, 2, 16, 54 and
  SH-inequivalent ones 1, 1, 2, 2, 16, 65. The OEIS data ends with 54, so
  a(n) is the **number of H-equivalence classes of Hadamard matrices of
  order 4n that contain a skew matrix**, and that is what the program
  counts. On orders 8–20 the two counts agree (an SH canonical form on the
  same search output also gives 1, 1, 2, 2), so the four terms of the bar
  cannot tell them apart; the program is still the H version, correct for
  every n.

**How it works**

- **Search (`T`).** One skew matrix per SH class is enough, since SH classes
  sit inside H classes. Take the SH class's lexicographic minimum: the upper
  triangle of DPSPᵀD read row by row, +1 before −1, minimised over signed
  permutations. That minimum has
  1. row 0 all +1 (the signs D can do this);
  2. sorted columns: for every r, the columns after r, read down rows 0..r,
     are in order, since swapping two that are not would make the matrix
     smaller at the first row where they differ;
  3. no better row r: moving a later j to position r and re-sorting the
     columns after it cannot give a smaller row r. Only a j whose column
     agrees with r's on rows 0..r−1 can keep rows 0..r−1 the same, and then
     row r becomes j's entries sorted within the blocks of equal columns.
     `K(v,r)` is that pattern followed by the sorted list of
     (row k on columns < r, S[k][v]) for k ≥ r (k = v adds the same entry,
     its pattern with a 0, to both lists, which does not change their
     order), and the test is `K(j,r)>=K(r,r)` for all j ≥ r; a j of a later
     block has a larger pattern, so it passes by itself.

  `T` fills the upper triangle cell by cell in row order, writing
  S[j][r] = −S[r][j] as it goes; `S` starts with row 0 = +1 and column 0 =
  −1. In a run of equal columns a +1 may not follow a −1: the loop runs over
  `(1,-1)[True:]` = (−1,) then. `A` holds the dot products of the current
  row with every earlier row over the columns filled so far, and a cell
  stays only if each of them is smaller in size than the number of cells
  left (`<N-j`), so a finished row is orthogonal to all earlier ones. At
  the last row, which has no free cell, `A` holds its full dot products, and
  `>any(A)` asks for zeros together with condition 3. At order 20 this
  leaves 119 matrices for the canonical form (424 without condition 3).
- **Canonical form (`D`).** The lexicographic minimum of PHQ, rows read in
  order, +1 before −1. Its first row is all +1, which fixes the column
  signs (each row u is a bit mask `R[u]` of its −1 entries, XOR-ed with the
  first row's). Once the rows are chosen the best column order is the
  sorted one, so a new row's string depends only on how many −1 it has in
  each block of columns still equal so far (the masks in `B`). `D` picks
  rows one at a time, any unused row with either sign (code 2u + e), keeps
  only those with the fewest −1 block by block (`Y=int.bit_count`), splits
  every block into its +1 and −1 part, and appends the counts to `Q`. A
  branch whose `Q` is already above the best leaf's stops. The counts fix
  the matrix, so the smallest `Q` over all leaves is a complete invariant:
  two matrices are H-equivalent exactly when their `Q` agree.
- **Automorphism pruning**, as in nauty. A leaf with the same `Q` as the
  best leaf `b` is the same matrix reached through other P, Q, so the map
  from the best path to this path (on signed rows, both signs: `x^e:y^e`)
  is an automorphism. It fixes the common prefix of the two paths and maps
  the earlier branch onto the current one, so the current branch adds
  nothing: `D` returns 1 until it reaches the common ancestor, the first
  node whose path is a prefix of the best one (`P!=b[1][:d]`). A node also
  skips a child whose orbit meets an explored child; the orbit is closed
  under the automorphisms found below that node (`G[n:]`), which all fix
  its path because the search did not return past it. Both cuts drop only
  branches that are images of explored ones, so the minimum is unchanged.
  Without them, order 12 (whose automorphism group has order 190080) took
  over 40 s by itself.
- a(n) is the number of distinct canonical forms, `len(C)`.

**Notes**

- Exact integer and bit arithmetic; the count needs no unproved claim. The
  bar terms were also checked by independent code: inside each class every
  matrix was mapped onto the first one by an explicit signed row and column
  permutation; the two classes of order 16 differ in an invariant (pairs of
  rows lying in 1 or 7 constant-product row quadruples versus 0 or 3; the
  two classes are transposes of each other); the two of order 20, which
  agree on the 4- and 6-row profiles and the p-ranks, have different plain
  lexicographic minima computed without any pruning; and the canonical form
  did not change under random signed row and column permutations.
- 4 terms in about 30 s here, almost all of it order 20; memory stays
  near 12 MB. Order 24 (16 classes) did not come out in 10 minutes. The
  bar is 4 terms in 120 s. The OEIS has no real b-file; the one here is
  its file synthesized from the six data terms.
- `T` recurses once per cell, about N²/2 levels, so Python's default
  recursion limit stops it at order 48, far beyond reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 1063 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001119), CC BY-SA 4.0.
