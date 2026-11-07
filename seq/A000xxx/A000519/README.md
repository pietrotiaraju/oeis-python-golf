# A000519

> Number of equivalence classes of nonzero regular 0-1 matrices of order n.
> — [OEIS A000519](https://oeis.org/A000519)

Offset 1: 1, 2, 3, 5, 7, 18, 43, 313, 7525, 846992, …

a(n) counts n×n 0-1 matrices, other than the zero matrix, whose rows and
columns all have the same number k of ones (any k from 1 to n), two of them
being the same when one becomes the other by permuting the rows and
permuting the columns. It is the sum over k of the classes with k ones per
line: [A000512](../A000512/) is k = 3, [A000513](../A000513/) k = 4,
[A000516](../A000516/) k = 5, and the program is theirs with an outer sum.

### Python 3 — 457 bytes

```python
from math import*
from functools import*
P=lambda n,m=1:[((j,*p),-z*j*~p.count(j))for j in range(m,n+1)for p,z in P(n-j,j)]if n else[((),1)]
n=H=1
while[print(sum(H//r//s*(f:=cache(lambda R,C,h:R==()or C[-1]>(0,)and(sum(comb(g:=gcd(r:=R[0],s),t)*f(R,C[1:]+((C[0][0]-t*r//g,s),),h-t*s//g)for t in range(h+1))if(s:=C[0][1])else h==0and f(R[1:],(*sorted(C),),k))))(R,(*zip([k]*n,S),(n,0)),k)for k in range(n+1)for R,r in P(n)for S,s in P(n))//H-1)]:n+=1;H*=n*n
```

**How it works**

- Burnside's lemma over the group S_n×S_n of row and column permutations:
  the number of classes is the average number of matrices fixed by a pair
  (ρ, σ). That number F(R, S) depends only on the cycle types R and S, and
  the cycle type with m_j cycles of length j has n!/z elements, where
  z = ∏ j^(m_j)·m_j!. With H = n!²,

  classes = (1/H)·Σ_{R,S} (H/z_R/z_S)·F(R, S),

  and each weight H/z_R/z_S is an integer (a product of class sizes).
  `n=H=1` and `H*=n*n` keep H = n!².
- `P(n)` lists the partitions of n, parts in increasing order, each with
  its z: a part j put in front of a partition whose parts are all ≥ j
  multiplies z by j times the new multiplicity of j, which is
  `-z*j*~p.count(j)`.
- A fixed matrix is constant on the orbits of ⟨(ρ, σ)⟩ on the cells. A row
  cycle of length r and a column cycle of length s hold r·s cells in
  g = gcd(r, s) orbits of length lcm(r, s); filling one orbit puts s/g
  ones in every row of the row cycle and r/g ones in every column of the
  column cycle, and t of the g orbits can be picked in C(g, t) ways. So
  F(R, S) is the sum, over the choices of t for every (row cycle, column
  cycle) pair that give every row and every column the right number of
  ones, of the products of the C(g, t).
- `f(R,C,h)` takes the row cycles one at a time (r = R[0]) and, for the
  current one, walks through the column slots in C. A slot is
  (deficit e, cycle length s), e being the ones still missing in each
  column of that cycle. The first slot is used: t orbits are chosen, h
  (the ones still missing in each row of the current cycle) drops by
  t·s/g, the slot's deficit by t·r/g, and the updated slot goes to the
  back. After the n column slots comes a sentinel (n, 0): its length 0 makes
  `if(s:=C[0][1])` false, so the row cycle ends there, which needs h = 0.
  The slots are then sorted, which brings the sentinel back to the end
  and puts the state in a canonical form: the later rows treat the column
  slots alike, so only their multiset matters. Every deficit is at most
  k ≤ n, and it can be n only for k = n; then every row of the first row
  cycle needs all n columns, so when that cycle ends every deficit is
  below n and the sentinel sorts last.
  The next row cycle starts again with h = k.
- `C[-1]>(0,)` tests the deficit of the slot just updated: a pair (e, s)
  is above the one-tuple (0,) exactly when e ≥ 0. So an overfilled column
  is cut at once, and a negative h leaves `range(h+1)` empty. When R is
  empty every row has its ones, kn in all; the column deficits
  started at kn in total and none is negative, so all of them are 0
  and `R==()` returns True, a count of 1.
- Each (R, S) pair gets a fresh cache, made inside the sum with a walrus,
  `(f:=cache(lambda …))(…)`; the lambda looks f up when it runs, so it
  calls the current one. Peak memory stays near 100 MB.
- The outer sum runs over k = 0, …, n. Degree 0 and degree n give one class
  each (for k = 0 every t is 0), and the final −1 removes the zero matrix.

**Notes**

- Complementing every entry turns the k-regular matrices into the
  (n − k)-regular ones and commutes with the permutations, and the multiset
  {⌊k/2⌋ : 0 ≤ k ≤ n} equals {min(k, n − k) : 0 ≤ k ≤ n}. So degree k can be
  replaced by `(x:=k//2)` (and x in the two other places), which keeps the
  deficits small: 465 bytes and much faster (8 terms in 60 s, a(7) after
  1.5 s, a(8) after 12 s). With `(x:=min(k,n-k))`: 471 bytes.
  The previous program (a `def a(n,k)` with a nested `@cache def
  f(i,j,h,D)` that indexed R and S and transposed sorted (length, deficit)
  pairs at every row end): 618 bytes.
- Exact integer arithmetic, so the program is right for every n. Only row
  and column permutations are used, as in the OEIS definition:
  no transposition in the equivalence.
- 7 terms in 60 s here, a(7) after about 36 s (two runs).
- a(18) has 41 digits, so the 4300-digit int-to-str limit is
  far out of reach.
- The b-file has 18 terms (up to a(18)); the bar is 7 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 802 | first entry |
| 2026-11-06 | Python 3 | 633 | carry cycle-type denominators and merge the orbit recurrences |
| 2026-11-06 | Python 3 | 618 | transpose sorted residual pairs and short-circuit the zero-degree test |
| 2026-11-07 | Python 3 | 457 | slot list with a sentinel, one cache per cycle-type pair |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000519), CC BY-SA 4.0.
