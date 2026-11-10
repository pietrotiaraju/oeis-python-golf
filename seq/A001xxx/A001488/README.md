# A001488

> Expansion of (Product_{j>=1} (1-(-x)^j) - 1)^10 in powers of x.
> — [OEIS A001488](https://oeis.org/A001488)

Offset 10: 1, -10, 45, -120, 200, -162, -160, 810, -1530, 1730, -749, -1630, 4755, -7070, 6700, -2450, …

### Python 3 — 111 bytes

```python
H=[t:=1]
while[print(H[-1])]:H+=sum(~-(j&2)*H[g]*(11*g+t)for j in range(-t,t)if~t<(g:=j-j*3*j+2>>1)<0)//t,;t+=1
```

**How it works**

- **Pentagonal numbers.** Euler's pentagonal number theorem,
  Π_{j≥1} (1 − y^j) = Σ_{i∈ℤ} (−1)^i·y^(i(3i−1)/2), with y = −x gives
  Π_{j≥1} (1 − (−x)^j) − 1 = Σ_{i≠0} ε_i·x^(p_i), where p_i = i(3i−1)/2
  and ε_i = (−1)^(i+p_i) = (−1)^(i(3i+1)/2). That sign is +1 for
  i ≡ 0, 1 (mod 4) and −1 for i ≡ 2, 3, so ε_i = 1 − (i&2) (Python's
  two's complement makes `j&2` right for negative i too).
- **Factor out x.** The i = 1 term is x, so the series is x·u(x) with
  u(0) = 1, and the coefficient of x^(k+t) in its k-th power (here
  k = 10) is w(t) = [x^t] u(x)^k. u has the coefficient ε_i at degree
  d = p_i − 1 = (3i² − i − 2)/2.
- **J. C. P. Miller's recurrence.** Comparing the coefficients of x^(t−1)
  in u·(u^k)′ = k·u′·u^k gives

  t·w(t) = Σ_{d=1}^{t} ((k+1)·d − t)·u(d)·w(t − d),

  so `//t` is an exact division, and only the pentagonal degrees d
  contribute, about 1.6·√t of them.
- **Negated degree.** The walrus holds g = −d = `j-j*3*j+2>>1` (the
  numerator is even), so `H[g]` is w(t − d) while `H` holds w(0), …,
  w(t−1), and (k+1)·d − t = −((k+1)·g + t). That minus sign goes into
  the sign factor: `~-(j&2)` is (j&2) − 1 = −ε_i.
- **The filter** `~t<g<0` (−t ≤ g ≤ −1) drops i = 0 (g = 1, the constant
  1 that was subtracted) and i = 1 (g = 0, the term being solved for) and
  keeps the index inside `H`; `range(-t,t)` contains every i with
  p_i − 1 ≤ t. `H=[t:=1]` stores w(0) = 1, which the loop condition
  prints first.

**Notes**

- One template serves the whole group; only the factor k + 1 changes:
  [A001482](../A001482/) (k = 4), [A001483](../A001483/) (k = 5), [A001484](../A001484/) (k = 6), [A001485](../A001485/) (k = 7), [A001486](../A001486/) (k = 8), [A001487](../A001487/) (k = 9), [A001488](../A001488/) (k = 10), [A001490](../A001490/) (k = 12).
- With d itself (`H[-g]`, `0<g<=t`, `(1-(j&2))`) the program is 4 bytes
  longer. Two zero pads in front, `H=[0,0,t:=1]`, make the bound `g<0`
  unnecessary (both dropped terms then read a zero), but cost two bytes
  more than they save.
- Exact integer arithmetic, so the program is right for every n; the
  coefficients grow only polynomially, far from the int-to-str limit.
- The filter scans 2t values of i for each term, so the run time is
  quadratic: the b-file (9991 terms, n = 10 to 10000) prints in about 40 s here.
  The bar is 8000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 111 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001488), CC BY-SA 4.0.
