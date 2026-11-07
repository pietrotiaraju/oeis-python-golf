# A000874

> Number of switching networks with S(n) and C(2,2) acting on the domain and GL(2,2) acting on the range.
> — [OEIS A000874](https://oeis.org/A000874)

Offset 1: 4, 16, 392, 1966074, 800887365826790, …

### Python 3 — 252 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(C:=lambda j,m=2*lcm(*L):1<<sum(prod((t*j//(g:=gcd(t*j,l))%2*l<1)<<g for l in L)for t in range(m))//m)(1)**2+3*C(2)+2*C(3)//C(1)
n=1
while[print(f(n)//6)]:n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}² (n inputs, 2 outputs) up to f ↦ h∘f∘g, where g runs
  over the 2ⁿ·n! maps that permute and complement the inputs (the
  hyperoctahedral group B_n) and h over GL(2,2), the 6 invertible linear maps
  of the outputs. The OEIS name gives the groups (its "S(n) and C(2,2)" on the
  domain means permuting and complementing the inputs; brute force confirms).
  A brute-force Burnside over all pairs (g, h) matches the data for n ≤ 4.
- Burnside: a(n) = Σ_g,h fix(g,h) / (|B_n|·|H|). A pair fixes f when f(g(x)) =
  h(f(x)) for every x, so f is free at one input of each cycle C of g on the
  2ⁿ inputs, and there its value y must satisfy h^|C|(y) = y. So fix(g,h) =
  Π_C Fix(h^|C|), Fix counting the outputs a map fixes.

**Cycles of g and of its powers**

- An element g of B_n is a signed permutation of the n coordinates: cycles of
  lengths l, each with a sign (the parity of the complemented coordinates
  along it). gᵗ fixes Π_l 2^gcd(t,l) inputs, the factor being 0 for a negative
  cycle when t/gcd(t,l) is odd (see [A000157](../A000157/)). The order of g
  divides m = 2·lcm(l), so Burnside's lemma for ⟨g⟩ counts the cycles of g^j:
  c_j = (1/m)·Σ_{t<m} fix(g^(jt)). Write C_j = 2^c_j, the number of Boolean
  functions fixed by g^j.

**The weight**

- The identity gives 4^c₁. The 3 involutions fix a line (2 outputs) and square
  to the identity: 2^(#odd)·4^(#even) = 2^c₂, as c₂ = #odd + 2·#even. The 2
  maps of order 3 fix only 0 and cube to the identity: a cycle of g takes 4
  values if 3 divides its length and 1 otherwise, 4^N₃ with N₃ the number of
  such cycles; since c₃ = Σ_C gcd(|C|,3) = c₁ + 2N₃, that is 2^(c₃−c₁).
- So W(g) = C₁² + 3C₂ + 2C₃/C₁.

**How it works**

- `f(r,*L)` is the recursion of [A000157](../A000157/): it averages the weight
  W(g) = Σ_h fix(g,h) over the signed permutations of r more coordinates,
  given the signed cycles `L` already chosen (positive cycles as negative
  numbers). The cycle through the next coordinate has length k with
  probability 1/r and either sign with probability 1/2, so `//r>>1` divides
  the sum over k = ±1…±r by 2r. It visits 2·3ⁿ⁻¹ signed compositions instead
  of the 2ⁿ·n! group elements.
- The floors are exact: for each h, the average over B_r of fix(bτ, h), τ the
  signed cycles already chosen, is the number of B_r-orbits that (τ, h) maps
  to themselves (de Bruijn's lemma), an integer.
- At r = 0, the lambda `C(j)` is C_j = 2^c_j, the sum over t written as
  fix(g^(tj)) for t < m (`t*j`); `C(3)//C(1)` is exact.
- `f(n)` is Σ_g W(g)/|B_n|, so `f(n)//6` is a(n), with |H| = 6.

**Notes**

- Exact integer arithmetic. All 7 listed terms print in well under a second,
  and 11 terms in 60 s here; from a(13) on the terms pass Python's 4300-digit
  limit for printing integers, which stops the program with a `ValueError`.
  The b-file is the OEIS data (7 terms) and the bar is all of it.
- B_n on the inputs with the other range groups (m = 2/3): trivial
  [A000814](../A000814/)/[A000815](../A000815/), S(m)
  [A000829](../A000829/)/[A000830](../A000830/), C(2,m)
  [A000844](../A000844/)/[A000845](../A000845/), S(m) and C(2,m)
  [A000859](../A000859/)/[A000860](../A000860/), GL(m,2)
  A000874/[A000875](../A000875/), AG(m,2)
  [A000889](../A000889/)/[A000890](../A000890/). The same range group with
  only complementing inputs: [A000868](../A000868/)/[A000869](../A000869/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 252 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000874), CC BY-SA 4.0.
