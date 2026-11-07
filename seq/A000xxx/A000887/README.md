# A000887

> Number of switching networks with S(n,2) acting on the domain and AG(3,2) acting on the range where S(n,k) is the symmetric group acting on k variables.
> — [OEIS A000887](https://oeis.org/A000887)

Offset 1: 2, 12, 2828, 8747130342, 491246345257275414284942, …

### Python 3 — 265 bytes

```python
import math
f=lambda r,*L:r<1and(c:=lambda d:sum(2**sum(map(math.gcd,L,[d*t]*n))for t in range(P))//P-1)and 8**c(1)+(21<<c(1)+c(2))+(56<<c(3))+(42<<(c(2)+c(4))//2)+(48<<(c(7)-c(1))//2)or sum(f(r+~k,*L,~k)for k in range(r))//r
n=P=1
while[print(f(n)//168)]:n+=1;P*=n
```

**What is counted**

- Maps f: {0,1}ⁿ → {0,1}³ up to permuting the n inputs (S(n)) and invertible
  affine maps y ↦ Ay ⊕ b of the outputs (AG(3,2), order 1344). The title's
  "S(n,2)" is S(n) on the n inputs. A brute-force Burnside count over the
  explicit groups matches every term.
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
  the image of A − I: 2^rank(A−I) = 2^(3−e(1)) maps per A, e(1) being the
  dimension of A's fixed space. A fixed input adds e(1) to the exponent of
  [A000872](../A000872/)'s term for A and 1 to every c_d, so
  2^rank(A−I)·(term at c) = 8·(term at c − 1). Hence a(n) =
  (1/(1344·n!))·Σ_σ (8^c₁ + 42·2^(c₁+c₂) + 224·2^c₃ + 168·2^((c₂+c₄)/2) +
  384·2^((c₇−c₁)/2)) = (1/(168·n!))·Σ_σ (A000872's leaf with every c_d
  lowered by 1).

**How it works**

- `f(r,*L)` is the recursion of [A000612](../A000612/): it averages over the
  permutations of the r variables left by choosing the length k+1 of the
  cycle through one of them (probability 1/r each); the lengths are stored
  as `~k` = −(k+1) and `r+~k` = r−k−1 (`gcd` ignores the sign). The main
  loop keeps P = n! with `P*=n`.
- At a leaf, the helper defined there with a walrus (so it sees `L`)
  recomputes c_d = Σ_{t<P} F(dt)/P, F(dt) being
  `2**sum(map(math.gcd,L,[d*t]*n))`.
- The program is [A000872](../A000872/)'s with `-1` in `c`.
- The floors are exact: at every level the average over Sᵣ and H is the
  number of (Sᵣ × H)-orbits that the permutation already chosen maps to
  themselves (de Bruijn's lemma), an integer, so each `//r` divides exactly,
  and so do the halved exponents and the division by 8 hidden in the shift
  (|H| = 1344).

**Notes**

- Exact integer arithmetic, Burnside's lemma and the group facts above, so
  every term is right. The b-file has 6 terms (a(1) to a(6)); they print in
  0.3 s here, and the bar is the whole b-file. In 60 s the program prints 7
  terms (a(7) after 4 s): each new n costs about 2n times the last, since P
  = n! and the recursion has 2ⁿ⁻¹ leaves. From a(13) on the terms have more
  than 4300 digits, past CPython's int-to-str limit.
- The same input group S(n) with the other range groups (m = 2/3): trivial
  [A000811](../A000811/)/[A000812](../A000812/), S(m)
  [A000826](../A000826/)/[A000827](../A000827/), C(2,m)
  [A000841](../A000841/)/[A000842](../A000842/), S(m) with C(2,m)
  [A000856](../A000856/)/[A000857](../A000857/), GL(m,2)
  [A000871](../A000871/)/[A000872](../A000872/), AG(m,2)
  [A000886](../A000886/)/A000887. Other entries of Harrison's table take
  C(2,n) (as [A000808](../A000808/)), B(n), GL(n,2) or AG(n,2) on the
  inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 265 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000887), CC BY-SA 4.0.
