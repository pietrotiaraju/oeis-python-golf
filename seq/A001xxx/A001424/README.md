# A001424

> Number of nonisomorphic and nonantiisomorphic groupoids with n elements.
> — [OEIS A001424](https://oeis.org/A001424)

Offset 0: 1, 1, 7, 1734, 89521056, 1241763995193675, …

A groupoid (magma) is a set with one binary operation and no axioms. Two
are identified when a relabelling of the points turns one operation into
the other (isomorphism) or into the other with its arguments swapped,
x∘y ↦ y∘x (anti-isomorphism).

### Python 3 — 280 bytes

```python
def f(r,k,p,*L):
 if r:return sum(f(j,k,p+[*range(n-r+1,n-j),n-r],*L,r-j)for j in range(r))//r
 c=1
 for q in range(n*n):
  o=[e:=q]
  while(e:=p[e//n]*k+p[e%n]*n//k)!=q:o+=[e]
  c*=sum(l>>len(o)%l*l for l in L)**(q==min(o))
 return c
n=0
while[print(f(n,1,[])+f(n,n,[])>>1)]:n+=1
```

**How it works**

- Burnside's lemma for the group S_n × {identity, transpose}: a(n) is
  half the sum of the average over the permutations π of the operations
  fixed by π and the average of those fixed by π followed by the swap.
  The first average is [A001329](../A001329/)(n), the second A029850(n),
  the formula in the entry.
- Both kinds of symmetry act on the pairs (x, y) by a permutation σ,
  (x, y) ↦ (πx, πy) or (x, y) ↦ (πy, πx), and an operation ∘ is fixed
  when (σq)∘ = π(q∘) for every pair q. On an orbit of σ of length m it
  is fixed by its value z at one pair, and z can be any point with
  π^m(z) = z: S(m) = Σ_{l∈L, l | m} l choices, with L the cycle lengths
  of π, written `sum(l>>m%l*l for l in L)` (a shift by at least l bits
  clears l). So |Fix| = Π over the orbits of σ of S(m).
- The program walks the orbits explicitly. A pair is q = x·n + y and the
  permutation is the list p, so `p[e//n]*k+p[e%n]*n//k` is
  πx·n + πy for k = n and πy·n + πx for k = 1. The walk from q collects
  its orbit o, and only the pair `min(o)` multiplies c by S(len(o)), once
  per orbit.
- The average over π is the cycle-by-cycle recursion of A001329, which
  here also builds p: the cycle through the first of the r points still
  free (points n − r … n − j − 1) has length r − j with probability 1/r,
  and `range(n-r+1,n-j),n-r` lists where those points go. `//r` is exact:
  f(r, …) is the average over the permutations σ of the r free points of
  the operations fixed by gσ, with g the partial permutation (twisted or
  not) on the points already used. g commutes with every such σ, and for
  g normalizing a group N the average of |Fix(gσ)| over σ ∈ N is the
  number of N-orbits that g maps to themselves, an integer.

**Notes**

- Exact integer arithmetic and an explicit orbit walk, so the program is
  right for every n; a(0) = (1 + 1)/2, empty products.
- The b-file has 9 terms (a(0) to a(8)); the bar is the whole b-file in
  60 s, which takes about 0.1 s (a(10) after 0.7 s).
- Closed forms for both products (gcd/lcm of the cycle lengths, with
  cases i mod 4 for the swap inside one cycle and lcm(2, i, j) between
  two cycles) came to 338 bytes, 58 more than the walk.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 280 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001424), CC BY-SA 4.0.
