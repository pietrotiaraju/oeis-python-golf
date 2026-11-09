# A001282

> One-half of the number of permutations p of [n] having exactly three runs of adjacent entries differing by 1.
> — [OEIS A001282](https://oeis.org/A001282)

Offset 6: 17, 259, 2770, 27978, 294602, 3331790, 40682144, 535206440, 7557750635, …

A run here is a maximal stretch of neighbouring entries in which each step
is ±1, such as 3 4 5 or 7 6 inside 2 7 6 1 3 4 5. a(n) counts the
permutations of 1, …, n with exactly three runs, halved: reversing a
permutation keeps its runs, and no permutation with n ≥ 2 is its own
reversal. Two runs is [A000544](../../A000xxx/A000544/), whose method this
follows.

### Python 3 — 204 bytes

```python
from math import*
A=[3,-1,-1,1,1,0,0,2,14];C=[0]*9;q=r=0;k=3
while 1:A+=sumprod(A[-4:],(k,2-k,~k,k+4)),;q=sumprod(A[-10:],(3,-15,24,-24,27,9,-36,32,-14,2))-q;t=r=q-r;C=[t:=t+c for c in C];print(t//3);k+=1
```

**How it works**

- **Counting by runs.** Mark a set X of the pairs of neighbours that
  differ by 1 and glue them: each glued block is a stretch of consecutive
  values in increasing or decreasing order. Give a block of s values the
  weight g(s) (g(1) = 1), so a pair (π, X) is an ordering of blocks and
  Σ_X weight = Πᵣ h(|r|) over the runs r of π, where h(L) is the sum of
  g over the ways to cut L into blocks. Choosing g so that h(L) = u for
  every L ≥ 2 gives Σ_π u^runs(π) xⁿ = H(Q), with H(y) = Σₖ k!·yᵏ and
  Q = (x + (u−1)(2x² − x³))/(1 + (u−1)x²), Jovovic's generating function
  in [A010030](https://oeis.org/A010030).
- **Three runs.** At u = 0, Q = z = x(1−x)/(1+x), and
  Q − z = 2uρ/((1+x)(1+uρ)) with ρ = x²/(1−x²). Taylor's formula then
  gives the coefficient of u³ as
  ρ³·(2H′(z)/(1+x) − 4H″(z)/(1+x)² + (4/3)H‴(z)/(1+x)³), which is
  Manyama's formula in the entry after re-indexing.
- **One base sequence.** From (k+1)! = (k+1)·k!, y²H′ = (1−y)H − 1, so
  every derivative of H is a rational function times H plus a rational
  function. With A(x) = H(z), the generating function of Hertzsprung's
  numbers [A002464](https://oeis.org/A002464) (1, 1, 0, 0, 2, 14, …),
  this works out (exact rational algebra, checked with sympy) to

  **3(1−x)⁹(1+x)²·a(x) = W(x)·A(x) − V(x),**

  W = 2 − 14x + 32x² − 36x³ + 9x⁴ + 27x⁵ − 24x⁶ + 24x⁷ − 15x⁸ + 3x⁹,
  V = 2 − 12x + 18x² − 4x³ − 23x⁴ + 36x⁵ − 12x⁷ + 3x⁸.
- **The code.** `A` grows by the recurrence
  A(n) = (n+1)A(n−1) − (n−2)A(n−2) − (n−5)A(n−3) + (n−3)A(n−4) (n ≥ 4,
  proved on [A001266](../A001266/)) with k = n − 3, as on A000544. Then
  `q` = (W·A)/(1+x) and `r` = q/(1+x), one step each (`q=t-q`), the nine
  running sums in `C` divide by (1−x)⁹, and `t//3` is a(n).
- **Starting at n = 6.** Since a(n) = 0 for n < 6, W·A − V and all the
  quotients vanish below x⁶, so the loop starts at n = 6 with every
  accumulator 0. V reaches x⁸ only; the three fake entries in front of
  A(0), 3, −1, −1, make the window add exactly −V₆, −V₇, −V₈ = 0, 12, −3
  (for n = 8: 3·(−1); n = 7: −15·(−1) + 3·(−1); n = 6: 24·(−1) −
  15·(−1) + 3·3) and nothing later.

**Notes**

- Exact integer arithmetic; the generating function rests on the cluster
  argument above and exact algebra. A count of all permutations agrees
  for n ≤ 10.
- One sumprod over `A[-10:]+F[-11:]` with the 21 weights of W and
  3(1−x)⁹(1+x)², as on A000544, is 219 bytes. Expanding the formula into
  a triple sum of binomials,
  a(n) = Σₗ Σₖ Σᵢ (−1)^(n−k−1)·k!·C(k,l)·w_l·C(k+2+i,i)·C(2k−l, n−k+l−6−2i)
  with w = 1, 4, 4 for l = 1, 2, 3, is 185 bytes but needs about n² steps
  per term: some 300 terms in 60 s.
- The b-file has 445 terms (a(6) to a(450)); the bar is all of them in
  60 s, and they print in a tenth of a second. a(1559) is the first term
  with more than 4300 digits (Python's int-to-str limit), so the program
  stops with a `ValueError` after a(1558).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 204 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001282), CC BY-SA 4.0.
