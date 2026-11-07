# A000529

> Powers of rooted tree enumerator.
> — [OEIS A000529](https://oeis.org/A000529)

Offset 1: 20, 74, 186, 388, 721, 1236, 1995, 3072, 4554, 6542, …

a(n) is the coefficient of x^(n+5) in r(x)ⁿ, where
r(x) = x + x² + 2x³ + 4x⁴ + 9x⁵ + 20x⁶ + … counts rooted trees
([A000081](../A000081/)); that is,
a(n) = [x⁵] (1 + x + 2x² + 4x³ + 9x⁴ + 20x⁵)ⁿ. This reading of the name
matches all 50 terms of the b-file (the entry's only source is Riordan
1958, p. 150).

### Python 3 — 56 bytes

```python
m=7
while[print(m*(m*(m*(m*m-85)+360)-516)//120+6)]:m+=1
```

**How it works**

- **A polynomial.** Only the terms up to x⁵ of r(x)/x matter, and a
  degree-5 coefficient of the n-th power picks a non-constant term from at
  most 5 of the n factors. So [x⁵] (1 + x + 2x² + …)ⁿ = Σ_{k≤5} c_k·C(n, k)
  for fixed numbers c_k, a polynomial in n of degree 5. Fitted to a(1..6):
  120·a(n) = n⁵ + 30n⁴ + 275n³ + 990n² + 1104n.
  The same fact gives Plouffe's generating function on the entry,
  (20 − 46x + 42x² − 18x³ + 3x⁴)/(1 − x)⁶, which the entry marks as
  conjectured: every degree-5 polynomial sequence has a g.f. over (1 − x)⁶.
- **Centering.** With m = n + 6 the m⁴ term drops out:
  120·a(n) = m⁵ − 85m³ + 360m² − 516m + 720. The program prints
  m(m(m(m² − 85) + 360) − 516)/120 + 6 (Horner form) for m = 7, 8, 9, …
  The bracket equals 120·(a(n) − 6) and a(n) is an integer, so `//120` is
  exact; the constant 720/120 = 6 goes outside as `+6`.
- **The loop.** `print` sits in the loop condition: it returns `None`, and
  `[None]` is a non-empty list, so the loop never ends (the
  [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: Horner in n,
  `n=1` / `while[print(n*(n*(n*(n*(n+30)+275)+990)+1104)//120)]:n+=1`:
  61 bytes; the g.f. expanded as Σ_j c_j·C(n + 5 − j, 5) with `math.comb`:
  108 bytes.
- Exact integer arithmetic. Correctness for every n rests on the reading of
  the name above (equivalently, on Plouffe's g.f.); both give the same
  degree-5 polynomial, and it matches all 50 b-file terms.
- About 3.2 million terms in 60 s here. The b-file has 50 terms (up to a(50));
  the bar is the whole b-file in 60 s, and it prints in well under a second.
- The centred form shows a(n) < (n + 6)⁵, so a term with more than 4300
  digits (Python's int-to-str limit) needs n + 6 > 10^860: out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 108 | first entry |
| 2026-11-07 | Python 3 | 56 | degree-5 polynomial, centred at m = n + 6 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000529), CC BY-SA 4.0.
