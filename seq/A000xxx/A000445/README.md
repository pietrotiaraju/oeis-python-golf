# A000445

> Latest possible occurrence of the first consecutive pair of n-th power residues, modulo any prime.
> — [OEIS A000445](https://oeis.org/A000445)

Offset 2: 9, 77, 1224, 7888, 202124, 1649375, …

### Python 3 — 934 bytes

```python
from math import*
from functools import*
def J(a,n):
 t=1;a%=n
 while a:
  while a%2<1:a//=2;t*=1-2*(n%8 in(3,5))
  a,n=n,a;t*=1-2*(a%4==n%4==3);a%=n
 return t*(n==1)
P=cache(lambda n:next((p for p in range(2,isqrt(n)+1)if n%p<1),n))
def Q(n):
 for r in range(2,n+1):
  if n%(r<<2*(r%4!=1)):continue
  x=r;u=()
  while x>1:
   p=P(x);x//=p
   if x%p<1:break
   u+=p,
  else:yield r,u
def S(d,C):
 def f(F):
  x=len(F);p=P(x)
  return max([x-1 if c==F[-1]==0 else f(V)for c in(range(d)if p==x else[(F[p]+F[x//p])%d])if x!=2 or d%(c or d)<1 for V in[F+[c]]if all(max(u)!=x or sum(V[p]for p in u)%2==e for u,e in C)]+[0])
 return f([0,0])
def V(n):
 L=[*Q(n)]
 T={(d:=gcd(a-1,n),tuple((u,(1-J(r,a))//2)for r,u in L)if d%2<1 else())for a in range(1,n)if gcd(a,n)<2}
 return max([S(d,E)for d,E in T]+[min(R&{x-1for x in R}or{0})for p in range(2,n+1)if n%p<1 and P(p)==p for R in[{x**n%p for x in range(1,p)}]])
n=2
while 1:print(V(n));n+=1
```

**How it works**

- The output index n is the power-residue exponent. For a unit
  a modulo n, put d=gcd(a−1,n). Large primes in that residue
  class have their n-th-power residues described by the zero
  colors of a map f into ℤ/dℤ, with f(xy)=f(x)+f(y).
  Thus assigning the colors of primes determines those of all
  positive integers.
- `V(n)` enumerates these residue classes a. The pair
  `(d,E)` describes the effective color group and quadratic
  restrictions; a set comprehension searches each distinct pair once.
  Primes dividing n are checked directly at the end as ramified
  exceptions.
- `Q(n)` generates squarefree r whose positive
  fundamental discriminant divides n, together with their prime
  factors ps. Its output is materialized once as L so all unit
  classes can reuse it; `r<<2*(r%4!=1)` supplies the same
  fundamental discriminant by multiplying r by 1 or 4.
  A repeated factor rejects r. J computes the Jacobi
  symbol by removing powers of two and quadratic reciprocity;
  it supplies the required parity of the colors in ps.
- J updates its sign by multiplying by `1-2*condition`,
  which is −1 exactly when reciprocity or the power-of-two
  rule requires a sign change. Q stores factor tuples directly,
  keeping every Frobenius type hashable.
- Inside search, F[x] is the color assigned to x. Start with
  `[0,0]`, using position 0 as a placeholder and f(1)=0.
  At x=len(F), `P(x)` is the least prime factor: at a
  prime branch over all colors, while at a composite derive
  `(F[p]+F[x//p])%d` from smaller integers.
- At x=2, only zero and the proper divisors of d are needed.
  Multiplying every color by a unit modulo d preserves its zero
  set and parity conditions; these choices represent all possible
  greatest common divisors of the original color with d.
- After appending c, check each relation whose largest prime
  has just been assigned. All its referenced F entries then
  exist. Reject the branch if the sum of those colors has the
  wrong parity.
- `c==F[-1]==0` detects the first adjacent zero colors,
  at x−1 and x. Return x−1 immediately; otherwise recurse.
  The comprehension uses `d%(c or d)<1` for the initial
  zero-or-divisor condition and retains 0 when no branch is valid.
  Taking maxima over branches and then over types finds the
  latest first pair. The finiteness and realizability arguments
  below explain why this finite search answers a question over
  infinitely many primes.

- The final maximum combines the color-search results and the
  ramified-prime results in finite lists. For a residue set R,
  `R&{x-1for x in R}` contains precisely the residues whose
  successor is also in R; its minimum is the original first-pair
  test. The fallback `{0}` represents an empty intersection.

**Which finite color patterns are realizable**

Let K be Q(zeta_n) with n-th roots of the finitely many assigned
positive rational primes adjoined. Kummer theory describes the
relations among their exponents. A positive real radical in the
abelian field Q(zeta_n) has at most two conjugates: every conjugate
is real, so the root-of-unity ratio is 1 or -1. Consequently the
only nontrivial rational radical relations are quadratic.
They are exactly the squarefree r with positive fundamental
discriminant D_r dividing n, where D_r=r if r=1 mod 4, otherwise
D_r=4r. Frobenius a acts on sqrt(r) by the Jacobi symbol (r/a).
For even d this requires sum(f(p),p dividing r)=(1-(r/a))/2 mod 2;
for odd d the parity can be chosen independently and imposes no
condition. These are the conditions constructed by the program.
All supported relations are checked when their largest prime is
assigned. Kummer duality shows they suffice to extend the pattern,
and Chebotarev realizes the resulting Frobenius conjugacy class
at arbitrarily large rational primes. Existence of a fixed root
of X^n-m is conjugacy invariant and is equivalent to f(m)=0.

**The exhaustive search terminates mathematically**

Extend f(1)=0 in increasing integer order. At a prime, branch
over its colors; at a composite x, derive f(x) from the smallest
prime factor and x divided by that factor. Stop a branch at its
first adjacent zeros and return the largest such first position.
Multiplication of all colors by a unit preserves the kernel and
all parity relations, so at the first prime 2 it suffices to use
0 and proper divisors of d as representatives. Hildebrand's
uniform theorem bounds the first adjacent zeros for every
completely multiplicative root-of-unity-valued function. Thus
this finitely branching tree has bounded depth and is finite.
Take the maximum over Frobenius types. Primes dividing n are
ramified exceptions and are checked directly by modular powers.
For every other prime smaller than the finite search range, any
existing first pair is below that prime; larger primes are covered
by the realizable patterns above. This proves the resulting maximum.

References: [Hildebrand's theorem, in Dietzel (2019)](https://msp.org/cnt/2019/8-2/moscow-v8-n2-p10-s.pdf),
[Kummer theory](https://websites.math.leidenuniv.nl/algebra/Stevenhagen-Kummer.pdf),
and the OEIS references on consecutive power residues.

**Notes**

- For the first value, modulo 43 the first consecutive positive
  quadratic residues are 9 and 10. This witnesses the lower bound
  a(2)≥9; the exhaustive color search and theorem give the matching
  global upper bound, rather than assuming a prime scan has stabilized.
- The six b-file values are not stored in the program. Its only
  initial colors express f(1)=0; all output values arise from
  branching, arithmetic and the realizability conditions.
- `P` is cached because the same integers occur on many
  branches. The color lists and recursion, however, are explored
  exhaustively, so larger exponents have severe time and memory
  costs. Deep searches can meet CPython's default recursion limit.
- Mathematical termination and practical completion are distinct:
  Hildebrand's uniform bound proves a finite tree, without making
  that tree small enough to traverse within the verification timeout.
- The b-file has 6 terms (indices 2 through 7). The bar is the
  first 2 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 1350 | first entry |
| 2026-11-06 | Python 3 | 1146 | shorten identifiers and equivalent expressions |
| 2026-11-06 | Python 3 | 975 | compress Jacobi signs, color search and Frobenius-type deduplication |
| 2026-11-06 | Python 3 | 934 | generate quadratic relations lazily and combine finite maxima |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000445), CC BY-SA 4.0.
