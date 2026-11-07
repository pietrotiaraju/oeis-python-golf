# A000445

> Latest possible occurrence of the first consecutive pair of n-th power residues, modulo any prime.
> — [OEIS A000445](https://oeis.org/A000445)

Offset 2: 9, 77, 1224, 7888, 202124, 1649375, …

For a prime p let r(p) be the least r ≥ 1 with r and r + 1 both nonzero n-th
power residues mod p (if there is one). a(n) is the largest r(p) over all
primes; for n = 2 it is reached at p = 43, whose first such pair is 9, 10.

### Python 3 — 311 bytes

```python
from math import*
n=1
while n:=n+1:
 m=0;S=[[a,0]for a in range(n)if gcd(a,n)<2]
 while S:
  x=len(F:=S.pop());a=F[0];d=gcd(a-1,n);p=2;m+=x-1>m
  while x%p:p+=1
  S+=[F+[c]for c in[(F[p%x]+F[x//p])%d][:p<x]or range(d)if c*2<=d*~-x>0<c|F[-1]if n%(x*(2+(x&2)))or~c+sum(i*2<a<i*x%a*2for i in range(a))&1]
 print(m)
```

The program prints a(n) without looking at a single prime: it searches all
patterns of residues that large primes can have.

**How it works**

- **Colours.** For a prime p ∤ n put d = gcd(n, p − 1). Then x is an n-th
  power residue mod p exactly when it is a d-th power residue, and with a
  primitive root g the index of x modulo d gives a colour f(x) ∈ ℤ/d with
  f(xy) = f(x) + f(y) and f(1) = 0. The residues are the zeros of f, and
  r(p) is the first x with f(x) = f(x+1) = 0.
- **Which colourings occur.** Let p ≡ a (mod n), so d = gcd(a − 1, n). The
  colours of the primes q < N are the Frobenius of p in
  Q(ζ_d, q^(1/d), …) (Kummer theory), and its Frobenius in Q(ζ_n) is
  a ↦ ζ_n^a. The two must agree on the intersection of the fields. A
  positive real radical in the abelian field Q(ζ_n) has only real
  conjugates, which differ from it by roots of unity, so by ±1: it is a
  square root. Hence the intersection is generated over Q(ζ_d) by the √r
  with r a squarefree product of the q and √r ∈ Q(ζ_n), that is with the
  discriminant D_r (r if r ≡ 1 (mod 4), else 4r) dividing n. On √r the
  class a acts by the Jacobi symbol (r/a); the colours act by
  (−1)^f(r) when d is even, since √r = (r^(1/d))^(d/2), and the condition
  is empty when d is odd. By Chebotarev's theorem every colouring with
  f(r) ≡ [(r/a) = −1] (mod 2) for these r is the colouring of infinitely
  many primes p ≡ a (mod n).
- **No special primes.** A small prime p ∤ n is unramified in the same
  fields, so the colours of 1, …, p − 1 under p also belong to large
  primes, with the same first pair. For p | n the first pair, if any, is at
  most p − 2 ≤ n − 2, below the lower bound a(n) ≥ n − 1 shown below. So
  a(n) is the largest first pair over all classes a and all allowed
  colourings.
- **The search.** The stack S holds lists F = [a, f(1), …, f(x−1)] for
  the units a mod n. For the next position x, `while x%p:p+=1` finds the
  least prime factor p. If p < x the colour is forced,
  f(x) = f(p) + f(x/p), the one-element list `[…][:p<x]`; at a prime p = x
  the slice is empty and `or range(d)` branches over all colours (`p%x`
  keeps the unused index in range). A child is pushed only if it passes
  the conditions below and `c|F[-1]` is nonzero, so a list never contains
  two adjacent zeros.
- **The answer.** m is the largest x − 1 over all popped lists, the
  longest pair-free start. Past position n no condition applies, so every
  list there has an allowed next colour, which either closes a pair or
  gives a child: the longest list is followed by a first pair, and every
  list longer than n starts a colouring whose first pair is no earlier.
  Lists that die at a condition end below n, under a(n) ≥ n − 1. So m is
  the largest first pair. A list is popped after its parent, so
  x − 1 ≤ m + 1 and `m+=x-1>m` keeps the maximum.
- **The parity condition.** `n%(x*(2+(x&2)))` is 0 when n is even and
  x | n for x ≡ 0, 1 (mod 4), 4x | n for x ≡ 2, 3 (mod 4). For squarefree x
  this is D_x | n. If n is even every unit a is odd and d is even; if n is
  odd, d is odd and no x passes, as required. For x = s²·r with r
  squarefree the test implies D_r | n, and the condition for x is the one
  for r, since f(x) = 2f(s) + f(r) and (x/a) = (r/a); these extra checks
  are true and redundant. The count `sum(i*2<a<i*x%a*2for i in range(a))`
  is the number of i < a/2 with i·x mod a > a/2, so by Schering's form of
  Gauss's lemma (odd a, gcd(x, a) = 1, which holds as x | n) (x/a) is −1
  to that power. `~c+…&1` is 1 when c and the count have the same parity.
- **Where it is checked.** The condition for x is checked when f(x) is
  set, not at the largest prime of x. A list that breaks it was counted
  only at positions below x ≤ n, which cannot beat a(n) ≥ n − 1.
- **Symmetry.** Multiplying all colours by −1 keeps the zeros and, when d
  is even, the parities, so at x = 2 one colour of each pair c, d − c is
  enough. `c*2<=d*~-x` keeps 2c ≤ d at x = 2 and always holds for x ≥ 3
  (2c < 2d ≤ d(x−1)); c = 0 at x = 2 is the pair 1, 2. This halves the
  search for d = 3.
- **The lower bound.** In the class a = 1 (d = n, every condition asks
  for f(r) even) colour every prime 1 if n is odd or n = 2, and 2 if n ≥ 4
  is even. Then f(m) = 0 needs n | Ω(m), resp. n/2 | Ω(m), so the first pair
  is above 2ⁿ, resp. 2^(n/2), and for n = 2 it is 9. All are ≥ n − 1.
- **It ends.** Hildebrand (1991) proved that a completely multiplicative
  function with values in the d-th roots of unity has f(m) = f(m+1) = 1
  for some m ≤ c(d), uniformly in the function. (A short Schur-type proof,
  arXiv 1309.7506: colour the integers by f, find x | y with
  f(x) = f(y) = f(x+y) below a Ramsey bound, and take m = y/x.) A list of
  the search extends to such a function, so no list is longer than
  c(d) + 1, the tree is finite and the loop over n moves on.

**Notes**

- Other versions that print the same terms:
  - without the symmetry at x = 2, `if c|F[-1]if`: 298 bytes, but the bar
    then takes 6.4 s of CPU instead of 2.9 s;
  - f(x) from every factorisation,
    `{(F[k]+F[x//k])%d for k in range(2,x)if x%k<1}or range(d)` in place
    of the factor loop: 308 bytes and about 10 s for the bar;
  - one search per distinct pair (d, conditions), Jacobi symbols by
    reciprocity, conditions at the largest prime and the primes dividing
    n checked by modular powers: 874 bytes, about as fast.
- Exact integer arithmetic. That the search gives a(n) for every n rests
  on the Kummer and Chebotarev argument above, and that it ends on
  Hildebrand's theorem. Compared with real primes 10⁴ < p < 10⁶ for
  n = 5, 8, 10, 12, 20, 24, 40 (residue patterns of 1, …, 12, or fewer for
  large d), every pattern of a prime is one of the search, and dropping
  the parity condition adds patterns no prime shows.
- a(3) is printed after about 3 s of CPU here (3 to 5 s of wall time on
  the shared machine). n = 4 needs a search deeper than 1224 positions
  with four colours at every prime and does not finish in 40 s; the stack
  stays small (10 MB of memory then).
- The b-file has 6 terms (up to a(7)); the bar is 2 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 1350 | first entry |
| 2026-11-06 | Python 3 | 1146 | shorten identifiers and equivalent expressions |
| 2026-11-06 | Python 3 | 975 | compress Jacobi signs, color search and Frobenius-type deduplication |
| 2026-11-06 | Python 3 | 934 | generate quadratic relations lazily and combine finite maxima |
| 2026-11-06 | Python 3 | 874 | recursive Jacobi symbol, squarefree-divisor comprehension and ordered parity checks |
| 2026-11-07 | Python 3 | 311 | one stack for all classes, parity by Schering's lemma at x itself, no special primes |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000445), CC BY-SA 4.0.
