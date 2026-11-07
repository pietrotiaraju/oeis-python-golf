# A000503

> a(n) = floor(tan(n)).
> — [OEIS A000503](https://oeis.org/A000503)

Offset 0: 0, 1, -3, -1, 1, -4, -1, 0, -7, -1, …

### Python 3 — 121 bytes

```python
n=0
while 1:
 a,b,c,d,k=n,0,1,1,3
 while-b%(d or 1)*(2*c-k*d)<n**k:a,b,c,d=k*a-n*n*b,a,k*c-n*n*d,c;k+=2
 print(b//d);n+=1
```

**How it works**

- This is the [A000209](../A000209/) program (round(tan n)) without the
  ½ shift. Lambert's continued fraction tan n = n/(1 − n²/(3 − n²/(5 − …)))
  has convergents A_m/B_m with X_{m+1} = (2m+1)X_m − n²X_{m−1}, A₀ = 0,
  A₁ = n, B₀ = B₁ = 1. With k = 2m + 3 the state is a, b = A_{m+1}, A_m and
  c, d = B_{m+1}, B_m, and `a,b,c,d=k*a-n*n*b,a,k*c-n*n*d,c` moves m up by one.
- With the true tail R = R_{m+1} = (2m+1) − n²/((2m+3) − …),
  tan n = (R·A_m − n²A_{m−1})/(R·B_m − n²B_{m−1}), a decreasing function of R
  because A_{m+1}B_m − A_mB_{m+1} = n^(2m+1) > 0. For m ≥ n − 1 the tail lies
  in [m − ½, ∞] (every R_j with j ≥ n + 1 is at least j, see A000209), so
  tan n lies between b/d (R = ∞) and (2a − kb)/v with v = 2c − kd
  (R = m − ½), as long as v·d > 0 keeps the pole out. The two ends differ by
  2n^(2m+1)/(vd).
- (−b mod d)/d is the gap from b/d up to the next integer, so
  ⌊tan n⌋ = ⌊b/d⌋ = `b//d` once (−b mod d)·v > 2n^(2m+1). The loop stops when
  `-b%d*v` is at least n^k = n^(2m+3), which is more than that for n ≥ 2.
  If v·d ≤ 0 the left side is ≤ 0 (Python's `%` has the sign of d), so the
  loop cannot stop with the pole inside.
- No guard m ≥ n − 1 is needed for n ≥ 8: by A000209's bound on the
  Bessel-polynomial values B_j(n), |v·d| < n^k/4 for m ≤ n − 2 (that page's
  c, d are twice these), and |−b mod d| < |d|, so the test cannot pass
  early. The values for n < 8 are checked against the b-file.
- `(d or 1)` covers B_m(n) = 0, which is not ruled out: the left side is
  then 0 and the loop goes on. With `<` rather than `<=`, n = 0 stops at
  once (0 < 0ᵏ fails) and prints 0//1 = 0.
- tan n is irrational for n ≥ 1 (Lambert), so b/d stays away from integers
  in the limit while the width tends to 0, and the loop ends.

**Notes**

- Exact integer arithmetic. Correctness for every n rests on the bracket
  above; termination on the irrationality of tan n.
- The previous record, Taylor series for cos n and sin n with a box of
  four corner floors, was 239 bytes.
- About 1140 terms in 60 s here (the continued fraction runs to m ≈ 1.05–1.15n).
  The b-file has 1001 terms (up to a(1000)); the bar is 100 terms in 60 s.
  The whole b-file takes about 39 s.
- The terms are small (|a(n)| is large only when n is near an odd multiple
  of π/2), so the 4300-digit int-to-str limit does not apply in practice.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 261 | first entry |
| 2026-11-06 | Python 3 | 239 | cancel the unused factorial and test corner agreement with a set |
| 2026-11-07 | Python 3 | 121 | Lambert continued fraction (A000209 bracket) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000503), CC BY-SA 4.0.
