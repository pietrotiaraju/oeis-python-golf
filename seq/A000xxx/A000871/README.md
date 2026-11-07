# A000871

> Number of switching networks with S(n) acting on the domain and GL(2,2) acting on the range.
> — [OEIS A000871](https://oeis.org/A000871)

Offset 1: 5, 35, 2266, 30564722, 25624410747226866, …

### Python 3 — 211 bytes

```python
import math
f=lambda r,V:r and sum(f(r+~k,[V[t]<<math.gcd(t,~k)for t in range(P)])for k in range(r))//r or sum(d**3%5<<sum(V[::d]*d,(2-d)*sum(V))//P for d in(1,2,3))
n=1;P=6
while[print(f(n,[1]*P)//6)]:n+=1;P*=n
```

**What is counted**

- Maps f: {0,1}ⁿ → {0,1}² up to permuting the n inputs (S(n)) and invertible
  linear maps of the outputs (GL(2,2), order 6). A brute-force Burnside
  count over the explicit groups matches every term.
- Burnside over the pairs (σ, h): σ̂ splits the N = 2ⁿ inputs into cycles,
  and f is fixed when f(σ̂x) = h(f(x)). On a cycle of length L the value at
  one input must be an output fixed by h^L and the others follow, so
  Fix(σ,h) = Π_C Fix(h^|C|) and a(n) = Σ Fix(σ,h) / (n!·|H|).
- Cycles of σ̂: if σ has cycle lengths l₁, l₂, … on the variables, σᵗ fixes
  the F(t) = 2^Σgcd(t,lᵢ) inputs that are constant on every cycle of σᵗ.
  Burnside for ⟨σ⟩ gives the number of cycles of σ̂^d, c_d = Σ_C gcd(d,|C|)
  = (1/P)·Σ_{t<P} F(dt), for any multiple P of the order of σ, such as n!.
- GL(2,2) fixes 0 and permutes the three nonzero outputs as S(3). A^L fixes
  4 outputs for the identity, 2 or 4 for the 3 transpositions (4 when L is
  even) and 1 or 4 for the two 3-cycles (4 when 3 | L), so Π_C = 4^c₁, 2^c₂
  and 2^(c₃−c₁): c₂ − c₁ cycles of σ̂ have even length and (c₃ − c₁)/2 have
  length a multiple of 3. So a(n) = (1/(6·n!))·Σ_σ (4^c₁ + 3·2^c₂ +
  2·2^(c₃−c₁)).
- With d = 1, 2, 3 for the three classes (sizes 1, 3, 2), the exponent is
  (2−d)·c₁ + c_d: [A000827](../A000827/)'s (3−d)·c₁ + c_d minus c₁.

**How it works**

- `f(r,V)` is the recursion of [A000612](../A000612/): it averages over the
  permutations of the r variables left by choosing the length k+1 of the
  cycle through one of them (probability 1/r each). With `k` in `range(r)`,
  `~k` is −(k+1), so `r+~k` = r−k−1 and `math.gcd(t,~k)` = gcd(t,k+1).
- `V` is a list over t < P; a new cycle of length l shifts entry t left by
  gcd(t,l), so at a leaf V[t] = F(t), and the main loop keeps P = 6·n! with
  `P*=n` (starting from P = 6).
- As d divides P, `V[::d]` makes (P/d)/(order of σ^d) full turns of ⟨σ^d⟩
  and c_d = d·ΣV[::d]/P. The exponent ((2−d)·ΣV + d·ΣV[::d])/P is
  `sum(V[::d]*d,(2-d)*sum(V))//P`: the start value of `sum` carries the
  (2−d)·ΣV part, which is negative for d = 3.
- The class sizes 1, 3, 2 are d³ mod 5.
- The floors are exact: at every level the average over Sᵣ and H is the
  number of (Sᵣ × H)-orbits that the permutation already chosen maps to
  themselves (de Bruijn's lemma), an integer, so each `//r` divides exactly.

**Notes**

- Exact integer arithmetic, Burnside's lemma and the group facts above, so
  every term is right. The b-file has 7 terms (a(1) to a(7)); they print in
  1.0 s here, and the bar is the whole b-file. In 60 s the program prints 8
  terms (a(8) after 19 s): each new n costs about 2n times the last, since P
  = 6·n! and the recursion has 2ⁿ⁻¹ leaves. From a(13) on the terms have
  more than 4300 digits, past CPython's int-to-str limit.
- A000827's list form with a start value, `sum(V*(3-d)+V[::d]*d,-sum(V))`,
  is 3 bytes longer (the first entry).
- The same input group S(n) with the other range groups (m = 2/3): trivial
  [A000811](../A000811/)/[A000812](../A000812/), S(m)
  [A000826](../A000826/)/[A000827](../A000827/), C(2,m)
  [A000841](../A000841/)/[A000842](../A000842/), S(m) with C(2,m)
  [A000856](../A000856/)/[A000857](../A000857/), GL(m,2)
  A000871/[A000872](../A000872/), AG(m,2)
  [A000886](../A000886/)/[A000887](../A000887/). Other entries of Harrison's
  table take C(2,n) (as [A000808](../A000808/)), B(n), GL(n,2) or AG(n,2) on
  the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 214 | first entry |
| 2026-11-07 | Python 3 | 211 | `sum(V[::d]*d,(2-d)*sum(V))` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000871), CC BY-SA 4.0.
