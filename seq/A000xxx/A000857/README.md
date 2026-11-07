# A000857

> Number of n-input 3-output switching networks under the action of S(n) on the inputs and S(3) and complementing group C(2,3) on the outputs.
> — [OEIS A000857](https://oeis.org/A000857)

Offset 1: 4, 74, 63440, 244728561176, 13754897546985740953546112, …

### Python 3 — 210 bytes

```python
import math
f=lambda r,V:r and sum(f(r+~k,[V[t]<<math.gcd(t,~k)for t in range(P)])for k in range(r))//r or sum(d**3%5<<d-4+sum(V*(3-d)+V[::d]*d)//P for d in(1,2,3))
n=1;P=6
while[print(f(n,[1]*P)//6)]:n+=1;P*=n
```

**What is counted**

- Maps f: {0,1}ⁿ → {0,1}³ up to permuting the n inputs (S(n)) and, on the
  outputs, permuting and complementing them (S(3) with C(2,3), the 48
  symmetries y ↦ π(y) ⊕ b of the cube). A brute-force Burnside count over
  the explicit groups matches every term.
- Burnside over the pairs (σ, h): σ̂ splits the N = 2ⁿ inputs into cycles,
  and f is fixed when f(σ̂x) = h(f(x)). On a cycle of length L the value at
  one input must be an output fixed by h^L and the others follow, so
  Fix(σ,h) = Π_C Fix(h^|C|) and a(n) = Σ Fix(σ,h) / (n!·|H|).
- Cycles of σ̂: if σ has cycle lengths l₁, l₂, … on the variables, σᵗ fixes
  the F(t) = 2^Σgcd(t,lᵢ) inputs that are constant on every cycle of σᵗ.
  Burnside for ⟨σ⟩ gives the number of cycles of σ̂^d, c_d = Σ_C gcd(d,|C|)
  = (1/P)·Σ_{t<P} F(dt), for any multiple P of the order of σ, such as n!.
- Every σ̂ fixes the all-zero input, so only an h with a fixed output
  counts. h(y) = π(y) ⊕ b has one exactly when b has even weight on every
  cycle of π (2^(3 − cycles of π) choices of b), and then a translation
  conjugates h to π. A d-cycle has 4 − d cycles, so with
  [A000827](../A000827/)'s count for π each class gets a factor 2^(d−1):
  a(n) = (1/(48·n!))·Σ_σ (8^c₁ + 6·2^(c₁+c₂) + 8·2^c₃).

**How it works**

- `f(r,V)` is the recursion of [A000612](../A000612/): it averages over the
  permutations of the r variables left by choosing the length k+1 of the
  cycle through one of them (probability 1/r each). With `k` in `range(r)`,
  `~k` is −(k+1), so `r+~k` = r−k−1 and `math.gcd(t,~k)` = gcd(t,k+1).
- `V` is a list over t < P; a new cycle of length l shifts entry t left by
  gcd(t,l), so at a leaf V[t] = F(t), and the main loop keeps P = 6·n! with
  `P*=n` (starting from P = 6).
- The program is A000827's with `d-4+` in the exponent: the factor 2^(d−1)
  and a division by 8, which leaves `//6` for the end. P = 6·n!, so
  `sum(V*(3-d)+V[::d]*d)//P` is the exponent (3−d)·c₁ + c_d, as there.
- The floors are exact: at every level the average over Sᵣ and H is the
  number of (Sᵣ × H)-orbits that the permutation already chosen maps to
  themselves (de Bruijn's lemma), an integer, so each `//r` divides exactly,
  and so does the division by 8 at the leaves (|H| = 48).

**Notes**

- Exact integer arithmetic, Burnside's lemma and the group facts above, so
  every term is right. The b-file has 6 terms (a(1) to a(6)); they print in
  0.1 s here, and the bar is the whole b-file. In 60 s the program prints 8
  terms (a(8) after 22 s): each new n costs about 2n times the last, since P
  = 6·n! and the recursion has 2ⁿ⁻¹ leaves. From a(13) on the terms have
  more than 4300 digits, past CPython's int-to-str limit.
- The same input group S(n) with the other range groups (m = 2/3): trivial
  [A000811](../A000811/)/[A000812](../A000812/), S(m)
  [A000826](../A000826/)/[A000827](../A000827/), C(2,m)
  [A000841](../A000841/)/[A000842](../A000842/), S(m) with C(2,m)
  [A000856](../A000856/)/A000857, GL(m,2)
  [A000871](../A000871/)/[A000872](../A000872/), AG(m,2)
  [A000886](../A000886/)/[A000887](../A000887/). Other entries of Harrison's
  table take C(2,n) (as [A000808](../A000808/)), B(n), GL(n,2) or AG(n,2) on
  the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 210 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000857), CC BY-SA 4.0.
