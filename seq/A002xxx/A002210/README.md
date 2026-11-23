# A002210

> Decimal expansion of Khinchin's constant.
> — [OEIS A002210](https://oeis.org/A002210)

Offset 1: 2, 6, 8, 5, 4, 5, 2, 0, 0, 1, 0, 6, 5, 3, 0, 6, 4, 4, 5, 3, 0, 9, …

### Python 3 — 360 bytes

```python
B=8;p=b=0
while B:=2*B:
 for U in 1<<B,-1<<B:
  z=l=-1;k=1
  while k<B:l+=(t:=U//(k<<k));z+=2*t//k;k+=1
  Z=[z+l*l//U]
  for m in range(5,B,2):Z+=sum(map(int.__mul__,Z,Z[::-1]))*2//(m*U),
  S=sum((z-U)//n//j for n,z in enumerate(Z,1)for j in range(n,2*n));E=U
  while k:E=U+E*S//(k*(l+B+4));k-=1
  a,b=b,str(E*10**B//U)
 while a[:p+1]==b[:p+1]:print(a[p]);p+=1
```

**How it works**

- **Series.** Khinchin's constant is K = ∏_(r≥1) (1 + 1/(r(r+2)))^(log₂ r),
  and ln K · ln 2 = Σ_(k≥2) −ln(1 − 1/k)·ln(1 + 1/k). Expanding
  −ln(1−y)·ln(1+y) = Σ_(n≥1) c_n·y^(2n) with
  c_n = (1 − 1/2 + 1/3 − … + 1/(2n−1))/n = (1/n)·Σ_(j=n..2n−1) 1/j
  and summing over k gives the Shanks–Wrench series
  S = ln K · ln 2 = Σ_(n≥1) c_n·(ζ(2n) − 1), whose terms shrink like 4⁻ⁿ.
- **ζ(2n).** ζ(2) = π²/6 = 2·Σ_(k≥1) 1/(k²·2^k) + ln²2 (Euler's
  Li₂(1/2) = π²/12 − ln²2/2), with ln 2 = Σ_(k≥1) 1/(k·2^k); both series
  share the term t = 1/(k·2^k). The rest comes from Euler's recurrence
  (n + ½)·ζ(2n) = Σ_(k=1..n−1) ζ(2k)·ζ(2n−2k) for n ≥ 2 (from
  πx·cot πx = 1 − 2Σ ζ(2n)x^(2n) and (cot)′ = −1 − cot²), so `m` = 2n + 1
  and `Z[::-1]` pairs ζ(2k) with ζ(2n−2k).
- **exp.** K = e^x with x = S/ln 2, by Horner from the top:
  E ← 1 + E·x/k for k = B, …, 1 gives Σ_(k≤B) x^k/k!.
- **Two passes, one code.** All numbers are integers in units of 2^−B,
  and `U` is the unit 1 with a sign. With U = 2^B every floor rounds down,
  and every step is monotone (sums, products of positive values, division
  by positive integers), so the pass gives lower bounds. With U = −2^B the
  stored values are negated (`//(m*U)`, `//U` and `E*S//(k*…)` carry the
  sign), the same floors now round the magnitudes up, and the pass gives
  upper bounds. The tails go outward too: `z=l=-1` covers the two seed
  series (stopped at k = B − 1, tails < 2^−B); the ζ series stops at
  n = B/2 − 1, where its tail is below 4^(−n)/(n+1) ≤ 2^−B because
  c_n ≤ 1/n and ζ(2n) − 1 ≤ 3·4⁻ⁿ; and the exp tail is below 2^−B as
  x < 2 and B ≥ 16.
- **Dividing by ln 2.** x needs the opposite bound of ln 2: `l+B+4` is at
  least ln 2 in the lower pass and at most ln 2 − 4·2^−B in magnitude in
  the upper one (the B − 1 floors move l by less than B units). That
  raises the upper x by about 4x/ln 2 > 5 units of 2^−B, more than the
  ζ tail can take off x (1.5 units) plus the unit the exp tail needs, so
  the upper pass needs no other tail term.
- **Size of the errors.** The seeds are within a few B units, and each
  step of Euler's recurrence at most doubles an error ((4n−1)/(2n+1) < 2,
  using Σ_(k≥1) (ζ(2k) − 1) = 3/4), so every bound stays within
  4B·2^(n−B) of its value; hence x < 1.2 in both passes. (In practice
  the errors grow only polynomially: 610 of the 616 digits that 2^−2048
  allows.)
- **Digits.** `E*10**B//U` is ⌊K_lo·10^B⌋ in the first pass and
  ⌊K_hi·10^B⌋ in the second. ⌊K·10^B⌋ lies between them, so the leading
  digits the two strings share are digits of K. `p` counts the digits
  already printed; `a[:p+1]==b[:p+1]` rechecks from the first digit, so a
  level whose interval is less favourable can never print a wrong digit.
  Then B doubles (16, 32, …).

**Notes**

- Every printed digit is proven by the two bounds. K is not known to be
  irrational: if it were a terminating decimal, the program would wait at
  that digit forever (each interval would straddle it) rather than print
  a wrong one. The 1200 digits of the b-file all come out.
- Each level gives about 0.3·B digits: 149 at B = 512, 302 at 1024,
  610 at 2048 (after about 11 s here), 1226 at 4096 (about 110 s here).
  The cost is Euler's recurrence, about B²/8 products of B-bit numbers.
- The b-file has 1200 terms; the bar is 500 digits in 60 s, which arrive
  with the B = 2048 level, well within half the time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 360 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002210), CC BY-SA 4.0.
