# A000872

> Number of switching networks with S(n) acting on the domain and GL(3,2) acting on the range.
> — [OEIS A000872](https://oeis.org/A000872)

Offset 1: 5, 46, 19930, 69945183326, 3929970742021874526325166, …

### Python 3 — 263 bytes

```python
import math
f=lambda r,*L:r<1and(c:=lambda d:sum(2**sum(map(math.gcd,L,[d*t]*n))for t in range(P))//P)and 8**c(1)+(21<<c(1)+c(2))+(56<<c(3))+(42<<(c(2)+c(4))//2)+(48<<(c(7)-c(1))//2)or sum(f(r+~k,*L,~k)for k in range(r))//r
n=P=1
while[print(f(n)//168)]:n+=1;P*=n
```

**What is counted**

- Maps f: {0,1}ⁿ → {0,1}³ up to permuting the n inputs (S(n)) and invertible
  linear maps of the outputs (GL(3,2), order 168). A brute-force Burnside
  count over the explicit groups matches every term.
- Burnside over the pairs (σ, h): σ̂ splits the N = 2ⁿ inputs into cycles,
  and f is fixed when f(σ̂x) = h(f(x)). On a cycle of length L the value at
  one input must be an output fixed by h^L and the others follow, so
  Fix(σ,h) = Π_C Fix(h^|C|) and a(n) = Σ Fix(σ,h) / (n!·|H|).
- Cycles of σ̂: if σ has cycle lengths l₁, l₂, … on the variables, σᵗ fixes
  the F(t) = 2^Σgcd(t,lᵢ) inputs that are constant on every cycle of σᵗ.
  Burnside for ⟨σ⟩ gives the number of cycles of σ̂^d, c_d = Σ_C gcd(d,|C|)
  = (1/P)·Σ_{t<P} F(dt), for any multiple P of the order of σ, such as n!.
- A^L fixes 2^e(L) outputs, e(L) being the dimension of its fixed space. By
  class: the identity, e = 3; 21 involutions, 2 + [2|L]; 56 elements of
  order 3, 1 + 2[3|L]; 42 of order 4, 1 + [2|L] + [4|L]; 48 of order 7,
  3[7|L].
- Summed over the cycles of σ̂, with c_d = Σ_C gcd(d,|C|): the cycles of
  even length number c₂ − c₁, those of length a multiple of 3 (c₃ − c₁)/2,
  of 4 (c₄ − c₂)/2, of 7 (c₇ − c₁)/6. So the exponents are 3c₁, c₁ + c₂, c₃,
  (c₂ + c₄)/2 and (c₇ − c₁)/2, and a(n) = (1/(168·n!))·Σ_σ (8^c₁ +
  21·2^(c₁+c₂) + 56·2^c₃ + 42·2^((c₂+c₄)/2) + 48·2^((c₇−c₁)/2)).

**How it works**

- `f(r,*L)` is the recursion of [A000612](../A000612/): it averages over the
  permutations of the r variables left by choosing the length k+1 of the
  cycle through one of them (probability 1/r each); the lengths are stored
  as `~k` = −(k+1) and `r+~k` = r−k−1 (`gcd` ignores the sign). The main
  loop keeps P = n! with `P*=n`.
- At a leaf, the helper defined there with a walrus (so it sees `L`)
  recomputes c_d = Σ_{t<P} F(dt)/P, F(dt) being
  `2**sum(map(math.gcd,L,[d*t]*n))`.
- `c(d)` is c_d; the leaf writes the five terms with shifts (`21<<c(1)+c(2)`
  is 21·2^(c₁+c₂), as `<<` binds looser than `+`).
- The floors are exact: at every level the average over Sᵣ and H is the
  number of (Sᵣ × H)-orbits that the permutation already chosen maps to
  themselves (de Bruijn's lemma), an integer, so each `//r` divides exactly.

**Notes**

- Exact integer arithmetic, Burnside's lemma and the group facts above, so
  every term is right. The b-file has 6 terms (a(1) to a(6)); they print in
  0.2 s here, and the bar is the whole b-file. In 60 s the program prints 7
  terms (a(7) after 3 s): each new n costs about 2n times the last, since P
  = n! and the recursion has 2ⁿ⁻¹ leaves. From a(13) on the terms have more
  than 4300 digits, past CPython's int-to-str limit.
- The V-list form (as in [A000827](../A000827/), with `c=lambda
  d:sum((V*d)[::d])//P`) is 264 bytes.
- The same input group S(n) with the other range groups (m = 2/3): trivial
  [A000811](../A000811/)/[A000812](../A000812/), S(m)
  [A000826](../A000826/)/[A000827](../A000827/), C(2,m)
  [A000841](../A000841/)/[A000842](../A000842/), S(m) with C(2,m)
  [A000856](../A000856/)/[A000857](../A000857/), GL(m,2)
  [A000871](../A000871/)/A000872, AG(m,2)
  [A000886](../A000886/)/[A000887](../A000887/). Other entries of Harrison's
  table take C(2,n) (as [A000808](../A000808/)), B(n), GL(n,2) or AG(n,2) on
  the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 263 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000872), CC BY-SA 4.0.
