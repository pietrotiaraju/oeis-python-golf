# A001664

> Quadratic coefficient of the n-th converging polynomial of Weber functions.
> — [OEIS A001664](https://oeis.org/A001664)

Offset 2: 1, −6, 25, −60, −203, 3710, −21347, −50400, 2465969, −24201342, …

### Python 3 — 203 bytes

```python
A=[0,0,1];B=[0,0,0,1,-1];m=1
while 1:
 m+=2;C=[0]*4
 for t in range(m,0,-1):C+=t*(3*C[-1]+2*~t*C[-2]+(4*m+2)*B[~t])-(4*t+3*m-1)*B[-t]+3*B[1-t]-2*A[2-t]+(4*m-2)*A[1-t]-2*m*~-m*A[-t],
 print(C[-3]);A,B=B,C
```

**How it works**

- **The definition.** Wynn ("Converging factors for the Weber parabolic
  cylinder functions of complex argument", 1963) builds polynomials
  p_r(k) = Σₛ p(r,s)·kˢ by the recurrences (42)–(46) of his paper, and the
  entry's terms are the coefficients p(n,2) of his Table VII (a = ½,
  θ = 0, so φ = 1, λ = 2(a−1) = −1 and μ = (a−½)(a−3/2) = 0). The program
  follows the entry's Maple program (R. J. Mathar, 2025), which transcribes
  those recurrences with the misprint in (45) corrected
  (p_{r−2,2} → p_{r−2,1}). This reconstruction reproduces all 22 terms of
  the entry; it is the definition the page relies on.
- **One recurrence.** With φ = 1, λ = −1, μ = 0, the four equations (43)–(46)
  are the same formula, (44), read with p(r,s) = 0 for s < 0 or s > r:

  p(r,s) = 3(s+1)·p(r,s+1) − 2(s+1)(s+2)·p(r,s+2)
  + 2(4r−1)(s+1)·p(r−1,s+1) − (4s+6r)·p(r−1,s) + 3·p(r−1,s−1)
  − 2·p(r−2,s−2) + 2(4r−3)·p(r−2,s−1) − 4(r−1)(2r−1)·p(r−2,s),

  for r ≥ 2 and 0 ≤ s ≤ r, from the rows p₀ = 1 and p₁ = k − 1 of (38)
  (it also gives the row p₂ = 1 − 3k + k² that the Maple program lists).
  At s = r it gives 3·1 − 2·1 = 1, Wynn's p(r,r) = 1 (42), and above the
  top it gives 0, so each row can be run from any s ≥ r down to 0. Every
  division by φ + 1 = 2 in the Maple program is exact: the formula above
  is already divided.
- **Rows as reversed lists.** A, B, C are the rows r−2, r−1, r, stored
  from the top coefficient down to p(r,0), behind four zeros, so p(r,s) is
  `C[~s]` and indices just past either end read a padding zero (negative
  ones from the back, small positive ones from the front). With t = s+1,
  p(r,s+1) and p(r,s+2) are the last two entries appended (`C[-1]`,
  `C[-2]`), `B[~t]`, `B[-t]`, `B[1-t]` are p(r−1,s+1), p(r−1,s),
  p(r−1,s−1), and `A[2-t]`, `A[1-t]`, `A[-t]` are p(r−2,s−2), p(r−2,s−1),
  p(r−2,s). The coefficients are written with m = 2r−1:
  2(4r−1) = 4m+2, 6r−4 = 3m−1, 2(4r−3) = 4m−2, 4(r−1)(2r−1) = 2m(m−1),
  and −2t(t+1) = 2t·~t.
- **The loop.** m runs over 3, 5, 7, … (r = 2, 3, 4, …); each row is built
  for s = m−1 down to 0 (m ≥ r+1, so the top entries are the zeros the
  formula gives there), its p(r,2) = `C[-3]` is printed, and the rows
  shift. The four padding zeros keep every index in range: a row built
  with m steps has m+4 entries and is read up to m+3 places from its end
  in the next row and m+4 in the one after (the two starting rows are
  padded to fit as well).

**Notes**

- Exact integer arithmetic, so every term is the one the recurrence
  defines. As a check on the transcription beyond the 22 terms, the
  constant coefficients p(r,0) agree with −A001662(r+1) (the entry's
  "absolute coefficient", Airey's converging factor) for r = 1 … 199,
  the whole b-file of [A001662](../A001662/).
- The bar is the whole b-file, 22 terms (n = 2 … 23), which take a
  fraction of a second; the program keeps going.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 203 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001664), CC BY-SA 4.0.
