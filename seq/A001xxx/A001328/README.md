# A001328

> Number of equivalence classes of n-valued Post functions of 2 variables under action of semi-direct product of symmetric groups S_2 and S(2,n).
> — [OEIS A001328](https://oeis.org/A001328)

Offset 2: 6, 438, 3962646, 10417184196975, 9954761196199929077325, …

a(n) counts the functions f: {0,…,n−1}² → {0,…,n−1} up to swapping the two
variables and permuting the values of each variable separately
(S(2,n) = Sₙ², of order n!²). Only the inputs are transformed. Together the
two give the wreath product Sₙ ≀ S₂, of order 2·n!²: n×n tables with
entries in {0,…,n−1} up to permuting rows, permuting columns and
transposing.

### Python 3 — 208 bytes

```python
from math import*
R=lambda F,r,*L:r and sum(R(F,r+k,*L,k)for k in range(-r,0))//r or F(*L)
n=2
while[print(R(lambda*L:R(F:=lambda*M:n**sum(gcd(a,b)for a in L for b in M),n)+isqrt(F(*L,1,1)//F(2)),n)//2)]:n+=1
```

**What is counted**

- By Burnside's lemma a(n) is the average of n^c(g) over the group, where
  c(g) is the number of cycles of g on the n² inputs (a function is fixed
  exactly when it is constant on each cycle).
- Half of the elements are (x,y) ↦ (σx, τy). A cycle of σ of length a and
  one of τ of length b cover ab points in orbits of length lcm(a,b), so
  c = G(σ,τ) = Σ_{i,j} gcd(aᵢ, b_j) over the cycle lengths aᵢ of σ and
  b_j of τ.
- The other half are (x,y) ↦ (σy, τx). Conjugating by (x,y) ↦ (x, τ⁻¹y)
  turns this into (x,y) ↦ (πy, x) with π = στ, and π takes every value n!
  times. Its square is π×π. For two cycles of π of lengths a and b, the
  2ab points of A×B ∪ B×A form gcd(a,b) cycles (each alternates between the
  two halves and has length 2·lcm(a,b)). A single cycle of length a gives
  a² points in a classes {(x, πᵈx)}, which the map pairs up as d ↔ −d−1
  (mod a); every class or pair of classes is one cycle, so ⌈a/2⌉ cycles.
  In all c = Σ_{i<j} gcd(aᵢ, a_j) + Σ ⌈aᵢ/2⌉ = (G(π,π) + #odd cycles)/2.
- So a(n) = (A + B)/2 with A the average of n^G(σ,τ) over σ, τ in Sₙ and B
  the average of n^((G(π,π)+#odd)/2) over π in Sₙ.

**How it works**

- `R(F,r,*L)` is the average over the permutations of r further points of
  `F` at all the cycle lengths: the cycle through one chosen point has
  length k with probability 1/r, so R(F,r,L) = Σ_k R(F, r−k, L+[k]) / r.
  Lengths are stored negative (`k` runs over −r…−1, `r+k` points are left);
  `gcd` ignores the sign.
- The outer `R` runs over σ (or π) with cycle lengths `L`. `F(*M)` is
  n^Σ gcd(a,b) over a in `L` and b in `M`, and the inner `R(F,n)` averages it
  over τ: that is A's share. Adding two cycles of length 1 adds 2·|L| to
  the exponent and one of length 2 adds Σ gcd(a,2) = #odd + 2·#even, so
  `F(*L,1,1)//F(2)` is n^(G(π,π)+#odd) (an exact division of powers of n),
  and `isqrt` of that perfect square is B's share.
- The floors are exact. Each inner average is (1/|H|) Σ_{h∈H} fix(hτ) for
  H the permutations of the remaining points, and each outer one is a sum
  of two such averages, the second over the coset (x,y) ↦ (αy, βx), whose
  representative normalizes H×H. By de Bruijn's lemma (for H normal in G
  and τ in G this is the number of H-orbits that τ maps to themselves)
  they are integers. The final sum is 2·a(n), and `//2` halves it.
- Exact integers throughout, so the program is right for every n.

**Notes**

- Writing B as `isqrt(F(*L)*n**sum(a%2for a in L))` costs 12 more bytes,
  and as `n**(sum(a%2+sum(map(gcd,L,[a]*n))for a in L)>>1)` 23 more. An
  inner recursion over τ with an incremental factor, as in
  [A000088](../../A000xxx/A000088/), makes 252 bytes.
- a(3) = 438 is [A001327](../A001327/)(2): the same count for 3 values and
  2 variables.
- Both recursions run over compositions of n, so a term takes 4^(n−1) calls
  of the inner `F`: the 8 b-file terms print in about 1 s, a(10) in about 16 s.
  The terms grow like n^(n²)/(2·n!²) and stay below Python's 4300-digit
  limit for printing integers until well past the timeout.
- The OEIS b-file is synthesized from the entry: 8 terms (n = 2 to 9). The
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 208 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001328), CC BY-SA 4.0.
