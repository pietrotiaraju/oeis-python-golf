# A000287

> Number of rooted polyhedral graphs with n edges.
> — [OEIS A000287](https://oeis.org/A000287)

Offset 6: 1, 0, 4, 6, 24, 66, 214, 676, 2209, 7296, 24460, 82926, …

### Python 3 — 77 bytes

```python
a=b=c=0;t=n=6
while 1:a,b,c=t+2-12*a-6*b-c>>3,a,b;print(a);t=4*t-10*t//n;n+=1
```

**How it works**

- Coserea's generating function on the OEIS page is
  A(x) = x² − 2x³/(1+x) + x·(2x² − 10x − 1 + (1−4x)^(3/2)) / (2(x+2)³).
  Multiplying the last part by (x+2)³ leaves x·(2x² − 10x − 1 +
  (1−4x)^(3/2))/2, whose coefficient of xⁿ for n ≥ 4 is
  t(n−1) = [x^(n−1)] (1−4x)^(3/2) / 2 = 6·Cat(n−3)/(n−1).
- The middle part −2x³/(1+x) contributes 2·(−1)ⁿ for n ≥ 3, and (x+2)³ turns
  the sequence (−1)ⁿ into itself times 8 − 12 + 6 − 1 = 1. Reading off
  coefficients gives, for n ≥ 6,
  8·a(n) + 12·a(n−1) + 6·a(n−2) + a(n−3) = t(n−1) + 2·(−1)ⁿ,
  with a(3) = a(4) = a(5) = 0.
- At the top of each round `a`, `b`, `c` are a(n−1), a(n−2), a(n−3) and `t`
  is t(n−1). Then t + 2 − 12a − 6b − c is 8·a(n) for even n and
  8·a(n) + 4 for odd n, so `>>3` (floor division by 8) gives a(n) either way:
  the alternating ±2 costs only the `+2`. `>>` binds looser than `+` and
  `-`, so no parentheses are needed.
- t(n) = t(n−1)·(4n − 10)/n. Written as `t=4*t-10*t//n`, the
  [A000108](../A000108/) step, the division is exact because 10·t(n−1)/n =
  4·t(n−1) − t(n) is an integer. All t(m) are integers: the coefficients of
  √(1−4x) after the first are −2·Cat(m−1), all even, and
  (1−4x)^(3/2) = (1−4x)·√(1−4x).
- The start is t(5) = 6 and n = 6, hence `t=n=6`; the first round prints
  (6 + 2) >> 3 = 1 = a(6).

**Notes**

- The program is exact for every n given that generating function. It
  also matches all 995 b-file terms. With x = z/(1+z)², so that z = C(x) − 1
  for the Catalan series C, the generating function simplifies to
  A(x) = x² − 2x³/(1+x) − z²/(1+2z)³ (checked as power series), because
  x + 2 = (2z+1)(z+2)/(1+z)² and 2x² − 10x − 1 + (1−4x)^(3/2) =
  −2z(z+2)³/(1+z)⁴.
- Plouffe's order-4 recurrence with linear coefficients (corrected by
  House) needs no Catalan term but five states and four polynomial
  coefficients, which is much longer. The first-order recurrence for b(n)
  in Irvine's formula on the page does not reproduce the terms as printed:
  from b(3) = 2 it gives b(4) = −792/536.
- Computing t(n−1) with `comb` instead costs the import and more than the
  update saves.
- Exact integers. Python's 4300-digit int-to-str limit stops the program at
  a(7163), after printing a(6) to a(7162).
- The b-file has 995 terms (n = 6 to 1000, 593 digits) and all of them print
  at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000287), CC BY-SA 4.0.
