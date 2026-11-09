# A001173

> Half the number of binary relations on n unlabeled points.
> — [OEIS A001173](https://oeis.org/A001173)

Offset 1: 1, 5, 52, 1522, 145984, 48464496, 56141454464, 229148550030864, 3333310786076963968, …

### Python 3 — 135 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<2*sum(map(math.gcd,L,[k]*n))-k for k in range(-r,0))//r
n=1
while[print(f(n)//2)]:n+=1
```

Half of [A000595](../../A000xxx/A000595/) (binary relations); the program is
the loop-free digraph program of [A000273](../../A000xxx/A000273/) with the
loops put back.

**What is counted**

- A binary relation on n labelled points is a subset of all n² ordered pairs
  (x, y), loops (x, x) included. By Burnside's lemma the number up to
  relabelling is (1/n!) Σ_π 2^D(π), where D(π) is the number of orbits of π
  on ordered pairs.
- If π has cycle lengths l₁, …, l_c, a cycle of length l holds l orbits of
  pairs inside it (the pairs (x, πᵗx), t = 0, …, l − 1, the loops being
  t = 0), and two cycles of lengths l, m hold gcd(l, m) orbits in each
  direction. So D(π) = Σᵢ lᵢ + 2 Σ_{i<j} gcd(lᵢ, lⱼ).
- The count is even, so the halving is exact. Grouped by cycle type λ the
  count is Σ_λ 2^D(λ)/z_λ. Since z_λ divides n!, its power of 2 is at most
  that of n!, which is n − (number of 1 bits of n) ≤ n − 1, while D(λ) ≥ n.
  So half the count is a sum of fractions with odd denominators; it is also a
  multiple of ½, hence an integer.

**How it works**

- `f(r,*L)` sums over the permutations of r further points, given the lengths
  `L` of the cycles chosen so far: it picks the length k of the cycle through
  one fixed point, which brings 2^k for the pairs inside it and 4^gcd(k, l)
  for each earlier cycle l, so each term is `f(…)<<2*Σgcd+k`.
- Lengths are stored negated: k runs over `range(-r,0)`, the points left are
  `r+k`, the shift is `2*sum(…)-k`, and `gcd` ignores the sign.
- `[k]*n` gives `map` a second argument at least as long as `L` (at most n
  cycles). `r<1or` returns `True` (1) when no points are left.
- `//r` at every level is exact, for the reason given on
  [A000273](../../A000xxx/A000273/) (de Bruijn's form of Burnside's lemma:
  each partial sum counts orbits of S_r that a fixed permutation of the other
  points maps to themselves). The final `//2` halves an even number.

**Notes**

- Exact for every n.
- The recursion visits all 2^(n−1) compositions of n, so the time doubles with
  every term: 21 terms in 13 s on the PC it was written on. The b-file has 59;
  the bar is 21 terms in 60 s.
- Caching `f` on sorted `L` (`functools.cache`, 173 bytes) reaches about 42
  terms in the same time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 135 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001173), CC BY-SA 4.0.
