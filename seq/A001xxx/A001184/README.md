# A001184

> Number of simple Hamiltonian paths connecting opposite corners of a 2n+1 X 2n+1 grid.
> — [OEIS A001184](https://oeis.org/A001184)

Offset 0: 1, 2, 104, 111712, 2688307514, 1445778936756068, 17337631013706758184626, 4628650743368437273677525554148, 27478778338807945303765092195103685118924

### Python 3 — 245 bytes

```python
m=1
while 1:
 T={(1,*[0]*m):1}
 for k in[*[1]*~-m,0]*m:
  for(a,b,*r),v in(T,T:={})[0].items():
   for R in{0,k}&{z:=0**a+0**b|a&b,z-1}:D=z-R;M=(s:=a|b)//4*2|R|D<<m;T[u]=T.get(u:=(R*M,*[(x>>1,M)[x&s>0]for x in r],D*M),0)+v
 print(T[min(T)]);m+=2
```

**How it works**

- A frontier (transfer-matrix) count over the cells of the m × m grid,
  m = 2n+1, in reading order. Give the start corner (0,0) an extra edge
  coming in from the left, outside the grid, and the end corner
  (m−1,m−1) an extra edge leaving downwards. A Hamiltonian path between
  the two corners is then exactly a set of grid edges in which every cell
  has degree 2 and that has no cycle: the pieces are paths, and the only
  two path ends are the two outside edges, so there is one piece and it
  covers every cell. The program counts those edge sets, cell by cell.
- The state is the m+1 edge stubs ("plugs", 0 = absent) crossing the
  frontier, kept as a queue `(a, b, *r)`: `a` comes into the current cell
  from the left, `b` from above, then the up plugs of the rest of the row
  and the down plugs of the cells already done in it. Doing the cell pops
  `a` and `b` and pushes its right plug `R` in front (the next cell's left
  plug) and its down plug `D` at the back. The start state has only the
  outside plug of (0,0).
- Degree 2: with z of `a`, `b` absent, the cell sends out R + D = z
  plugs. `R` runs over `{0,k}&{z,z−1}` and `D=z-R`; the flag `k` is 0 in
  the last column, where nothing may leave to the right.
- A plug's value is the bit mask of the queue positions of all plugs on the
  same path piece (bit p for position p; the piece from the start corner
  has one plug, the others two). That is a canonical form by itself: no
  relabelling pass, and moving the queue one place is `x>>1` for every
  piece the cell does not touch. The pieces of `a` and `b` (the plugs with
  `x&s>0`, s = a|b, since different pieces have disjoint masks) become one
  piece with mask M = (s with bits 0, 1 dropped, shifted) | R | D·2ᵐ,
  `(s:=a|b)//4*2|R|D<<m`, covering the merge of two pieces, the
  continuation of one, and a new piece born in the cell.
- No cycles: `a` and `b` are the two ends of one piece exactly when
  a = b (= 3), so `a&b` is 3 there and 0 otherwise, and `z|a&b` = 3
  leaves `{3,2}&{0,k}` empty.
- After the last cell the queue is (R, d₀, …, d_{m−1}) with R = 0. The
  start piece always keeps exactly one plug on the frontier, so every final
  state has a plug; the wanted one has only d_{m−1} (the outside edge of the
  end corner) and is the smallest tuple, `min(T)`. Down plugs of other
  bottom cells make the other final states, which are dropped.
- Golf: the masks replace the usual labels plus a relabelling pass
  (about 40 bytes); `(T,T:={})[0].items()` walks the old layer while the
  name `T` already holds the new one; the flags list `[*[1]*~-m,0]*m`
  is one byte shorter than testing `k%m` on a `range(m*m)`.

**Notes**

- Exact integer counts, and the argument above holds for every n; no
  term is stored.
- The largest layer of states grows about 7 times per step of n (9296 at
  n = 5, 63774 at n = 6) and the time about 12 times per term: 6 terms in
  8 s, the 7th (63 MB) at about 92 s on the PC that set the bar. Past the
  bar, n = 7 needs several hundred MB and is still running when the
  timeout stops it.
- The b-file has the 9 known terms (n ≤ 8); the bar is 6 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 245 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001184), CC BY-SA 4.0.
