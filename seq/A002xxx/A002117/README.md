# A002117

> Apéry's number or Apéry's constant zeta(3). Decimal expansion of zeta(3) = Sum_{m >= 1} 1/m^3.
> — [OEIS A002117](https://oeis.org/A002117)

Offset 1: 1, 2, 0, 2, 0, 5, 6, 9, 0, 3, 1, 5, 9, 5, 9, 4, 2, 8, 5, 3, 9, 9, 7, …

### Python 3 — 109 bytes

```python
q=5;y=0;j=t=4
while(y%t+q)//t or[print(y//t),q:=q*10,y:=y%t*10]:b=4*j*j*~-j;q,y,t=q*(2-j)**3,(q+y)*b,t*b;j+=2
```

**How it works**

A Gibbons-style unbounded spigot (as for π in [A000796](../A000796/)) run
on Apéry's series.

- **Series.** ζ(3) = (5/2)·Σ_(k≥1) (−1)^(k+1)/(k³·C(2k, k)) (Markov 1890,
  Apéry 1979). The term ratio is ρ_k = k³/(2(k+1)²(2k+1)) < 1/4 and the
  first term is 1/2, so ζ(3) = (5/4)·u₁ with u_k = 1 − ρ_k·u_(k+1).
  Every tail u_k lies in [0, 1]: each truncation 1 − ρ_k(1 − ρ_(k+1)(…))
  does, since all ρ < 1, and so does the limit.
- **State.** The digits still to print are those of f(u), where u is the
  current tail and f(x) = (q·x + y)/t; at the start f(x) = 5x/4 (q = 5,
  y = 0, t = 4).
- **Taking a term.** With j = 2k + 2 (4, 6, 8, …; `j+=2`),
  ρ_k = (j−2)³/(4j²(j−1)). Substituting x = 1 − (a/b)·x′ with
  a = (j−2)³ and b = 4j²(j−1) (`4*j*j*~-j`) gives
  f = (−q·a·x′ + (q+y)·b)/(t·b): `q*(2-j)**3` carries the minus sign, and
  one tuple assignment updates q, y, t. `j=t=4` starts both at 4.
- **Printing a digit.** f(0) = y/t and f(1) = (q+y)/t enclose f(u) (f is
  affine, of either slope). Their integer parts agree exactly when
  0 ≤ (y mod t) + q < t, i.e. `(y%t+q)//t` is 0; then the digit is
  `y//t`, certain, and f becomes 10·(f − digit): `q*10` and `y%t*10`.
- **Loop.** As in [A000796](../A000796/), the `while` condition prints a
  digit when it is safe (the list is non-empty, so true) and the body
  always takes one more term. A term is worth about log₁₀ 4 ≈ 0.6 digits,
  so one chance per term keeps up.

**Notes**

- It is exact: integers only, and a digit is printed only when both ends
  of the interval agree. The width |q|/t shrinks by ρ_k < 1/4 per term,
  and ζ(3) is irrational (Apéry), so f(u) is never a whole number and no
  digit is held back forever.
- Each printed value is one digit, so the 4300-digit int-to-str limit does
  not apply. t gains about log₁₀(4k³) digits per term; 20 002 digits take
  about 33 000 terms and some 28 s here (16 reference seconds).
  The bar is the whole b-file (20 002 digits) in 60 s.
- The Amdeberhan–Zeilberger series gains about 3 digits per term but
  needs its quadratic numerator in the update.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 109 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002117), CC BY-SA 4.0.
