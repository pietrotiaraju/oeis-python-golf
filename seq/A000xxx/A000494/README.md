# A000494

> Nearest integer to sin(n).
> — [OEIS A000494](https://oeis.org/A000494)

Offset 0: 0, 1, 1, 0, −1, −1, 0, 1, 1, 0, …

### Python 3 — 95 bytes

```python
n=0
while 1:
 p=2*n;N=p+1;F=2;d=0
 while N%F<p:d+=2;p*=n*n;N=p+N*~d*d;F*=~d*d
 print(N//F);n+=1
```

**How it works**

- The nearest integer to sin n is ⌊sin n + ½⌋, because sin n = ±½ is
  impossible for n ≥ 1 (e^(in) would be algebraic, against Lindemann).
  The program sums the Taylor series of sin n + ½ exactly and stops once
  the floor is certain, with the loop of [A000484](../A000484/).
- After k steps, with t_j = n^(2j+1)/(2j+1)!, the partial sum
  X_k = ½ + Σ_{j≤k} (−1)ʲ t_j is N/F with F = 2·(−1)ᵏ·(2k+1)! and
  p = 2n^(2k+1); it starts at X_0 = n + ½ (`p=2*n;N=p+1;F=2`). Here `d`
  is 2k, so `~d*d` = −d(d+1) = −2k(2k+1) extends the factorial and flips
  the sign of F, and `N=p+N*~d*d` adds (−1)ᵏ·t_k.
- `N%F` takes the sign of F: at odd k it is ≤ 0 < p and the loop goes
  on; at even k it is F·frac(X_k) and p/F = t_k, so the loop stops at the
  first even k with frac(X_k) ≥ t_k.
- That stop is safe. The terms are unimodal (t_{j+1}/t_j =
  n²/((2j+2)(2j+3)) falls with j and is never 1), every term before the
  peak is at least t_0 = n ≥ 2 when n ≥ 2, and the test needs t_k < 1; for
  n = 1 the terms fall from the start. So the terms fall from k on, the
  tail after an even k is in (−t_{k+1}, 0), and sin n + ½ lies in
  (X_k − t_{k+1}, X_k), above ⌊X_k⌋. Hence `N//F` is the answer.
- The loop ends because sin n + ½ is not an integer for n ≥ 1. At n = 0,
  p = 0 and the first test `1<0` fails at once: X_0 = ½ prints 0.

**Notes**

- Without `p` (`2*n**d` twice, from `d=1`) the loop is 98 bytes and
  slower, about 880 terms in 60 s, under the bar. The previous record,
  215 bytes, placed n between multiples of π/6 with Machin's formula.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file
  in 60 s, which takes about 11 s here (about 1440 terms in 60 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 239 | first entry |
| 2026-11-06 | Python 3 | 215 | share the Machin summand and compute the sector sign arithmetically |
| 2026-11-07 | Python 3 | 95 | exact Taylor series of sin n + ½ with a one-sided stop test |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000494), CC BY-SA 4.0.
