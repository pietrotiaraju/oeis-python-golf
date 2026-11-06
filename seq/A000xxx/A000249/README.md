# A000249

> Nearest integer to modified Bessel function K_n(5).
> — [OEIS A000249](https://oeis.org/A000249)

Offset 0: 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 10, 42, 193, 966, 5215, 30170, …

### Python 3 — 239 bytes

```python
from fractions import*
def f(e):
 A=C=t=Fraction(e);p=q=0*t
 for k in range(~m-n,0):t=10+(-k|1)*5/t;A=5+A*25/4/k/k;C=5+(C/k-2)*25/4/k;p,q=q,p-2*k*q/5+(k==-n)
 return round((p+q+q/t)/(C+A/t))
n=0;m=24
while 1:n+=f(1)==f(m)!=print(f(1));m+=2
```

**How it works**

- At x = 5 there is no shortcut like the vanishing logarithm at x = 2
  ([A000167](../A000167/)), so the program brackets K_n(5) between two
  exact rationals. When both round to the same integer, it prints that
  integer. When they don't, it tightens the bracket (`m+=2`) and tries again.
- **Ratio K_1/K_0.** With w = 1/(2x) = 1/10, Gauss's continued fraction for
  ₂F₀ gives K_1(5)/K_0(5) = 1 + w/R, where R = 1 + c_1/(1 + c_2/(1 + …)) and
  c_j = (j|1)/20 (1, 3, 3, 5, 5, 7, … over 20). Every tail t_j of R is a
  ratio of Tricomi functions U(a, b, 10) with a > 0. Those are positive
  (integral representation, DLMF 13.4.4), so t_j = 1 + c_j/t_{j+1} lies in
  [1, 1 + c_j]. In the code, `t` is T = 10t, which runs
  T ← 10 + 5(j|1)/T for j = d, …, 1, with d = m+n+1 steps (k = −j). The
  true start value lies in [10, 10 + ((d+1)|1)/2], so start values 1 and m
  sit on either side of it, since m ≥ 24+2n ≥ n+23. Each step is
  decreasing in T, so the final T is monotone in the start value, with
  direction (−1)^d.
- **Normalisation.** The Wronskian I_0K_1 + I_1K_0 = 1/x (DLMF 10.28.2)
  gives K_0 = 2/Den with Den = wI_0 + 10I_1, where w = 10K_1/K_0 = 10 + 10/T.
  The I-series are Horner loops in the same loop as T, with z = x²/4 = 25/4.
  `A` = 5·Σ z^i/(i!)² = 5I_0 and `C` = Σ z^i/(i!)²·(5 + 12.5/(i+1))
  = 5I_0 + 5I_1, so Den/2 = C + A/T. A start value s adds s·z^d/(d!)² in
  place of the true tail. Since d ≥ 25, that tail lies between 5 and
  5.6 times z^d/(d!)², so start 1 gives too small a Den and start m ≥ 24
  too large a one.
- **Recurrence.** K_{k+1} = (2k/5)K_k + K_{k−1} holds for y_k = K_k·Den
  with y_0 = 2 and y_1 = w/5. The coefficients of y_n in (y_0, y_1) build
  up in the same descending loop as a row vector:
  (p, q) ← (q, p + (2j/5)q), with a 1 injected at j = n. This gives
  y_n/2 = p + q·w/10 = p + q + q/T, and the result is (y_n/2)/(Den/2).
- **Why the corners pair up.** Every solution of the recurrence is
  αK_k + β(−1)^kI_k. With the starts above, α = Den, and the value computed
  with exact I's is K_n + τ(−1)^nI_n with τ = K_0(w* − w)/(wI_0 + 10I_1).
  Here w* is the true w, and τ is decreasing in w, so the value is monotone
  in w with direction (−1)^(n+1). Since m is even, d = m+n+1 has the parity
  of n+1, and the value is a decreasing function of the start value for
  every n. Start 1 (small T, small I-tails) is therefore an upper bound and
  start m a lower bound. Truncating Den only moves each bound outward.
- n = 0: the injection `k==-n` never fires, so both corners are exactly 0.
  That is the right term, because K_0(5) ≈ 0.0037.
- Golf notes:
  - `A=C=t` share the start value.
  - `0*t` makes the Fractions for p and q, and `(-k|1)*5/t` keeps the
    division exact.
  - `n+=f(1)==f(m)!=print(f(1))` prints only when the corners agree,
    because chained comparisons short-circuit.

**Notes**

- Exact rational arithmetic. Every printed term is certified by the bracket
  above. Both corners were also checked against mpmath for every n ≤ 94
  and for sampled n up to 400, at a precision finer than the bracket. The
  bracket is far tighter than rounding needs: its relative width is about
  10^(−3.4n) on the first try.
- For each n, the loop ends unless K_n(5) is exactly a half-integer. That
  would need K_n(5) to be rational. Nobody expects it to be, but I know of
  no proof. None of the first 318 terms needed a second try.
- It gets 393 terms in 60 s locally (each try re-runs the loops from
  scratch), and the bar is 300. Terms pass the 4300-digit int-to-str limit
  of Python 3.11+ only from n = 1780 on, far beyond what fits in the time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 239 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000249), CC BY-SA 4.0.
