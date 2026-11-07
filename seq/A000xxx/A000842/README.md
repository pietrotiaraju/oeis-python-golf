# A000842

> Number of n-input 3-output switching networks under action of symmetric group S(n) on the inputs and complementing group C(3,2) on the outputs.
> — [OEIS A000842](https://oeis.org/A000842)

Offset 1: 8, 288, 366080, 1468180471808, 82529385161696481036468224, …

### Python 3 — 162 bytes

```python
import math
f=lambda r,V:r and sum(f(r+~k,[V[t]<<math.gcd(t,~k)for t in range(P)])for k in range(r))//r or 1<<sum(V)//P-3
n=P=1
while[print(f(n,[3]*P))]:n+=1;P*=n
```

**What is counted**

- Maps f: {0,1}ⁿ → {0,1}³ up to permuting the n inputs (S(n)) and
  complementing outputs, f ↦ f ⊕ b with b ∈ {0,1}³ (the complementing group
  C(2,3)). A brute-force Burnside count over the explicit groups matches
  every term.
- Burnside over the pairs (σ, h): σ̂ splits the N = 2ⁿ inputs into cycles,
  and f is fixed when f(σ̂x) = h(f(x)). On a cycle of length L the value at
  one input must be an output fixed by h^L and the others follow, so
  Fix(σ,h) = Π_C Fix(h^|C|) and a(n) = Σ Fix(σ,h) / (n!·|H|).
- Cycles of σ̂: if σ has cycle lengths l₁, l₂, … on the variables, σᵗ fixes
  the F(t) = 2^Σgcd(t,lᵢ) inputs that are constant on every cycle of σᵗ.
  Burnside for ⟨σ⟩ gives the number of cycles of σ̂^d, c_d = Σ_C gcd(d,|C|)
  = (1/P)·Σ_{t<P} F(dt), for any multiple P of the order of σ, such as n!.
- For b ≠ 0, y ↦ y ⊕ b fixes no output when applied an odd number of times,
  and every σ̂ fixes the all-zero input, a cycle of length 1. So only b = 0
  counts and a(n) = [A000812](../A000812/)(n)/8 = (1/(8·n!))·Σ_σ 8^c₁.

**How it works**

- `f(r,V)` is the recursion of [A000612](../A000612/): it averages over the
  permutations of the r variables left by choosing the length k+1 of the
  cycle through one of them (probability 1/r each). With `k` in `range(r)`,
  `~k` is −(k+1), so `r+~k` = r−k−1 and `math.gcd(t,~k)` = gcd(t,k+1).
- `V` is a list over t < P; a new cycle of length l shifts entry t left by
  gcd(t,l), so at a leaf V[t] = 3·F(t), and the main loop keeps P = n! with
  `P*=n`.
- The program is A000812's with `-3` in the exponent: `V` starts at 3,
  `sum(V)//P` = 3c₁, and `1<<sum(V)//P-3` = 8^c₁/8.
- The floors are exact: at every level the average over Sᵣ and H is the
  number of (Sᵣ × H)-orbits that the permutation already chosen maps to
  themselves (de Bruijn's lemma), an integer, so each `//r` divides exactly,
  and so does the division by 8 at the leaves (|H| = 8).

**Notes**

- Exact integer arithmetic, Burnside's lemma and the group facts above, so
  every term is right. The b-file has 6 terms (a(1) to a(6)); they print in
  0.1 s here, and the bar is the whole b-file. In 60 s the program prints 8
  terms (a(8) after 3 s): each new n costs about 2n times the last, since P
  = n! and the recursion has 2ⁿ⁻¹ leaves. From a(13) on the terms have more
  than 4300 digits, past CPython's int-to-str limit.
- The same input group S(n) with the other range groups (m = 2/3): trivial
  [A000811](../A000811/)/[A000812](../A000812/), S(m)
  [A000826](../A000826/)/[A000827](../A000827/), C(2,m)
  [A000841](../A000841/)/A000842, S(m) with C(2,m)
  [A000856](../A000856/)/[A000857](../A000857/), GL(m,2)
  [A000871](../A000871/)/[A000872](../A000872/), AG(m,2)
  [A000886](../A000886/)/[A000887](../A000887/). Other entries of Harrison's
  table take C(2,n) (as [A000808](../A000808/)), B(n), GL(n,2) or AG(n,2) on
  the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 162 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000842), CC BY-SA 4.0.
