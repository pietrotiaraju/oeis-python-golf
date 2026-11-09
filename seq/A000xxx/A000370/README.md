# A000370

> Number of NPN-equivalence classes of Boolean functions of n or fewer variables.
> — [OEIS A000370](https://oeis.org/A000370)

Offset 0: 1, 2, 4, 14, 222, 616126, 200253952527184, 263735716028826576482466871188128, …

### Python 3 — 226 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and 1<<sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(m))//m+(sum(L)>-n)
n=0
while[print(f(n)//2)]:n+=1
```

**What is counted**

- Two functions {0,1}ⁿ → {0,1} are NPN-equivalent when one becomes the other
  by permuting the inputs, negating some inputs and possibly negating the
  output. A function of fewer than n variables is a function of n variables
  that ignores some of them, so "n or fewer" changes nothing: a(n) is the
  number of orbits of B_n × Z₂ on the 2^(2ⁿ) functions of n variables.
- Permuting and negating inputs is the group B_n of 2ⁿ·n! maps
  g(x) = P·x ⊕ s on the 2ⁿ points (P a permutation of the coordinates, s a
  mask). By Burnside's lemma,
  a(n) = Σ_g (fix(g) + fix(g·¬)) / (2·|B_n|).
- A function is fixed by g when it is constant on each cycle of g on the
  points, so fix(g) = 2^c(g), with c(g) the number of cycles. It is fixed by
  g·¬ when it alternates along every cycle, which needs every cycle to have
  even length; then there are again 2^c(g) such functions.
- So a(n) = Σ_g 2^c(g)·(2 if all cycles of g are even, else 1) / (2·|B_n|).
  This is twice [A000157](../A000157/), whose program is the same sum
  divided by 4·|B_n|.

**Odd cycle ⟺ fixed point**

The weight (2 or 1) only needs to know whether g has a fixed point. For g
in B_n, some cycle has odd length exactly when g has a fixed point. A fixed
point is a cycle of length 1. Conversely, if x lies on a cycle of odd length L, let
u = x ⊕ g(x) ⊕ … ⊕ g^(L−1)(x). An affine map over GF(2) commutes with sums of
an odd number of terms, so g(u) = g(x) ⊕ … ⊕ g^L(x) = u, and u is a fixed
point.

**Signed cycle types**

- An element of B_n is a signed permutation of the coordinates: each cycle
  has a length l and a sign, the parity of the negations along it. A
  positive cycle fixes 2 patterns of its coordinates and a negative one
  none, so g has a fixed point exactly when all its cycles are positive.
- gᵗ splits a cycle of length l into gcd(t,l) cycles, each with sign
  (−1)^(t/gcd(t,l)) if the cycle was negative. So gᵗ fixes Π 2^gcd(t,l)
  points, with the factor of a negative cycle 0 when t/gcd(t,l) is odd. The
  order of g divides m = 2·lcm(lengths), and Burnside's lemma for ⟨g⟩ gives
  c(g) = (1/m) Σ_{t<m} fix(gᵗ).

**How it works**

- `f(r,*L)` averages the weight 2^c(g)·(2 or 1) over the signed permutations
  of r further coordinates, given the signed cycles `L` chosen so far
  (positive cycles as negative numbers, negative cycles as positive ones).
  The cycle through one chosen coordinate has length k with probability 1/r
  and either sign with probability 1/2, so f(r,L) = Σ_{k,±} f(r−k, L+[±k]) /
  (2r): `k` runs over ±1…±r, `r-abs(k)` coordinates are left, and `//r>>1`
  divides by 2r. There is no |B_n| anywhere.
- At r = 0, `prod(…)` is fix(gᵗ): `(t//g%2*l<1)<<g` is 2^gcd(t,l) unless l > 0
  (a negative cycle) and t/gcd(t,l) is odd. The lengths add up to −n exactly
  when every cycle is positive, so `sum(L)>-n` is 1 when g has no fixed
  point, and the leaf `1<<c+(sum(L)>-n)` is 2^c(g)·(2 or 1).
- The floors are exact. With H = B_r and τ the signed permutation already
  chosen, f(r,L) = (1/|H|) Σ_{h∈H} (fix(hτ) + fix(hτ·¬)). By de Bruijn's
  lemma (for H normal in G and σ in G, (1/|H|) Σ_{h∈H} fix(hσ) is the number
  of H-orbits that σ maps to themselves) both halves are integers.
- `f(n)` is Σ_g 2^c(g)·(2 or 1) / |B_n|, so `f(n)//2` is a(n).

**Notes**

- The recursion visits 2·3^(n−1) signed compositions of n instead of the
  2ⁿ·n! group elements: all 12 b-file terms (n = 0 to 11)
  take about 7 s here. The bar stays at 7 terms in 60 s.
- It is the recursion of [A000616](../A000616/) (NP classes) and
  [A000610](../A000610/) (self-complementary classes) with both weights at
  once; this sequence is their average.
- Terms past n = 13 exceed Python's 4300-digit limit for printing integers,
  long after the timeout.

## First four terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(3) have to arrive in time.

### Python 3, 4 terms — 209 bytes

```python
from itertools import*
n=0
while 1:R=range(2**n);print(len({min(sum((f>>(s^sum((x>>i&1)<<p[i]for i in p))&1^k)<<x for x in R)for p in permutations(R[:n])for s in R for k in(0,1))for f in range(2**2**n)}));n+=1
```

**How it works**

- A function f of n variables is its truth table read as an integer, bit x
  holding f(x), and `range(2**2**n)` runs over all 2^(2ⁿ) of them. As in the
  main record, "n or fewer variables" changes nothing.
- For a permutation p of the coordinates and a mask s,
  `s^sum((x>>i&1)<<p[i]for i in p)` is g(x) = s ⊕ σ̂(x), where σ̂ moves bit i
  of x to position p[i]. `for i in p` visits every index once, only in
  another order, and `R[:n]` is range(n) because n < 2ⁿ. Over all p and s
  these are the 2ⁿ·n! elements of B_n.
- `sum((f>>g(x)&1^k)<<x for x in R)` is the truth table of x ↦ f(g(x)) ⊕ k.
  As (g, k) runs over B_n × Z₂, a group, the generator yields exactly the
  NPN class of f (with repetitions).
- Its minimum is the same for every function in the class, and different
  classes are disjoint, so the set of minima has one element per class: its
  size is a(n). At n = 0 the empty permutation gives g(0) = 0 and k swaps
  the two constants, so a(0) = 1.
- Every step is exact integer work, for every n; only the time grows.

**Limits**

- a(3) = 14 takes 256 functions × 96 transforms of 8 points: the four terms
  come in about 0.2 reference seconds.
- a(4) would take 65 536 functions × 768 transforms of 16 points, about half
  an hour here, and a(5) would loop over 2³² functions. The main record never
  lists functions: it sums 2^c(g) over signed cycle types.
- 209 bytes is an upper bound on the shortest valid four-term program, not a
  proof of minimality.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-06 | 235 | first entry |
| 2026-11-07 | 226 | signed cycle-type recursion with //(2r) at every level |

**Python 3, 4 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 209 | first entry: smallest truth table of each NPN class, over all functions |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000370), CC BY-SA 4.0.
