# A001325

> Number of equivalence classes of 3-valued Post functions of n variables under action of semi-direct product of symmetric group S_n and complementing group D(n,3).
> — [OEIS A001325](https://oeis.org/A001325)

Offset 1: 18, 2862, 158942078604, 1154756479802000759397882239648671476, …

a(n) counts the functions f: {0,1,2}ⁿ → {0,1,2} up to permuting the n
variables and complementing any of them, xᵢ ↦ 2 − xᵢ (the complementing
group D(n,3) of Harrison and High, of order 2ⁿ). Only the inputs are
transformed. Together the two give the group Bₙ of signed permutations, of
order 2ⁿ·n!.

### Python 3 — 213 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and 3**(sum(3**sum((g:=gcd(t,l))*(t//g%2*l<1)for l in L)for t in range(m))//m)
n=1
while[print(f(n))]:n+=1
```

**What is counted**

- By Burnside's lemma a(n) = Σ_g 3^c(g) / (2ⁿ·n!), where c(g) is the number
  of cycles of g on the 3ⁿ inputs: a function is fixed by g exactly when it
  is constant on each cycle.
- An element g of Bₙ permutes the coordinates and complements some of them.
  Each cycle of the permutation has a length l and a sign: positive if an
  even number of complements lie along it (going once round the cycle then
  maps a value to itself), negative if odd (going round applies x ↦ 2 − x).
- gᵗ moves every coordinate t steps along its cycle, so it splits a cycle of
  length l into d = gcd(t,l) orbits of l/d coordinates, and going once round
  such an orbit is t/d turns of the cycle. A point fixed by gᵗ is fixed by
  its values on one coordinate per orbit, and each must be left alone by t/d
  turns: any of 3 values on a positive cycle, or when t/d is even; only the
  value 1 when the cycle is negative and t/d is odd. So gᵗ fixes
  Π 3^(d·e) points, with e = 0 for a negative cycle with t/d odd and e = 1
  otherwise.
- The order of g divides m = 2·lcm(lengths), and Burnside's lemma for the
  cyclic group ⟨g⟩ gives c(g) = (1/m) Σ_{t<m} fix(gᵗ).

**How it works**

- This is the program of [A000616](../../A000xxx/A000616/) (the same count
  for two values) with three values. `f(r,*L)` averages over the signed
  permutations of r further coordinates, given the signed cycles `L` chosen
  so far: negative entries are positive cycles and positive entries
  negative ones. The cycle through one chosen coordinate has length k with
  probability 1/r and either sign with probability 1/2, so
  f(r,L) = Σ_{k,±} f(r−k, L+[±k]) / (2r): `k` runs over ±1…±r, `r-abs(k)`
  coordinates are left, and `//r>>1` divides by 2r.
- At r = 0, `(g:=gcd(t,l))*(t//g%2*l<1)` is d·e for one cycle: the
  comparison fails only for l > 0 (a negative cycle) with t/d odd. So
  `3**sum(…)` is fix(gᵗ), and `3**(sum(…)//m)` is 3^c(g).
- The floors are exact. f(r,L) is (1/|H|) Σ_{h∈H} fix(hτ), with H = B_r and
  τ the signed permutation already chosen (fix counting the functions fixed);
  by de Bruijn's lemma (for H normal in G and τ in G this is the number of
  H-orbits that τ maps to themselves) it is an integer.
- Exact integers throughout, so the program is right for every n.

**Notes**

- The (length, order) pairs of [A001327](../A001327/), with `for o in(1,2)`
  in place of the signs, make 232 bytes.
- The recursion visits 2·3^(n−1) signed compositions of n, and the terms
  grow like 3^(3ⁿ)/(2ⁿ·n!). a(1)…a(8) (a(8) has 3124 digits) print in
  0.2 s; a(9) has 9383 digits, and Python's 4300-digit limit for printing
  integers stops the program there.
- The OEIS b-file is synthesized from the entry: 5 terms (n = 1 to 5). The
  bar is the whole b-file in 60 s, which takes 0.1 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 213 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001325), CC BY-SA 4.0.
