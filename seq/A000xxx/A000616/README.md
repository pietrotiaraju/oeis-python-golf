# A000616

> a(-1)=1 by convention; for n >= 0, a(n) = number of irreducible Boolean functions of n variables.
> — [OEIS A000616](https://oeis.org/A000616)

Offset -1: 1, 2, 3, 6, 22, 402, 1228158, 400507806843728, …

### Python 3 — 219 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and 1<<sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(m))//m
n=-1
while[print(f(n)>>(n<0))]:n+=1
```

**What is counted**

- For n ≥ 0, a(n) is the number of NP-equivalence classes of Boolean functions
  of n variables: orbits of the group B_n of 2ⁿ·n! maps g(x) = P·x ⊕ s
  (permute and negate inputs) on the 2^(2ⁿ) functions. By Burnside's lemma
  a(n) = Σ_g 2^c(g) / |B_n|, where c(g) is the number of cycles of g on the
  2ⁿ points.
- An element of B_n is a signed permutation of the n coordinates; each of its
  cycles has a length l and a sign, the parity of the number of negations
  along it. g^t splits a cycle of length l into gcd(t,l) cycles, and on a
  negative cycle each of them has sign (−1)^(t/gcd(t,l)). A signed cycle
  fixes 2 patterns of its coordinates when positive and none when negative,
  so g^t fixes Π 2^gcd(t,l) points, the factor of a negative cycle being 0
  when t/gcd(t,l) is odd.
- The order of g divides m = 2·lcm(lengths), and Burnside's lemma for the
  cyclic group ⟨g⟩ gives c(g) = (1/m) Σ_{t<m} fix(gᵗ).

**How it works**

- `f(r,*L)` averages over the signed permutations of r further coordinates,
  given the signed cycles `L` chosen so far (negative entries are positive
  cycles, positive entries negative ones, so `l<1` means "always fixes").
  The cycle through one chosen coordinate has length k with probability 1/r
  and either sign with probability 1/2, so f(r,L) = Σ_{k,±} f(r−k, L+[±k]) /
  (2r): `k` runs over ±1…±r, `r-abs(k)` coordinates are left, and `//r>>1`
  divides by 2r.
- At r = 0, `prod(…)` is fix(gᵗ): `(t//g%2*l<1)<<g` is 2^gcd(t,l) unless l > 0
  (a negative cycle) and t/gcd(t,l) is odd. `1<<sum(…)//m` is 2^c(g).
- The floors are exact. f(r,L) is (1/|H|) Σ_{h∈H} fix(hτ) with H = B_r and τ
  the signed permutation already chosen; by de Bruijn's lemma (for H normal
  in G and τ in G this is the number of H-orbits that τ maps to themselves)
  it is an integer.
- f(−1) skips the recursion (an empty range) and returns 2 from the empty
  cycle list; `>>(n<0)` halves it for the conventional a(−1) = 1 only.

**Notes**

- The recursion visits 2·3^(n−1) signed compositions of n: the 12 b-file
  terms (n = −1 to 10) take about 3 s, n = 11 about 10 s. The bar is the
  whole b-file, 12 terms in 60 s.
- The terms beyond the b-file grow like 2^(2ⁿ)/(2ⁿ·n!); from n = 14 they pass
  Python's 4300-digit limit for printing integers, long after the timeout.
- [A000618](../A000618/) prints the differences and [A000610](../A000610/)
  keeps only the elements without fixed points. The cycle-type recursion is
  the one of [A000273](../A000273/) and [A000171](../A000171/), with signs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 219 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000616), CC BY-SA 4.0.
