# A000889

> Number of switching networks with S(n) and C(2,2) acting on the domain and AG(2,2) acting on the range.
> — [OEIS A000889](https://oeis.org/A000889)

Offset 1: 2, 7, 124, 494298, 200221917406630, …

### Python 3 — 266 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(D:=lambda j,m=2*lcm(*L):1<<sum(R:=[prod((t*j//(g:=gcd(t*j,l))%2*l<1)<<g for l in L)for t in range(m)])//m+(0in R))(1)**2+6*D(2)+8*D(3)//D(1)
n=1
while[print(f(n)//24)]:n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}² (n inputs, 2 outputs) up to f ↦ h∘f∘g, where g runs
  over the 2ⁿ·n! maps that permute and complement the inputs (the
  hyperoctahedral group B_n) and h over AG(2,2), the 24 affine maps of the
  outputs (all permutations of the 4 outputs). The OEIS name gives the groups
  (its "S(n) and C(2,2)" on the domain means permuting and complementing the
  inputs; brute force confirms). A brute-force Burnside over all pairs (g, h)
  matches the data for n ≤ 4.
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

- By cycle type on the 4 outputs: the identity and the 3 translations (two
  2-cycles: a cycle of g takes 4 values if its length is even, none if odd)
  give 4^c₁·(1 + 3e₁) = D₁². A transposition gives 2^c₂ (as the swap in
  [A000829](../A000829/)); a 4-cycle gives 4^c₁ when every cycle of g has
  length divisible by 4 (e₂ = 1, and then 4^c₁ = 2^c₂) and 0 otherwise; the 6
  of each give 6·C₂·(1+e₂) = 6D₂. The 8 3-cycles give 4^N₃ = 2^(c₃−c₁) each,
  as in [A000874](../A000874/).
- So W(g) = D₁² + 6D₂ + 8D₃/D₁, using e₃ = e₁.

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
- At r = 0, the lambda `D(j)` is D_j: `R` lists fix(g^(tj)) for t < m,
  `sum(R)//m` is c_j and `0in R` is e_j; `D(3)//D(1)` is exact.
- `f(n)` is Σ_g W(g)/|B_n|, so `f(n)//24` is a(n), with |H| = 24.

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
  A000889/[A000890](../A000890/). The same range group with only complementing
  inputs: [A000883](../A000883/)/[A000884](../A000884/).

## First three terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(3) have to arrive in time.

### Python 3, 3 terms — 223 bytes

```python
from itertools import*
n=1
while 1:R=range(2**n);print(len({min(tuple(map((g:=[f[s^sum((x>>i&1)<<p[i]for i in p)]for x in R]).index,g))for p in permutations(R[:n])for s in R)for f in product((0,),*[range(4)]*~-2**n)}));n+=1
```

**How it works**

- A map f: {0,1}ⁿ → {0,1}² is the tuple of its 2ⁿ values in 0…3. AG(2,2)
  is every permutation of the four outputs, so a(n) counts the maps up to
  any relabelling of the values and B_n on the inputs.
- For a permutation p of the coordinates and a mask s,
  `s^sum((x>>i&1)<<p[i]for i in p)` is β(x) = s ⊕ σ̂(x), where σ̂ moves bit i
  of x to position p[i]. `for i in p` visits every index once, only in
  another order, and `R[:n]` is range(n) because n < 2ⁿ. Over all p and s
  these are the 2ⁿ·n! elements of B_n, and g is the list of f∘β.
- `tuple(map(g.index,g))` replaces every value by the position where it
  first occurs. It is the same for g and h∘g whatever the relabelling h, and
  two lists with the same pattern differ by a relabelling, so it is a
  canonical form of g up to the outputs' group.
- The minimum of that form over β ∈ B_n is therefore the same for every map
  in the class of f, and two maps with the same minimum are in the same
  class. So the set of minima has one element per class.
- `product((0,),*[range(4)]*~-2**n)` only starts from maps with f(0) = 0
  (a fixed 0, then 2ⁿ − 1 free values). Every class has one, by relabelling
  the outputs, so the set still meets every class: its size is a(n).
- Nothing is approximated; the count is exact for every n.

**Limits**

- a(3) = 124 takes 4⁷ = 16 384 maps × 48 elements of B_3: the three terms
  come in about 6 reference seconds.
- a(4) would take 4¹⁵ ≈ 1.1·10⁹ maps × 384 elements. The main record never
  lists maps: Burnside's lemma over B_n × AG(2,2), with the cycle counts of
  each group element, gives all seven b-file terms at once.
- 223 bytes is an upper bound on the shortest valid three-term program, not
  a proof of minimality.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 266 | first entry |

**Python 3, 3 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 223 | first entry: first-occurrence pattern minimised over B_n, from the maps with f(0) = 0 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000889), CC BY-SA 4.0.
