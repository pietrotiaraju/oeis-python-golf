# A000544

> One-half of the number of permutations p of [n] having exactly two runs of adjacent entries differing by 1.
> — [OEIS A000544](https://oeis.org/A000544)

Offset 4: 3, 25, 155, 1005, 7488, 64164, 619986, 6646750, 78161249, 999473835, …

A run here is a maximal stretch of neighbouring entries in which each step
is ±1, such as 3 4 5 or 7 6 inside 2 7 6 1 3 4 5. a(n) counts the
permutations of 1, …, n with exactly two runs, halved: reversing a
permutation keeps its runs, and no permutation with n ≥ 2 is its own
reversal.

### Python 3 — 165 bytes

```python
from math import*
A=[-1,1,1,0,0];F=[0]*7;k=1
while 1:A+=sumprod(A[-4:],(k,2-k,~k,k+4)),;print(f:=sumprod(A[-6:]+F[-7:],(-1,3,-3,5,-3,1,-1,5,-9,5,5,-9,5)));F+=f,;k+=1
```

**How it works**

- **The entry's generating function.** With y = x(1 − x)/(1 + x), the
  entry gives
  Σₙ a(n)xⁿ = x²·Σₖ k·k!·(x² − x + k − 1)·yᵏ / ((1 − x²)²(1 − x)²).
- **Hertzsprung's numbers.** Put H(y) = Σₖ k!·yᵏ. Since
  (k+1)! = (k+1)·k!, H − 1 = y·(yH′ + H), that is
  y²H′ + (y − 1)H + 1 = 0. So Σ k·k!·yᵏ = yH′ = ((1 − y)H − 1)/y, and one
  more application of y·d/dy gives
  Σ k²·k!·yᵏ = ((1 − 3y + y²)H − 1 + 2y)/y². The series A(x) = H(y) is
  [A002464](https://oeis.org/A002464), 1, 1, 0, 0, 2, 14, 90, …, the
  permutations with no neighbours differing by 1.
- **A rational form.** Put both sums into the g.f.; x²/y² = (1 + x)²/(1 − x)²,
  and after clearing denominators one factor 1 + x cancels:
  F(x) = (U·A + V)/D with U = 1 − 3x + 5x² − 3x³ + 3x⁴ − x⁵,
  V = −1 + 2x − 2x² − 2x³ + x⁴ and D = (1 − x)⁶(1 + x).
- **Two recurrences.** Substituting A(x) = H(y) in the equation for H and
  reading off coefficients gives, for n ≥ 4,
  Aₙ = (n + 1)Aₙ₋₁ − (n − 2)Aₙ₋₂ + (5 − n)Aₙ₋₃ + (n − 3)Aₙ₋₄,
  A₀, …, A₃ = 1, 1, 0, 0. And D·F = U·A + V gives
  Fₙ = Σᵢ UᵢAₙ₋ᵢ + Vₙ − Σᵢ₌₁⁷ DᵢFₙ₋ᵢ, where D = 1 − 5x + 9x² − 5x³ − 5x⁴
  + 9x⁵ − 5x⁶ + x⁷. F₀, …, F₃ = 0, and Vₙ = 0 for n ≥ 5.
- **The code.** The lists hold the coefficients oldest first, so the
  weight tuples are the polynomials reversed. With k = n − 3 the weights
  of Aₙ₋₄, …, Aₙ₋₁ are (k, 2−k, ~k, k+4), since ~k = −(n − 2). One
  `sumprod` (Python 3.12) over `A[-6:]+F[-7:]` does both sums of Fₙ: the
  first six weights are U₅, …, U₀, the last seven are −D₇, …, −D₁, and
  `F=[0]*7` supplies F₀, …, F₃ and the zeros before them.
- **V for free.** The only Vₙ that reaches a printed term is V₄ = 1. The
  list `A` starts with a fake A₋₁ = −1, which meets the weight U₅ = −1 at
  n = 4 and adds exactly V₄ = 1; it leaves the window after that step.
- **The loop.** `print(f:=…)` prints Fₙ and keeps it for `F+=f,`; the
  print must follow the update, so the loop is `while 1:`.

**Notes**

- Other versions that print the same terms: `F+=…,;print(F[-1])` in place
  of the walrus: 166 bytes; dividing by (1 − x)⁶ with six running sums,
  `P=[t:=t+p for p in P]`, and by 1 + x with `print(q:=t-q)`: 166 bytes;
  the previous program (two updates, n in place of k and an explicit
  `(n==4)` for V₄): 204 bytes.
- Exact integer arithmetic. Correctness for every n rests on the entry's
  generating function; the derivation above is exact algebra. A count of
  all permutations from the definition agrees for n ≤ 9.
- The b-file has 447 terms (a(4) to a(450)); the bar is all of them in
  60 s, and they print in about 0.2 s here.
- a(1559) is the first term with more than 4300 digits (Python's
  int-to-str limit): the program prints 1555 terms, up to a(1558), in
  about 0.6 s and then stops with a `ValueError`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 218 | first entry |
| 2026-11-06 | Python 3 | 204 | use exact sumprod convolutions with padded initial histories |
| 2026-11-07 | Python 3 | 165 | one sumprod for Fₙ, fake A₋₁ supplies V₄, walrus print |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000544), CC BY-SA 4.0.
