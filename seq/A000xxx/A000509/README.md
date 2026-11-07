# A000509

> Size of second largest n-arc in PG(2,q), where q runs through the primes and prime powers >= 7.
> — [OEIS A000509](https://oeis.org/A000509)

Offset 1: 6, 6, 8, 10, 12, 13, 14, 14, 17, 21, …

An arc in the projective plane PG(2,q) is a set of points with no three on
a line; it is complete if no point can be added. a(i) is the second largest
size of a complete arc in PG(2,q) for the i-th prime power q ≥ 7 (the
largest is q + 1 for odd q and q + 2 for even q).

### Python 3 — 447 bytes

```python
def f(S,C,V,k=0):
 if C+1>>N:B.add(k)
 while V:b=V&-V;V-=b;f(S|b,T:=C|b|sum(l^b for l in L if l&b>0<l&S),V&~T,k+1);V*=k>3
q=6
while 1:
 q+=1;p=h=2
 while q%p:p+=1
 if p**q%q<1:
  Q=q**3;R=range(N:=q*q+q+1);A=lambda a,b,c=1:a+b and(a+c*b)%p+p*A(a//p,b//p,c)
  while len({*(G:=[t:=1]+[t:=A(t*p%Q,h,t*p//Q)for _ in[0]*Q*Q])})<Q-1:h+=1
  L=[sum(1<<(i+j)%N for i in R if A(A(G[i],G[i*q]),G[i*q*q])<1)for j in R];B={0};f(0,0,2**N-1);print(sorted(B)[-2])
```

**How it works**

- Prime powers: p is the smallest prime factor of q, and `p**q%q<1` holds
  exactly when q has no other prime factor (its exponent is below q).
- The field GF(q³) = GF(pᵐ), m = 3e for q = pᵉ, is built directly over
  GF(p). An element is an integer in [0, Q), Q = q³, read as its m base-p
  digits. `A(a,b,c)` adds c·b to a digit by digit mod p; the recursion
  stops when both arguments are 0.
- For h = 2, 3, … the program lists the powers of X modulo Xᵐ − h(X):
  `t*p%Q` shifts the digits up and the overflowing top digit c = `t*p//Q`
  comes back as c·h. It keeps the first h whose powers take Q − 1 distinct
  values. Then X^m − h is primitive: the step is a companion matrix T; if T
  were singular, with nilpotent part of dimension a ≥ 1, an orbit would have
  at most a + p^(m−a) ≤ 1 + p^(m−1) < Q − 1 values, so T is invertible and
  the orbit of 1 runs through every nonzero vector. A T-invariant subspace
  would then be everything, so the minimal polynomial is irreducible,
  GF(p)[X]/(Xᵐ − h) is the field and X =: γ has order Q − 1. h = 0 and 1
  never pass and primitive polynomials of degree m exist, so h stays
  below Q.
- `G[i]` is γ^i. The points of PG(2,q) are GF(q³)*/GF(q)*, and since
  GF(q)* = ⟨γ^N⟩ with N = q² + q + 1 they are γ^i for 0 ≤ i < N. The
  trace Tr(x) = x + x^q + x^(q²) is GF(q)-linear and onto GF(q), so
  D = {i : Tr(γ^i) = 0} is a line, and multiplying by γ^j moves it to the
  line D + j (mod N): Singer's cyclic model of PG(2,q). x^q for x = γ^i is
  `G[i*q]`, and `G` has Q² + 1 entries, more than the largest index
  (N − 1)·q². `L` holds the N lines as bit masks.
- Every 4 points of an arc form a frame, and PGL(3,q) is transitive on
  ordered frames, so each complete arc with at least 4 points is the image
  of one through a fixed frame (and no complete arc is smaller: three
  points have secants through only 3q < N points).
- `f(S,C,V,k)` extends the arc S (k points, a bit mask). C holds the
  covered points, S and all its secants; V holds the free points above the
  last one added. The secants through a new point b are the lines through
  b that meet S (`l&b>0<l&S`); they share only b, so `sum(l^b …)` is their
  union without b, and `C|b|…` the new C. The arc is complete when C has all
  N bits, `C+1>>N`, and its size goes into the set B (the seed 0 is
  harmless).
- `V*=k>3` ends the loop after the first candidate on the first four
  levels, so the search starts from points 0, 1, the lowest point off
  their line and the lowest point off the three secants: a frame. Every
  point below a frame point is covered at that stage, so the other points
  of any arc through this frame are among the later candidates and the
  search meets every such arc. `sorted(B)[-2]` is the second largest
  complete size.

**Notes**

- The previous 867-byte version built GF(q) itself, used affine lines
  y = ax + b plus the line at infinity, fixed a frame at four corners and
  kept a secant table: it printed 5 terms in about 6 s here. Here most of
  the time goes into the Q² powers per tried h; `[0]*Q*q*q` (q⁵ powers,
  still enough) is 2 bytes longer and cuts the q = 8 field search from
  about 20 s to 3 s.
- Exhaustive and exact for every q: the program rests only on Singer's
  construction and the transitivity of PGL(3,q) on frames, and stores no
  arc sizes.
- 3 terms in 60 s here (q = 7 after 3 s, q = 8 after 23 s, q = 9 after
  28 s); q = 11 takes about 80 s. The list `G` has Q² + 1 entries, so
  memory becomes the limit near q = 16 (17 million entries).
- The b-file has 12 terms (up to a(12), q = 29); the bar is 2 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 1387 | first entry |
| 2026-11-06 | Python 3 | 867 | primitive-polynomial field arithmetic and direct affine line masks |
| 2026-11-07 | Python 3 | 447 | Singer cyclic plane from GF(q³), greedy frame inside the search |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000509), CC BY-SA 4.0.
