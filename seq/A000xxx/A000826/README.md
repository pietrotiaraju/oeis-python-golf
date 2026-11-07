# A000826

> Number of switching networks (see Harrison reference for precise definition).
> — [OEIS A000826](https://oeis.org/A000826)

Offset 1: 10, 88, 6616, 91666432, 76873231310808704, …

### Python 3 — 187 bytes

```python
import math
f=lambda r,V:r and sum(f(r+~k,[V[t]<<math.gcd(t,~k)for t in range(P)])for k in range(r))//r or sum(1<<sum(V[::d])//P-1for d in(1,2))
n=1;P=2
while[print(f(n,[2]*P))]:n+=1;P*=n
```

**What is counted**

- Maps f: {0,1}ⁿ → {0,1}² up to permuting the n inputs (S(n)) and swapping
  the two outputs (S(2)), as Sean A. Irvine's comment on the entry says. A
  brute-force Burnside count over the explicit groups matches every term.
- Burnside over the pairs (σ, h): σ̂ splits the N = 2ⁿ inputs into cycles,
  and f is fixed when f(σ̂x) = h(f(x)). On a cycle of length L the value at
  one input must be an output fixed by h^L and the others follow, so
  Fix(σ,h) = Π_C Fix(h^|C|) and a(n) = Σ Fix(σ,h) / (n!·|H|).
- Cycles of σ̂: if σ has cycle lengths l₁, l₂, … on the variables, σᵗ fixes
  the F(t) = 2^Σgcd(t,lᵢ) inputs that are constant on every cycle of σᵗ.
  Burnside for ⟨σ⟩ gives the number of cycles of σ̂^d, c_d = Σ_C gcd(d,|C|)
  = (1/P)·Σ_{t<P} F(dt), for any multiple P of the order of σ, such as n!.
- A permutation π of the output bits fixes 2^(cycles of π^L) outputs under
  π^L, so Π_C Fix(π^|C|) = 2^Σ_b c_b over the cycle lengths b of π: the
  number of cycles of (σ, π) on inputs × output bits. The swap gives 2^c₂,
  so a(n) = (1/(2·n!))·Σ_σ (4^c₁ + 2^c₂).

**How it works**

- `f(r,V)` is the recursion of [A000612](../A000612/): it averages over the
  permutations of the r variables left by choosing the length k+1 of the
  cycle through one of them (probability 1/r each). With `k` in `range(r)`,
  `~k` is −(k+1), so `r+~k` = r−k−1 and `math.gcd(t,~k)` = gcd(t,k+1).
- `V` is a list over t < P; a new cycle of length l shifts entry t left by
  gcd(t,l), so at a leaf V[t] = 2·F(t), and the main loop keeps P = 2·n!
  with `P*=n` (starting from P = 2).
- For d = 1, 2, `V[::d]` holds 2F(0), 2F(d), …: that is (P/d)/(order of σ^d)
  full turns of ⟨σ^d⟩, so `sum(V[::d])` = 2·(P/d)·c_d and `sum(V[::d])//P` =
  2c₁ for d = 1 and c₂ for d = 2: both exponents with one expression. `-1`
  halves each term, which gives the division by |H| = 2.
- The floors are exact: at every level the average over Sᵣ and H is the
  number of (Sᵣ × H)-orbits that the permutation already chosen maps to
  themselves (de Bruijn's lemma), an integer, so each `//r` divides exactly,
  and so does the halving at the leaves (|H| = 2).

**Notes**

- Exact integer arithmetic, Burnside's lemma and the group facts above, so
  every term is right. The b-file has 8 terms (a(1) to a(8)); they print in
  6.1 s here, and the bar is the whole b-file. The next term needs more than
  60 s: each new n costs about 2n times the last, since P = 2·n! and the
  recursion has 2ⁿ⁻¹ leaves. From a(13) on the terms have more than 4300
  digits, past CPython's int-to-str limit.
- The same input group S(n) with the other range groups (m = 2/3): trivial
  [A000811](../A000811/)/[A000812](../A000812/), S(m)
  A000826/[A000827](../A000827/), C(2,m)
  [A000841](../A000841/)/[A000842](../A000842/), S(m) with C(2,m)
  [A000856](../A000856/)/[A000857](../A000857/), GL(m,2)
  [A000871](../A000871/)/[A000872](../A000872/), AG(m,2)
  [A000886](../A000886/)/[A000887](../A000887/). Other entries of Harrison's
  table take C(2,n) (as [A000808](../A000808/)), B(n), GL(n,2) or AG(n,2) on
  the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 187 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000826), CC BY-SA 4.0.
