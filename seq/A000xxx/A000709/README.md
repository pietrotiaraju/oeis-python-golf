# A000709

> Related to population of numbers of form x^2 + y^2.
> — [OEIS A000709](https://oeis.org/A000709)

Offset 1: 1, 2, 4, 7, 12, 21, 38, 68, 124, 229, 428, 806, 1530, 2919, 5591, 10750, 20730, 40077, 77653, 150752, …

### Python 3 — 197 bytes

```python
from decimal import*
c=getcontext();n=p=1
while 1:
 p+=1;c.prec=2*p;L=c.ln(2)*~-n;t=s=2*L.sqrt()
 for k in range(1,4*p):t*=L/k;s+=t/(2*k+1)
 w=s/10**p;n+=round(s-w)==round(s+w)!=print(round(s)or 1)
```

**What is computed**

- The terms are a(n) = round(∫₁^{2ⁿ⁻¹} du/√(ln u)) for n ≥ 2, with
  a(1) = 1: the OEIS formula, as in Alois P. Heinz's Maple program that
  made the b-file (the integral is Shanks's main term for the number of
  sums of two squares up to x). The entry's Mathematica line uses Floor
  instead, which disagrees with the data, e.g. a(7) = 38 while the
  integral is 37.56.

**How it works**

- With u = e^{x²} the integral becomes 2∫₀^{√L} e^{x²} dx, L = (n−1) ln 2,
  and expanding e^{x²} gives the positive series
  V = 2√L · Σ_{k≥0} L^k / (k!(2k+1)).
- `t` runs through the terms 2√L·L^k/k! and `s` adds t/(2k+1), all in
  `decimal` at 2p digits. Python documents `ln` and `sqrt` as correctly
  rounded and the four operations round to nearest.
- **Certified rounding.** p goes up by one every pass, and the program
  prints only when s − s·10⁻ᵖ and s + s·10⁻ᵖ round to the same integer;
  otherwise it tries the same n again with more digits. With n ≤ p−1,
  L < 0.7p, so the 4p terms leave a tail below 1.3·10^(−1.29p) of the
  sum (term ratio L/k < 0.175), and the roundings add at most 110p·10^(−2p)
  in relative terms (about 5 roundings per term, each 5·10^(−2p)). For
  p ≥ 4 both together are below 10⁻ᵖ, so the true value lies between the
  two bracket ends and its rounding is the printed one. The passes with
  p < 4 are n = 1 (everything exactly 0) and n = 2 at p = 3, which
  prints 2 (checked).
- A true value exactly at a half-integer would make it retry forever; by
  then the sequence itself would not be defined.
- `n+=A==B!=print(…)` advances n only when the two ends agree (the chain
  stops before `print` otherwise), and `round(s)or 1` gives a(1) = 1 from
  the empty integral.

**Notes**

- The precision grows with n (2p digits, p ≈ n) and each term needs 4p
  steps: 666 terms in 60 s.
- The b-file has 1000 terms; the bar is 500 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 197 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000709), CC BY-SA 4.0.
