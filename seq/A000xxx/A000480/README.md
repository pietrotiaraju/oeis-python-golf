# A000480

> a(n) = floor(cos(n)).
> — [OEIS A000480](https://oeis.org/A000480)

Offset 0: 1, 0, −1, −1, −1, 0, 0, 0, −1, −1, …

### Python 3 — 86 bytes

```python
n=0
while 1:
 N=F=1;d=0
 while N%F<n**-d:d-=2;N=n**-d+N*~d*d;F*=~d*d
 print(N//F);n+=1
```

**How it works**

- The program sums the Taylor series of cos n exactly and stops once the
  floor is certain, with the loop of [A000484](../A000484/) (round(cos n))
  minus the ½ shift.
- After k steps, with t_j = n^(2j)/(2j)!, the partial sum
  X_k = Σ_{j≤k} (−1)ʲ t_j is N/F with F = (−1)ᵏ·(2k)!. `d` is −2k, so
  `n**-d` is n^(2k) and `~d*d` = −d(d+1) = −2k(2k−1): `F*=~d*d` extends
  the factorial and flips the sign of F, and `N=n**-d+N*~d*d` adds
  (−1)ᵏ·t_k.
- `N%F` takes the sign of F. For n ≥ 1 it is ≤ 0 < nᵈ at odd k, so the
  loop goes on; at even k it is F·frac(X_k), and the loop stops at the
  first even k with frac(X_k) ≥ t_k. As in A000484, t_k < 1 there puts k
  past the peak of the unimodal terms, so the tail is in (−t_{k+1}, 0),
  cos n lies in (X_k − t_{k+1}, X_k) above ⌊X_k⌋, and `N//F` is ⌊cos n⌋.
- The loop ends because cos n is not an integer for n ≥ 1 (cos n = 0 or
  ±1 would make n a multiple of π/2). At n = 0 the bound is 0 from the
  first step on, and that step (X_1 = 1, F = −2) stops with `N%F` = 0:
  X_1 = 1 is exactly cos 0, and 1 is printed.

**Notes**

- Keeping nᵈ in a variable `p` (`N=F=p=1`, `p*=n*n`) is 87 bytes; the
  previous record, which located n between multiples of π/2 with
  Machin's formula, was 211.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 80 terms (up to a(79)); the bar is the whole b-file in
  60 s. It prints in a fraction of a second, about 930 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 225 | first entry |
| 2026-11-06 | Python 3 | 211 | share the Machin summand and shorten the quadrant test |
| 2026-11-07 | Python 3 | 86 | exact Taylor series of cos n with a one-sided stop test |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000480), CC BY-SA 4.0.
