# A001531

> Number of self-dual Boolean functions of n variables that are distinct under complementation/permutation.
> — [OEIS A001531](https://oeis.org/A001531)

Offset 0: 1, 1, 3, 7, 83, 109950, 28613442061634, 32966964611113760521683249750048, …

### Python 3 — 265 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(t:=max(1,*L))and any((t*(l>0)+l)//gcd(t,l)%2for l in L)<<sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(2*lcm(*L)))//lcm(*L)//4
n=1
while[print(f(n))]:n+=1
```

**What is counted**

- A function f is self-dual when f(¬x) = ¬f(x). Two functions are
  equivalent when one becomes the other by permuting and negating inputs:
  the group B_m of 2^m·m! signed permutations g(x) = P·x ⊕ s. Negating the
  output adds nothing: for a self-dual f, ¬f is f with all inputs negated.
- The OEIS data counts self-dual functions of n + 1 variables, so the
  program computes m = n + 1: a(2) = 3 are the classes of x, maj(x,y,z) and
  x ⊕ y ⊕ z, three inputs; with two inputs the only self-dual functions are
  ±x and ±y, one class, and a(0) = 1 is {x, ¬x}. Burnside's lemma below,
  evaluated element by element on the 2^m points for m ≤ 6, gives
  1, 1, 3, 7, 83, 109950, the first six terms. (Self-dual functions of
  n + 1 inputs correspond to all functions of n inputs, f ↦ f(x, 1), which
  is probably where the shift comes from.)
- Every g in B_m commutes with complementing all points, c(x) = ¬x, so
  B_m maps self-dual functions to self-dual functions, and by Burnside's
  lemma a(n) = (1/|B_m|) Σ_g s(g), where s(g) counts the self-dual f with
  f∘g = f.

**Fixed self-dual functions**

- Such an f is constant on every cycle of g on the 2^m points, and c maps
  cycles to cycles. If c maps a cycle to itself, f would have to take both
  values on it: s(g) = 0. Otherwise c pairs the cycles, f is free on one
  cycle of each pair and determined on the other: s(g) = 2^(P/2), with P
  the number of cycles of g.
- c maps the cycle of x to itself when c·gᵗ fixes x for some t. On the
  coordinates of a cycle of g of length l with an odd (negative cycle) or
  even (positive) number of negations, gᵗ is gcd(t,l) cycles of length
  l/gcd(t,l), each traversing the old one t/gcd(t,l) times, and c adds one
  negation per step. A signed permutation fixes a pattern exactly when all
  its cycles are positive, so c·gᵗ fixes points of that block exactly when
  (t·[negative] + l)/gcd(t,l) is even. In terms of 2-adic valuations: a
  positive cycle needs v₂(t) < v₂(l), a negative one v₂(t) = v₂(l).
- So some t works for every cycle at once exactly when all negative cycles
  have the same v₂(l) = a and all positive ones have v₂(l) > a (any a ≥ 0
  when there is no negative cycle), and then t = the longest negative cycle,
  or t = 1 when there is none, works too.

**How it works**

- `f(r,*L)` is the signed-cycle-type recursion of [A000370](../A000370/)
  with the weight s(g) at the leaves: the cycle through one chosen
  coordinate has length k and either sign with probability 1/(2r) each,
  `k` > 0 standing for a negative cycle and `k` < 0 for a positive one, and
  `//r>>1` divides by 2r. The floors are exact by de Bruijn's lemma (see
  that page) with the set of self-dual functions in place of all functions.
- At the leaf, `t:=max(1,*L)` is the test value above and
  `any((t*(l>0)+l)//gcd(t,l)%2for l in L)` is 1 when it fails for some
  cycle, so no cycle is mapped to itself.
- `sum(prod(…)for t in range(2*lcm(*L)))` adds the fixed points of gᵗ over a
  multiple of the order of g, as on the A000370 page, so dividing by
  `lcm(*L)` and then by 4 gives P/2.
- f(r,L) is never 0 for r ≥ 1: leaving the r coordinates alone gives r
  positive cycles of length 1, which would need v₂(t) < v₂(1) = 0, so no
  cycle is mapped to itself and that weight is positive. So `r and … or …`
  never falls through to the leaf early.

**Notes**

- Exact integer arithmetic, so the program is right for every n. All 9
  b-file terms (n = 0 to 8) come out in under a second; the bar is the whole
  b-file in 60 s.
- a(14) has more than 4300 digits, Python's int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 265 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001531), CC BY-SA 4.0.
