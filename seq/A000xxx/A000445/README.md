# A000445

> Latest possible occurrence of the first consecutive pair of n-th power residues, modulo any prime.
> — [OEIS A000445](https://oeis.org/A000445)

Offset 2: 9, 77, 1224, 7888, 202124, 1649375, …

### Python 3 — 1146 bytes

```python
from math import gcd,isqrt
from functools import cache
def J(a,n):
 t=1;a%=n
 while a:
  while a%2<1:
   a//=2
   if n%8 in(3,5):t=-t
  a,n=n,a
  if a%4==n%4==3:t=-t
  a%=n
 return t*(n==1)
@cache
def P(n):
 return next((p for p in range(2,isqrt(n)+1)if n%p<1),n)
def Q(n):
 O=[]
 for r in range(2,n+1):
  D=r if r%4==1 else 4*r
  if n%D:continue
  x=r;u=[]
  while x>1:
   p=P(x);x//=p
   if x%p<1:break
   u.append(p)
  else:O.append((r,u))
 return O
def S(d,C):
 def f(F):
  x=len(F);p=P(x)
  U=range(d)if p==x else [(F[p]+F[x//p])%d]
  if x==2:U=[c for c in U if c==0 or d%c==0]
  B=0
  for c in U:
   V=F+[c]
   if any(max(u)==x and sum(V[p]for p in u)%2!=e for u,e in C):continue
   v=x-1 if c==F[-1]==0 else f(V)
   B=max(B,v)
  return B
 return f([0,0])
def V(n):
 L=Q(n);T=set();b=0
 for a in range(1,n):
  if gcd(a,n)>1:continue
  d=gcd(a-1,n)
  E=tuple((tuple(u),(1-J(r,a))//2)for r,u in L)if d%2==0 else ()
  if (d,E)in T:continue
  T.add((d,E));b=max(b,S(d,E))
 for p in range(2,n+1):
  if n%p<1 and P(p)==p:
   R={pow(x,n,p)for x in range(1,p)}
   b=max(b,min([x for x in R if x+1 in R]or[0]))
 return b
n=2
while 1:print(V(n));n+=1
```

**How it works**

The search uses a finite-color formulation; it does not embed the six known terms.
For each unit a modulo n put d=gcd(a-1,n). A large prime l
with l=a mod n has n-th-power residues described by the kernel
of a completely additive map f from positive rationals to Z/dZ.
Values on primes determine f.

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

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 2 terms in 10 s; the official b-file contains 6 terms.
- Exhaustive color search is expensive. The first two values are independently computed as 9 and 77. Later searches can exceed CPython's default recursion-depth limit, which the contribution rules explicitly treat as an interpreter limit rather than a mathematical failure. No conjectural stabilization in a scan of primes is assumed.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 1350 | first entry |
| 2026-11-06 | Python 3 | 1146 | shorten identifiers and equivalent expressions |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000445), CC BY-SA 4.0.
