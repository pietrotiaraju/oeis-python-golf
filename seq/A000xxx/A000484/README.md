# A000484

> a(n) = round(cos(n)).
> — [OEIS A000484](https://oeis.org/A000484)

Offset 0: 1, 1, 0, −1, −1, 0, 1, 1, 0, −1, …

### Python 3 — 89 bytes

```python
n=0
while 1:
 N=3;F=p=2;d=0
 while N%F<p:d-=2;p*=n*n;N=p+N*~d*d;F*=~d*d
 print(N//F);n+=1
```

**How it works**

- round(cos n) = ⌊cos n + ½⌋, because cos n = ±½ is impossible for n ≥ 1
  (e^(in) would be algebraic, against Lindemann). The program sums the
  Taylor series of cos n + ½ exactly and stops once the floor is certain.
- After k steps, with t_j = n^(2j)/(2j)!, the partial sum
  X_k = ½ + Σ_{j≤k} (−1)ʲ t_j is N/F with F = 2·(−1)ᵏ·(2k)! and p = 2n^(2k);
  `d` is −2k. Each step does `d-=2` and `p*=n*n`, and `~d*d` is
  −d(d+1) = −2k(2k−1), so `F*=~d*d` builds the factorial with the sign
  flipped every step and `N=p+N*~d*d` adds the new term (−1)ᵏ·t_k.
- `N%F` takes the sign of F. At odd k it is ≤ 0 < p, so the loop always
  goes on. At even k it is F times the fractional part of X_k, and p/F is
  t_k, so the loop stops at the first even k with frac(X_k) ≥ t_k.
- That stop is safe. The terms are unimodal (the ratio
  t_{j+1}/t_j = n²/((2j+1)(2j+2)) falls with j and is never 1), and for
  n ≥ 2 every term before the peak is at least t_0 = 1, while the test
  needs t_k ≤ frac(X_k) < 1; for n = 1 they fall from the start. So the
  terms fall from k on, and at even k the alternating tail is in
  (−t_{k+1}, 0). Then cos n + ½ lies in (X_k − t_{k+1}, X_k), whose lower
  end is above X_k − frac(X_k) = ⌊X_k⌋, and `N//F` is the answer.
- The loop ends: X_k tends to cos n + ½, which is not an integer, so its
  fractional part tends to a positive limit while t_k tends to 0. At
  n = 0, p is 0 after the first step and the second step (k = 2) stops
  with X = 3/2, printing 1.

**Notes**

- The same loop with `d+=2` from `d=-1` is 90 bytes. Without the `p`
  variable (`2*n**-d` twice) it is 92 bytes and too slow for the bar
  (about 870 terms in 60 s). Bracketing n between multiples of π/3 with
  Machin's formula, the previous record, was 213 bytes.
- [A000480](../A000480/) (⌊cos n⌋) and [A000494](../A000494/)
  (round(sin n)) use the same loop.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file
  in 60 s, which takes about 12 s here (about 1380 terms in 60 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 224 | first entry |
| 2026-11-06 | Python 3 | 213 | share the two Machin summands |
| 2026-11-07 | Python 3 | 89 | exact Taylor series of cos n + ½ with a one-sided stop test |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000484), CC BY-SA 4.0.
