# A000815

> Number of switching networks (see Harrison reference for precise definition).
> — [OEIS A000815](https://oeis.org/A000815)

Offset 1: 36, 666, 384112, 735192450952, 20632358601785638477436416, …

### Python 3 — 213 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and 1<<3*sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(m))//m
n=1
while[print(f(n))]:n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}³ (n inputs, 3 outputs) up to f ↦ h∘f∘g, where g runs
  over the 2ⁿ·n! maps that permute and complement the inputs (the
  hyperoctahedral group B_n) and h over the identity alone (no change on the
  outputs). The OEIS entry only says "see Harrison reference"; its first term,
  36 = (64 + 8)/2 for n = 1, fixes the groups. A brute-force Burnside over all
  pairs (g, h) matches the data for n ≤ 4.
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

- With h the identity, every cycle of g takes any of the 8 outputs: W(g) =
  fix(g) = 8^c₁. So a(n) = Σ_g 8^c₁ / |B_n|, the number of orbits of B_n on
  maps from {0,1}ⁿ to an 8-element set.

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
- At r = 0, `sum(prod(…)for t in range(m))//m` is c₁ and `1<<3*…` is 8^c₁
  (`3*S//m` is (3S)//m, exact).
- `f(n)` is Σ_g W(g)/|B_n| = a(n), printed as is.

**Notes**

- Exact integer arithmetic. All 6 listed terms print in well under a second,
  and 12 terms in 60 s here; from a(13) on the terms pass Python's 4300-digit
  limit for printing integers, which stops the program with a `ValueError`.
  The b-file is the OEIS data (6 terms) and the bar is all of it.
- B_n on the inputs with the other range groups (m = 2/3): trivial
  [A000814](../A000814/)/A000815, S(m)
  [A000829](../A000829/)/[A000830](../A000830/), C(2,m)
  [A000844](../A000844/)/[A000845](../A000845/), S(m) and C(2,m)
  [A000859](../A000859/)/[A000860](../A000860/), GL(m,2)
  [A000874](../A000874/)/[A000875](../A000875/), AG(m,2)
  [A000889](../A000889/)/[A000890](../A000890/). The same range group with
  only complementing inputs: [A000808](../A000808/)/[A000809](../A000809/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 213 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000815), CC BY-SA 4.0.
