# A000840

> Number of cubic bicolored graphs on n unlabeled nodes admitting an automorphism exchanging the colors.
> — [OEIS A000840](https://oeis.org/A000840)

Offset 1: 0, 0, 1, 1, 2, 5, 12, 31, 90, 285, 938, 3285, 11983, 45390, 177803, 718390, 2986407, 12749364, 55802982, 250068732, …

### Python 3 — 388 bytes

```python
from math import*
from functools import*
f=cache(lambda n,R:sum(perm(n-1,p)*f(n+~p,(*sorted(R+((3,p+1),)),))for p in range(n))if n else R==()or g(R[1:],*R[0]))
def g(R,e,a,N=[]):
 if R:(s,b),*R=R;G=gcd(a,b);return sum(comb(G,m)*g(R,e-m*b//G,a,N+[(s-m*a//G,b)])for m in range(min(e*G//b,s*G//a)+1))
 return(a|~e)%2*comb(a//2,e//2)*f(0,(*sorted(N),))
n=1
while[print(f(n,())//perm(n))]:n+=1
```

**The count**

A cubic bicolored graph with n nodes of each colour is an n×n 0/1 matrix M
(rows = one colour, columns = the other) with every row and column sum 3,
taken up to independent row and column permutations, the group
H = S_n × S_n. It has an automorphism exchanging the colours exactly when
its H-orbit is fixed by transposition τ, and by Burnside's lemma for
H ∪ Hτ the number of H-orbits fixed by τ is the average number of fixed
matrices over the coset Hτ. Conjugating by H turns (α, β)τ into (αβ, 1)τ,
so

a(n) = (1/n!) · Σ_{γ ∈ S_n} #{M : M = (γ, 1)τ·M}.

The matrices fixed by (γ, 1)τ satisfy M(i, j) = M(j, ψ(i)) for a
permutation ψ with the cycle type of γ (so also M(ψi, ψj) = M(i, j), and
row i has the sum of column ψ(i)). The cells split into orbits:

- inside one cycle of length a, with ψ(i) = i + 1 (mod a), the cells
  (i, i + δ) for one δ form a class meeting every row once, and the
  relation pairs δ with 1 − δ: there are ⌊a/2⌋ orbits giving each row 2,
  and for odd a one more (2δ ≡ 1) giving each row 1;
- between cycles of lengths a and b there are g = gcd(a, b) orbits, each
  giving every row of the a-cycle b/g and every row of the b-cycle a/g.

So the term for γ depends only on its cycle type, and counts the sets of
orbits that give every cycle the row sum 3.

**How it works**

- `f(n,R)` with n > 0 is the sum over γ: the cycle through the smallest of
  the n remaining points has length p + 1, in perm(n−1, p) ways. `R` holds
  the cycles as pairs (row sum still needed, length), sorted so that every
  multiset is cached once; the main loop divides by n!.
- `f(0,R)` takes the first cycle (e, a) and `g` walks through the others.
  For a cycle (s, b) it chooses m of the G = gcd(a, b) orbits, in C(G, m)
  ways, taking m·b/G from e and m·a/G from s; the range bound stops either
  from going below 0. The visited cycles collect in `N`.
- When the walk is over, the orbits inside the current cycle must give the
  last e: C(⌊a/2⌋, ⌊e/2⌋) ways, and none when a is even and e odd, which is
  `(a|~e)%2`. The other cycles go back, sorted, to the cached `f`; those
  that already have their 3 simply pass through.
- Only `f` is cached: one cached function for every step of the walk is
  shorter, but it was slower and used ten times the memory.

**Notes**

- Exact integer arithmetic, correct for every n (Burnside's lemma and the
  orbit count above; the output matches every OEIS term it reaches).
- The b-file is the OEIS data, n = 1 to 30 (a(11) onwards from Andrew
  Howroyd's computation). On this PC the program prints 26 terms in 60 s,
  using about 150 MB; the bar is 20 terms in 60 s.
- The recursion is about n²/2 calls deep for the identity (n cycles of
  length 1), so Python's default limit of 1000 frames stops it near n = 32.
- [A000843](../A000843/) is the same program for the quartic case
  (`4` in place of `3`).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 388 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000840), CC BY-SA 4.0.
