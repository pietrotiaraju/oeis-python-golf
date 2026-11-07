# A000794

> Permanent of the Desarguesian projective plane PG(2,n), or 0 if such plane does not exist.
> — [OEIS A000794](https://oeis.org/A000794)

Offset 0: 1, 2, 24, 3852, 18534400, 4598378639550, 0, …

### Python 3 — 419 bytes

```python
import math
print('1\n2')
n=2
while 1:
 p=2;a=K=0;M=n**3;v=n*n+n+1
 while n%p:p+=1
 while p**K<M:K+=1
 for c in range(M*(p**K==M)):s=[1]*K;exec('s+=sum(c//p**i%p*s[i-K]for i in range(K))%p,;'*M);a=a or len({(*s[t:t+K],)for t in range(M)})>M-2!=(R:=[sum((any(s[d::v])<1)<<(i+d)%v for d in range(v))for i in range(v)])and sum((-1)**T.bit_count()*math.prod((~T&r).bit_count()for r in R)for T in range(2**v))
 print(a);n+=1
```

**What is computed**

PG(2,n) is built from the field GF(n), so it exists exactly when n is a prime
power. The program builds the plane from scratch for each such n (no tables)
and takes the permanent of its (n²+n+1)×(n²+n+1) incidence matrix; for other
n it prints 0. The first two terms are the OEIS conventions for the
degenerate "planes" of order 0 (one point on one line, permanent 1) and
order 1 (a triangle, permanent 2); no field gives them, so they are printed
as they are.

**How it works**

- **Prime powers.** p is the least prime factor of n and K the least
  exponent with p^K ≥ n³; n is a power of p exactly when p^K = n³, and then
  K = 3k for n = p^k. Otherwise the loop over c is empty and a stays 0.
- **The field GF(n³) without arithmetic.** For every coefficient vector c
  (the base-p digits of c) the `exec` string runs the linear recurrence
  s(t+K) = Σ cᵢ·s(t+i) mod p from the window 1, …, 1. If its first n³
  windows of length K take at least n³−1 values, the recurrence map cycles
  through all n³−1 nonzero states (a singular map has too small an image),
  so its polynomial is primitive. Then s(t) = L(αᵗ) for a primitive element
  α of GF(p^K) = GF(n³) and a nonzero GF(p)-linear form L.
- **Singer's plane.** The points of PG(2,n) are the cosets αᵈ·GF(n)*, with
  d taken mod v = n²+n+1, because GF(n)* = {α^(jv)}. The set
  H = {x : L(λx) = 0 for all λ in GF(n)} is a 2-dimensional GF(n)-subspace
  (the kernel of a nonzero GF(n)-linear map to a 1-dimensional space), i.e.
  a line, and its points are D = {d : s(d+jv) = 0 for all j}, which is
  `any(s[d::v])<1` (the slice also meets s(d+N) = s(d) for small d, a
  harmless repeat). Multiplying by α shifts D, and the shifts D+i are all
  v lines. `R` holds them as bitmasks of points.
- **Permanent.** Ryser's formula in the form
  perm = Σ_T (−1)^|T| Π_lines |line ∖ T| over all sets T of points.
- **Stopping after the first plane.** `a=a or …` skips the rest once a is
  set (a permanent of a plane is never 0: its incidence matrix has a
  perfect matching), and the chain `…>M-2!=(R:=…)` builds R only when the
  test passes, since M−2 is never equal to a list.

**Speed**

Ryser's sum has 2^v terms: 2²¹ for n = 4, which arrives after about 10 s
here, and 2³¹ for n = 5, many hours. The bar is the first 5 terms within
60 s.

**Notes**

- Every 0 the program prints is a theorem: the plane is Desarguesian, so
  the only question is whether GF(n) exists. A search for a cyclic
  difference set (any set of n+1 residues mod v with distinct differences)
  would be shorter, but it would rest on two open conjectures: that every
  cyclic plane is Desarguesian and that planar difference sets exist only
  for prime-power orders.
- A memoized permanent (cache over sets of used points) does n = 4 in 5 s
  but keeps about 1.4 million entries, and for n = 5 it would grow without
  bound before the timeout; Ryser's formula runs in constant memory.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 419 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000794), CC BY-SA 4.0.
