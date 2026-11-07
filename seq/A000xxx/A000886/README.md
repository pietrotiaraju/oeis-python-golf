# A000886

> Number of switching networks with S(n,2) acting on the domain and AG(2,2) acting on the range where S(n,k) is the symmetric group acting on k variables.
> — [OEIS A000886](https://oeis.org/A000886)

Offset 1: 2, 11, 590, 7644658, 6406102803167154, …

### Python 3 — 216 bytes

```python
import math
f=lambda r,*L:r<1and(v:=lambda d:1<<sum(2**sum(map(math.gcd,L,[d*t]*n))for t in range(P))//P)and v(1)**2+6*v(2)+8*v(3)//v(1)or sum(f(r+~k,*L,~k)for k in range(r))//r
n=P=1
while[print(f(n)//24)]:n+=1;P*=n
```

**What is counted**

- Maps f: {0,1}ⁿ → {0,1}² up to permuting the n inputs (S(n)) and invertible
  affine maps y ↦ Ay ⊕ b of the outputs (AG(2,2), order 24, all permutations
  of the 4 outputs). The title's "S(n,2)" is S(n) on the n inputs. A
  brute-force Burnside count over the explicit groups matches every term.
- Burnside over the pairs (σ, h): σ̂ splits the N = 2ⁿ inputs into cycles,
  and f is fixed when f(σ̂x) = h(f(x)). On a cycle of length L the value at
  one input must be an output fixed by h^L and the others follow, so
  Fix(σ,h) = Π_C Fix(h^|C|) and a(n) = Σ Fix(σ,h) / (n!·|H|).
- Cycles of σ̂: if σ has cycle lengths l₁, l₂, … on the variables, σᵗ fixes
  the F(t) = 2^Σgcd(t,lᵢ) inputs that are constant on every cycle of σᵗ.
  Burnside for ⟨σ⟩ gives the number of cycles of σ̂^d, c_d = Σ_C gcd(d,|C|)
  = (1/P)·Σ_{t<P} F(dt), for any multiple P of the order of σ, such as n!.
- Every σ̂ fixes the all-zero input, so only an h with a fixed output
  counts. An affine map y ↦ Ay ⊕ b with a fixed point is conjugate by a
  translation to its linear part A, and it has one exactly when b lies in
  the image of A − I: 2^rank(A−I) maps per A. With [A000871](../A000871/)'s
  count for A ∈ GL(2,2), the classes get factors 1, 2, 4: a(n) =
  (1/(24·n!))·Σ_σ (4^c₁ + 6·2^c₂ + 8·2^(c₃−c₁)).

**How it works**

- `f(r,*L)` is the recursion of [A000612](../A000612/): it averages over the
  permutations of the r variables left by choosing the length k+1 of the
  cycle through one of them (probability 1/r each); the lengths are stored
  as `~k` = −(k+1) and `r+~k` = r−k−1 (`gcd` ignores the sign). The main
  loop keeps P = n! with `P*=n`.
- At a leaf, the helper defined there with a walrus (so it sees `L`)
  recomputes c_d = Σ_{t<P} F(dt)/P, F(dt) being
  `2**sum(map(math.gcd,L,[d*t]*n))`.
- `v(d)` is 2^c_d, so the leaf is `v(1)**2+6*v(2)+8*v(3)//v(1)`; the floor
  is exact since c₃ ≥ c₁.
- The floors are exact: at every level the average over Sᵣ and H is the
  number of (Sᵣ × H)-orbits that the permutation already chosen maps to
  themselves (de Bruijn's lemma), an integer, so each `//r` divides exactly.

**Notes**

- Exact integer arithmetic, Burnside's lemma and the group facts above, so
  every term is right. The b-file has 7 terms (a(1) to a(7)); they print in
  1.6 s here, and the bar is the whole b-file. In 60 s the program prints 8
  terms (a(8) after 30 s): each new n costs about 2n times the last, since P
  = n! and the recursion has 2ⁿ⁻¹ leaves. From a(13) on the terms have more
  than 4300 digits, past CPython's int-to-str limit.
- [A000871](../A000871/)'s program with `d-3+` added to the exponent (each
  class times 2^rank(A−I)/4, then `//6`) is 218 bytes.
- The same input group S(n) with the other range groups (m = 2/3): trivial
  [A000811](../A000811/)/[A000812](../A000812/), S(m)
  [A000826](../A000826/)/[A000827](../A000827/), C(2,m)
  [A000841](../A000841/)/[A000842](../A000842/), S(m) with C(2,m)
  [A000856](../A000856/)/[A000857](../A000857/), GL(m,2)
  [A000871](../A000871/)/[A000872](../A000872/), AG(m,2)
  A000886/[A000887](../A000887/). Other entries of Harrison's table take
  C(2,n) (as [A000808](../A000808/)), B(n), GL(n,2) or AG(n,2) on the
  inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 216 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000886), CC BY-SA 4.0.
