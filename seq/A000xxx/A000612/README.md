# A000612

> Number of P-equivalence classes of switching functions of n or fewer variables, divided by 2.
> — [OEIS A000612](https://oeis.org/A000612)

Offset 0: 1, 2, 6, 40, 1992, 18666624, 12813206169137152, …

### Python 3 — 175 bytes

```python
from math import*
f=lambda r,*L:r<1and 1<<sum(2**sum(map(gcd,L,[t]*n))for t in range(lcm(*L)))//lcm(*L)-1or sum(f(r+k,*L,k)for k in range(-r,0))//r
n=0
while[print(f(n))]:n+=1
```

**What is counted**

- P-equivalence permutes the inputs: the classes are the orbits of Sₙ on the
  2^(2ⁿ) functions on the 2ⁿ points, which are the subsets of {1,…,n}. By
  Burnside's lemma there are Σ_σ 2^c(σ) / n! of them, where c(σ) is the
  number of cycles of σ on the subsets.
- Every σ fixes the empty set, so the value there is free and the count is
  even; a(n) = Σ_σ 2^(c(σ)−1) / n!, the number of classes of sets of
  nonempty subsets (the OEIS comment on hypergraphs).
- If σ has cycle lengths L, σᵗ splits a cycle of length l into gcd(t,l)
  cycles and fixes the 2^Σgcd(t,l) subsets that are unions of them. The
  order of σ is lcm(L), so Burnside's lemma for ⟨σ⟩ gives
  c(σ) = (1/lcm L) Σ_{t<lcm L} 2^Σgcd(t,l).

**How it works**

- `f(r,*L)` is the recursion of [A000273](../A000273/): it averages over
  the permutations of r further points, choosing the length k of the cycle
  through one fixed point (probability 1/r each), so
  f(r,L) = Σ_k f(r−k, L+[k]) / r. Lengths are stored negated, `k` runs over
  `range(-r,0)`, and `gcd` and `lcm` ignore the sign.
- At r = 0 the leaf is 2^(c(σ)−1): `map(gcd,L,[t]*n)` pairs t with every
  cycle (there are at most n), and `-1` halves the count. For n = 0 the
  empty cycle list gives lcm() = 1 and the single empty set, so a(0) = 1.
- The floors are exact: by de Bruijn's lemma the full count at each level is
  the number of Sᵣ-orbits that the permutation already chosen maps to
  themselves, an integer, and these come in pairs differing at the empty
  set, so half of it is an integer too.

**Notes**

- The recursion has 2^(n−1) leaves: the 13 b-file terms (n = 0 to 12) take
  well under a second, and the bar is the whole b-file, 13 terms in 60 s.
- a(14) has more than 4300 digits, so printing it stops the program with
  Python's integer-to-string limit, after the b-file is done.
- Walking all n! permutations on the 2ⁿ points directly (the
  [A000370](../A000370/) frame) is 202 bytes and reaches only n = 8 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 175 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000612), CC BY-SA 4.0.
