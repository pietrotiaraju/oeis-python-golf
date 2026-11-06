# A000511

> Number of n-step spiral self-avoiding walks on hexagonal lattice, where at each step one may continue in same direction or make turn of 2*Pi/3 counterclockwise.
> — [OEIS A000511](https://oeis.org/A000511)

Offset 0: 1, 1, 2, 3, 5, 8, 11, 17, 25, 33, …

### Python 3 — 249 bytes

```python
V=[(1,0),(-1,1),(0,-1)]
def f(x,y,d,n,S):
 if n==0:return 1
 t=0
 for j in(d,(d+1)%3):
  a=x+V[j][0];b=y+V[j][1]
  if(a,b)not in S:S.add((a,b));t+=f(a,b,j,n-1,S);S.remove((a,b))
 return t
n=0
while 1:print(f(1,0,0,n-1,{(0,0),(1,0)})if n else 1);n+=1
```

**How it works**

- Use axial coordinates on the triangular lattice. The three directions
  (1,0), (−1,1), (0,−1) differ by 120-degree counterclockwise turns.
- Fix the first step to (1,0), removing the arbitrary absolute direction.
  Every subsequent step either keeps its direction or advances to the
  next of these three directions, exactly as in the definition.
- `S` contains the visited vertices. A step is accepted only when its
  endpoint is new; backtracking removes it again after counting all
  continuations. Thus every allowed self-avoiding walk is counted once.
- The zero-step walk is counted separately. Positive lengths begin with
  the fixed first step and use the same search for their remaining steps.

**Notes**

- The search uses integer coordinates and constant work per search node.
  It stores one walk at a time, rather than a table of known counts.
- Running time grows with the number of walks. Python's recursion limit
  can eventually be reached, as allowed by the repository rules.
- The reference file contains 96 published OEIS terms; the verification
  bar is 20 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 249 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000511), CC BY-SA 4.0.
