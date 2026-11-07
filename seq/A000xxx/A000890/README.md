# A000890

> Number of switching networks with S(n) and C(2,2) acting on the domain and AG(2,3) acting on the range.
> — [OEIS A000890](https://oeis.org/A000890)

Offset 1: 2, 8, 502, 547849868, 15351457458188948591044, …

### Python 3 — 317 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(42<<(a:=(d:=lambda j,m=2*lcm(*L):sum(R:=[prod((t*j//(g:=gcd(t*j,l))%2*l<1)<<g for l in L)for t in range(m)])//m+(0in R))(1))+d(2))+8**a+224*2**d(3)+384*2**(d(7)-a>>1)+(168<<(d(2)-~d(4)>>1))
n=1
while[print(f(n)//1344)]:n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}³ (n inputs, 3 outputs) up to f ↦ h∘f∘g, where g runs
  over the 2ⁿ·n! maps that permute and complement the inputs (the
  hyperoctahedral group B_n) and h over AG(3,2), the 1344 affine maps y ↦ Ay ⊕
  b of the outputs. The OEIS name gives the groups (its "S(n) and C(2,2)" on
  the domain means permuting and complementing the inputs; brute force
  confirms). A brute-force Burnside over all pairs (g, h) matches the data for
  n ≤ 4.
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
- e_j = 1 when g^j has no fixed point. If g^j fixes x, so does every power of
  it, so e_j = 1 exactly when some fix(g^(jt)) is 0. In B_n an odd cycle
  forces a fixed point (A000157), so e_j = e_1 for odd j. Write D_j =
  2^(c_j+e_j) = C_j·(1+e_j): the Boolean functions φ with φ∘g^j = φ or φ∘g^j =
  ¬φ (the second kind needs every cycle of g^j to be even).

**The weight**

- Group the 8 maps with the same linear part A (the classes of
  [A000875](../A000875/)). A brute-force table of their cycle types on the 8
  outputs gives, per A, the sum over the 8 translations b: the identity: D₁³;
  each of the 21 involutions: 2·D₁D₂; each of the 56 of order 3: 4·D₃; each of
  the 42 of order 4: 4·2^((c₂+c₄)/2+e₂); each of the 48 of order 7:
  8·2^((c₇−c₁)/2).
- In exponents d_j = c_j + e_j: d₇ − d₁ = c₇ − c₁, and (c₂+c₄)/2 + e₂ =
  ⌈(d₂+d₄)/2⌉ because c₂ + c₄ is even and e₄ ≤ e₂. So W(g) = 8^d₁ +
  42·2^(d₁+d₂) + 224·2^d₃ + 384·2^((d₇−d₁)/2) + 168·2^⌈(d₂+d₄)/2⌉.

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
- At r = 0, the lambda `d(j)` is d_j: `R` lists fix(g^(tj)) for t < m,
  `sum(R)//m` is c_j and `0in R` is e_j. `a` keeps d₁; `168<<(d(2)-~d(4)>>1)`
  is the ceiling term. Exponents with shifts are 3 bytes shorter here than the
  powers D_j with `isqrt` (and a bit-length trick for the ceiling).
- `f(n)` is Σ_g W(g)/|B_n|, so `f(n)//1344` is a(n), with |H| = 1344.

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
  [A000874](../A000874/)/[A000875](../A000875/), AG(m,2)
  [A000889](../A000889/)/A000890. The same range group with only complementing
  inputs: [A000883](../A000883/)/[A000884](../A000884/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 317 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000890), CC BY-SA 4.0.
