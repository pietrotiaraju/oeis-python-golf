# A000209

> Nearest integer to tan n.
> — [OEIS A000209](https://oeis.org/A000209)

Offset 0: 0, 2, −2, 0, 1, −3, 0, 1, −7, 0, 1, −226, …

### Python 3 — 125 bytes

```python
n=0
while 1:
 a,b,c,d,k=n-~n,1,2,2,3
 while-b%(d or 1)*(2*c-k*d)<=n**k:a,b,c,d=k*a-n*n*b,a,k*c-n*n*d,c;k+=2
 print(b//d);n+=1
```

**How it works**

- Lambert's continued fraction tan n = n/(1 − n²/(3 − n²/(5 − …))). Its
  convergents A_m/B_m follow A_m = (2m−1)A_{m−1} − n²A_{m−2} (B the same),
  with A_0 = 0, A_1 = n, B_0 = B_1 = 1. The program runs the combinations
  2A + B and 2B of the two sequences, so with k = 2m + 3 the state is
  a, b = 2A_{m+1} + B_{m+1}, 2A_m + B_m and c, d = 2B_{m+1}, 2B_m. Then
  b/d = A_m/B_m + ½ and the rounding is just `b//d`.
- With the true tail R = R_{m+1} = (2m+1) − n²/((2m+3) − …),
  tan n = (R·A_m − n²A_{m−1})/(R·B_m − n²B_{m−1}), a decreasing Möbius
  function of R. Every tail with j ≥ n + 1 has R_j ≥ j (downward induction
  on a truncation: R_{j+1} ≥ j + 1 gives R_j ≥ 2j − 1 − n²/(j+1) ≥ j), and
  then R_n ≥ n − 1. So for m ≥ n − 1, R lies in [m − ½, ∞], and tan n lies
  between its values at R = ∞ (that is b/d − ½) and at R = m − ½
  ((2a − kb)/v − ½ with v = 2c − kd), as long as the pole is outside, which
  is exactly v·d > 0.
- The two ends differ by 8n^(2m+1)/(vd), because
  A_{m+1}B_m − A_mB_{m+1} = n^(2m+1). With θ = (−b mod d)/d, the distance
  from b/d up to the next integer, the rounding is settled once
  θ·vd > 8n^(2m+1). The test `-b%d*v > n**k` implies that: it fails when
  vd ≤ 0 (the left side is then ≤ 0), and n^k ≥ 8n^(k−2) once n ≥ 3.
- No guard m ≥ n − 1 is needed, because the test cannot pass before that.
  B_j(n) is the real part of the reverse Bessel polynomial θ_j(in), and
  |θ_j(in)|² = Σ_i s_i(j+½)·n^(2j−2i) (DLMF 10.49.18), with every
  s_i ≤ (j+½)^(2i). So |B_j(n)| ≤ n^j/√(1 − ((j+½)/n)²), which for
  m ≤ n − 2 gives |vd| < 0.97·n^k when n ≥ 8, and |−b mod d| < |d|. The
  n < 8 are in the bar.
- `(d or 1)` covers B_m(n) = 0, which I could not rule out (it does not
  happen for n < 400, m < 4n): the modulus becomes 1, the left side 0, and
  the loop goes on.
- The loop ends: tan n is never a half-integer (otherwise e^(2in) would be
  algebraic, against Lindemann), and the width shrinks like (en/2m)^(2m),
  so it stops near m ≈ 1.4n.

**Notes**

- About 1180 terms in 60 s here. The bar is 900 terms in 60 s.
- Checking only from m = n − 1 on and comparing the two floors directly
  (`k<2*n or d*(v:=2*c-k*d)<1or b//d-(2*a-k*b)//v`) is 144 bytes and does
  about 3300 terms; the guarded `8*n**k` form of this test is 136 bytes and
  about 2300 terms. Without the guard the test runs from m = 0, and that
  costs the speed.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 125 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000209), CC BY-SA 4.0.
