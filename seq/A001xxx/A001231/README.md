# A001231

> Number of nonisomorphic projective planes of order n.
> — [OEIS A001231](https://oeis.org/A001231)

Offset 2: 1, 1, 1, 1, 0, 1, 1, 4, 0

A projective plane of order n has v = n²+n+1 points and lines of n+1 points,
any two points lying on exactly one line (then any two lines also meet in
exactly one point). Two planes are isomorphic when a relabelling of the points
maps the lines of one onto the lines of the other. The known values come from
theory and big computer searches: PG(2,q) exists for every prime power q, the
Bruck–Ryser theorem rules out n = 6, uniqueness for n ≤ 8 and the four planes
of order 9 are computer results, and n = 10 is the Lam–Thiel–Swiercz search.
The program uses none of them: it enumerates and compares.

### Python 3 — 483 bytes

```python
def g(J,L,M,U,t):
 if M.bit_count()>n:
  J=[J[p]|M*(M>>p&1)for p in R];L+=M,;t=~-len(L)//n;M=1<<t;U=J[t]
  if t>n:x=[[max(l*(l>>a&l>>b&1)for l in L)for b in R]for a in R];I=lambda y,f=[],k=0:k==v or any(I(y,f+[c],k+1)for c in{*R}-{*f}if all(x[i-2][j-2]>>R[k-2]&1==y[f[i]][f[j]]>>c&1for j in R[:k]for i in R[:j]));X[:0]=[x][any(map(I,X)):]
 all(U>>c&1or g(J,L,M|1<<c,U|J[c],c)or len(L)//2>n<t for c in R[t+1:])
n=1
while 1:n+=1;R=range(v:=n*n+n+1);X=[];g([0]*v,(),1,0,0);print(len(X))
```

**How it works**

- Points are 0 … v−1, a line is a bitmask, `L` is the tuple of finished lines
  and `J[p]` the mask of points already on a common line with p. `g` builds
  the current line `M` point by point: `t` is its last point and `U` the union
  of the `J` of its points, so a candidate c > t may be added when `U` does
  not have bit c. A line with n+1 points is committed (`J` updated) and the
  next one is started.
- Lines are produced in the order of their two smallest points. In a plane
  whose first line is ℓ₀ = {0, …, n}, every line meets ℓ₀, so its smallest
  point is ≤ n: n+1 lines start at 0 and n at each a = 1 … n (the other lines
  through a meet ℓ₀ only in a). So after m ≥ 1 lines the next one starts at
  a = ⌊(m−1)/n⌋ (`t=~-len(L)//n`), and its second point must be the smallest
  partner of a not yet joined to a (a pair (p, a) with p < a is already
  covered). The other points are larger and are tried in every way, so each
  plane that contains the forced lines below is found exactly once, as its
  own sorted list of lines. Anything recorded is a plane: v lines of n+1
  points with no pair twice cover all C(v,2) pairs. m = v gives t = n+1, the
  only time `t>n` after a commit, and records it; the loop that follows finds
  no candidate since `J[n+1]` is full.
- Normalisation: for the first 2n+2 lines (`len(L)//2<=n`), and for the
  second point of every line (`t<=n`), only the first candidate is taken.
  That forces ℓ₀, the blocks {0, in+1, …, in+n}, the lines
  {1, n+1+j, 2n+1+j, …} through 1 and the line {2, n+1, 2(n+1), …, n(n+1)}
  through 2. Every plane has such a labelling: pick a point 0 and a line ℓ₀
  through it, number the rest of ℓ₀ 1 … n and the other lines through 0 as
  blocks 1 … n; the n lines through 1 other than ℓ₀ meet each block once, so
  numbering them j = 0 … n−1 gives the point of block i on line j the label
  in+1+j. The line through 2 and n+1 meets block i ≥ 2 on a line j = cᵢ ≠ 0,
  all different, and renumbering the lines j = 1 … n−1 makes cᵢ = i−1. So
  every isomorphism class is met. For n = 2 … 5 the search finds 1, 1, 2, 36
  normalised planes, exactly v(n+1)·n!·n!·n / |Aut PG(2,n)| (the labellings
  above, divided by the collineations, e.g. 13 392 000 / 372 000 = 36), as it
  must when PG(2,n) is the only plane.
- Isomorphism: `x[a][b]` is the line through a and b. Each new plane is
  compared with the kept ones by `I`, a backtracking search for a bijection:
  position k stands for point (k−2) mod v, its image c is any unused point
  such that for all earlier positions i < j, point k lies on line(i, j) in the
  new plane exactly when c lies on line(f[i], f[j]) in the other one. A
  bijection that keeps collinear triples (both ways) maps each line into, so
  onto, a line: it is an isomorphism, and every isomorphism passes. The plane
  is kept (`X[:0]=[x][any(map(I,X)):]`) only when no kept plane is isomorphic
  to it, so `len(X)` is a(n), for every n.
- Starting at point v−2 instead of 0 is only for speed: mapping the points of
  ℓ₀ first leaves wrong choices that are refuted much later (the 36 planes of
  order 5 take 54 s with the natural order, 0.3 s with this one).

**Golf notes**

- The candidate loop is `all(U>>c&1or g(…)or len(L)//2>n<t for c in …)`:
  `g` returns None, so an element is falsy, and `all` stops, right after the
  first usable candidate exactly when the line is a forced one.
- `I` is a lambda defined inside `g`, so it closes over the new table `x`, and
  `map(I,X)` hands it each kept plane as `y`.
- `R=range(v)` gives `R[k-2]` = (k−2) mod v, `R[:k]` and `R[t+1:]`; `L` is a
  tuple so `L+=M,` makes a new one.
- `J` starts at zeros: a point's own bit is never needed, since candidates
  are always beyond the line's last point.

**Notes**

- Exact bit arithmetic and exhaustive search; no theorem about planes is used
  and no term is stored. a(6) = 0 comes from the search running dry (this is
  Tarry's result: no two orthogonal Latin squares of order 6).
- n = 2 … 5 take under a second, n = 6 about 32 s here (about 15 reference
  seconds). n = 7 would mean about 14 400 normalised planes out of a far
  larger search tree.
- Each added point costs a `g` frame and a generator frame, so the depth is
  about 2nv: within Python's default recursion limit up to n = 7, beyond that
  an interpreter limit.
- The b-file has the 9 known terms (n = 2 … 10); the bar is 5 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 483 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001231), CC BY-SA 4.0.
