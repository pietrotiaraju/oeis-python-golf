# A001116

> Maximal kissing number of an n-dimensional lattice.
> — [OEIS A001116](https://oeis.org/A001116)

Offset 0: 0, 2, 6, 12, 24, 40, 72, 126, 240, 272, …

### Python 3 — 1447 bytes

```python
from fractions import*
from math import*
O=sumprod
S=lambda Q:[[Q[0][0]*b-a*c for b,c in zip(r,Q[0][1:])]for a,*r in Q[1:]]
D=lambda Q:Q==[]or(d:=Q[0][0])>0and D(S(Q))*d//d**~-len(Q)
V=lambda Q,b:Q and[(((z-O(r,y))//d,*y),(z*z+v)//d)for d,*r in[Q[0]]for y,v in V(S(Q),d*b)for w in[isqrt(d*b-v)]for z in range((O(r,y)+w)%d-w,w+1,d)]or[((),0)]
n=0
while 1:
 w=range(n);K=[[[1+(i==j)for j in w]for i in w]][:n>1];b=n
 for P in K:
  L=V(P,P[0][0]);m=min(v for x,v in L if v);G=[*{tuple(a*c for a in x for c in x)for x,v in L if v==m}];b=max(b,len(G));e=range(n*n);L=[[i==j for i in e]for j in e];C=[]
  for g in G:
   for l in L:
    if s:=O(l,g):L,C=[[[(a*s-b*O(m,g))*s for a,b in zip(m,l)]for m in X]for X in(L,C)];C+=[a*s for a in l],;break
   else:W=[(f,O(f,g),{e for e in G[:G.index(g)]if O(f,e)==0})for f in C];C=[f for f,d,z in W if d>=0]+[[s*b-t*a for a,b in zip(p,m)]for p,s,y in W for m,t,z in W if s>0>t and sum(y&z<=x for f,d,x in W)<3]
  for f in C:
   M=R=[[f[i*n+j]+f[j*n+i]for j in w]for i in w];B=m
   while D(M)<1or any(0<v<q*m for x,v in V(M,q*m)):
    if c:=[(v-m,-k)for x,v in V(P,B)if(k:=O(x,map(O,R,[x]*n)))<0]:p,q=min(c,key=lambda t:Fraction(*t));M=[[q*a+p*b for a,b in zip(*z)]for z in zip(P,R)]
    B*=2
   Q=[[a//gcd(*sum(M,[]))for a in r]for r in M];K+=[Q]*all(D(A)-D(Q)or 1-(T:=lambda c=[],k=0:k==n or any(T(c+[x],k+1)for x,v in V(A,Q[k][k])if[O(x,map(O,A,[y]*n))for y in c+[x]]==Q[k][:k+1]))()for A in K)
 print(2*b);n+=1
```

**What is computed**

- A lattice is Zⁿ with a positive definite Gram matrix P; its kissing number
  is the number of minimal vectors, the x ≠ 0 with P[x] = min P. a(n) is the
  largest kissing number of an n-dimensional lattice.
- The maximum is reached at a **perfect form** (one that is determined by its
  minimum and its minimal vectors). Scale a lattice to minimum 1 and let S be
  its minimal vectors. The Ryshkov polyhedron
  R = {Q : Q[x] ≥ 1 for every integer x ≠ 0} is closed, convex and locally
  finite, and contains no line (Q + tD ∈ R for all t forces D[x] = 0 on Zⁿ,
  so D = 0). Its face {Q ∈ R : Q[x] = 1 for x ∈ S} is non-empty and contains
  no line either, so it has an extreme point, which is a vertex of R: a
  perfect form with minimum 1 whose minimal vectors contain S. So
  a(n) = max |Min P| over the perfect forms P.
- **Voronoi's algorithm** finds them all: up to GL_n(Z) and scaling there
  are finitely many perfect forms, and their neighbour graph (two forms are
  neighbours when their perfect cones, spanned by the rank-one forms xxᵀ of
  the minimal vectors, share a facet) is connected (Voronoi 1908; see
  A. Schürmann, *Computational geometry of positive definite quadratic
  forms*, AMS 2009, ch. 3). The program walks the graph from Aₙ.

**How it works**

- Forms are primitive integer Gram matrices. `S` is the scaled Schur
  complement d·Q′ − r rᵀ (d = Q₀₀, r the rest of row 0), always integral.
- `D(Q)` is the determinant, built from the Schur pivots with exact
  divisions, and it returns 0 as soon as a pivot is ≤ 0. By Sylvester's
  criterion it is positive exactly for positive definite Q, so the same
  function is the definiteness test and the determinant.
- `V(Q,b)` lists every x with Q[x] ≤ b together with Q[x] (Fincke–Pohst
  without square roots): d·Q[x] = (d·x₀ + r·y)² + S(Q)[y], so for each y with
  S(Q)[y] ≤ d·b the value z = d·x₀ + r·y runs over the integers ≡ r·y (mod d)
  with |z| ≤ isqrt(d·b − S(Q)[y]).
- For each perfect form P (starting with Aₙ: 2 on the diagonal, 1 elsewhere)
  the minimal vectors give the generators x⊗x; the set of tuples merges x
  and −x, so `len(G)` is half the kissing number.
- **Facets** of the cone spanned by G: double description in n² coordinates.
  `L` (first the identity) is a basis of the vectors orthogonal to every
  generator seen so far. A generator g with s = l·g ≠ 0 for some l in `L` is
  absorbed by elimination: everything is projected along l onto g⊥ (times s
  twice, to keep the rays' orientation) and s·l becomes a new ray. Otherwise
  it is an ordinary step: rays with f·g ≥ 0 stay, and each pair p, m with
  p·g > 0 > m·g gives (p·g)m − (m·g)p if p and m are adjacent. Adjacency is
  the combinatorial test: no third ray vanishes on all the processed
  generators that both vanish on (`sum(…)<3`, since p and m themselves
  always count). At the end `L` spans the antisymmetric matrices, and each
  ray f gives the facet normal R = F + Fᵀ.
- **Neighbour** across a facet R: P + tR keeps the facet's minimal vectors at
  m, and the neighbour is P + ρR with ρ = min (P[x] − m)/(−R[x]) over the x
  with R[x] < 0. The loop takes the best candidate among the x with
  P[x] ≤ B, B = m, 2m, 4m, …, and accepts it when M = qP + pR (ρ′ = p/q) is
  positive definite with no vector strictly between 0 and qm: if ρ′ > ρ, the
  vector that reaches ρ has M[x] < qm, or M is not definite. ρ is attained,
  so B eventually covers it. M starts as R, which is never positive definite
  (see below), just to enter the loop.
- **Isometry**: Q is new unless some A in `K` has the same determinant and
  vectors u₁, …, uₙ of A with uᵢᵀAuⱼ = Q_ij, found by backtracking over the
  vectors `V(A,Q[k][k])`. Equal determinants make the frame a basis
  (det(U)² = det Q / det A = 1). The determinant only splits classes, it
  never merges them.
- n = 0 and 1: `[:n>1]` leaves `K` empty and the program prints 2n, i.e. 0
  (no non-zero vectors) and 2 (the vectors ±1 of Z). The general loop would
  not end for n = 1: there the only facet normal is positive definite. For
  n ≥ 2 a facet normal R is never positive semidefinite, because R[x] = 0
  would put the facet's minimal vectors in a proper subspace W, whose
  rank-one forms span only dim W(dim W + 1)/2 ≤ n(n−1)/2 < n(n+1)/2 − 1
  dimensions; so every facet has a neighbour.

**Golf notes**

- `O=sumprod` (`math.sumprod`, Python 3.12) is an exact integer dot product.
- Working with x⊗x in n² coordinates avoids indexing a triangle: the extra
  antisymmetric directions just stay in `L`.
- The rays are not divided by their gcd: the numbers grow, the answers do
  not change.
- The isometry search is a lambda bound by `:=` inside the `all(…)` that
  scans `K`, so it closes over the current `A`.

**Notes**

- Checks: the program finds 1, 1, 2, 3 perfect forms for n = 2 to 5 (A₂;
  A₃; A₄, D₄; A₅, D₅ and A₅³, as classified by Korkine–Zolotarev and
  Voronoi); its facets of the cones of A₄, D₄, A₅, D₅ (10, 64, 15, 400) equal
  those of a brute-force search over all (N − 1)-subsets of generators;
  every one of the 513 neighbours it computes up to n = 5 is perfect and
  keeps the facet's minimal vectors; the isometry test recognises random
  GL_n(Z) images of each form.
- a(5) arrives after about 10 s here. n = 6 has seven perfect forms, but
  the cone of D₆ alone has 6336 facets: an instrumented run took 7 minutes
  for that cone and had found six of the seven classes (with E₆) when it was
  stopped. The bar is the 6 terms n = 0 to 5 in 120 s; the b-file is the 10
  known terms (a(9) = 272 is Watson's; a(10) is open).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 1447 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001116), CC BY-SA 4.0.
