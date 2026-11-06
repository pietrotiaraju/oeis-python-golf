# A000186

> Number of 3 X n Latin rectangles in which the first row is in order.
> — [OEIS A000186](https://oeis.org/A000186)

Offset 0: 1, 0, 0, 2, 24, 552, 21280, 1073760, 70299264, 5792853248, …

### Python 3 — 77 bytes

```python
a=b=c=f=n=0
while f:=2**n*~-n-n*f:a,b,c=n*(n*a+b+2*c)-f,n*a,n*b;print(a);n+=1
```

**How it works**

- Gessel's e.g.f. (listed in A000186) is A(x) = Σ a(n)xⁿ/n! =
  e^(2x)·G(x) with G(x) = Σ_k k!·x^k/(1+x)^(3k+3) = f(t)/(1+x)³,
  where f(t) = Σ k!·t^k and t = x/(1+x)³.
- f satisfies t²f′ + (t−1)f + 1 = 0. Substituting t (dt/dx =
  (1−2x)/(1+x)⁴) and then A = e^(2x)G gives
  x²(1+x)A′ = (1+x)(1−x−x²−2x³)A − (1−2x)e^(2x), and dividing by 1+x:
  x²A′ = (1−x−x²−2x³)A − E with E = (1−2x)e^(2x)/(1+x).
- With u_n = a(n)/n! the coefficient of xⁿ reads
  u_n = n·u_{n−1} + u_{n−2} + 2u_{n−3} + E_n, and ε_n = n!·E_n follows
  from (1+x)E = (1−2x)e^(2x): ε_n = 2ⁿ(1−n) − n·ε_{n−1}. The program
  keeps f = −ε.
- Instead of a(n−1), a(n−2), a(n−3) the loop keeps the scaled values
  a = (n−1)!·u_{n−1} = a(n−1), b = (n−1)!·u_{n−2}, c = (n−1)!·u_{n−3}.
  Then a(n) = n!·u_n = n(n·a + b + 2c) − f, and the next state is just
  b = n·a, c = n·b: no polynomial coefficients of degree 3.
- No seeds are needed: every old value is multiplied by n at the step
  n = 0, so starting from zeros gives f = −1 and a(0) = 1, and the
  recurrence holds from n = 1 on. A sympy check of the ODE on the series
  and the whole b-file agree.

**Notes**

- Each term is a handful of big-integer operations; the whole b-file
  (208 terms) prints in well under a second. The bar is the whole
  b-file in 60 s.
- `while f:=…:` computes f in the loop condition, 1 byte under `while 1:`.
  It never stops the loop, because f is never 0. Mod 3 the update
  f = 2ⁿ(n−1) − n·f gives f ≡ −(−1)ⁿ when 3 | n, f ≡ −f_{n−1} when
  n ≡ 1, and f ≡ 2ⁿ + f_{n−1} ≡ 2·(−1)ⁿ when n ≡ 2 (mod 3), so f is
  never divisible by 3.
- Python's 4300-digit limit for printing ints stops the program after
  a(859) (4297 digits); a(860) has 4303.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 78 | first entry |
| 2026-11-05 | Python 3 | 77 | f computed in the while condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000186), CC BY-SA 4.0.
