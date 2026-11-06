# A000132

> Number of ways of writing n as a sum of 5 squares.
> — [OEIS A000132](https://oeis.org/A000132)

Offset 0: 1, 10, 40, 80, 90, 112, 240, 320, 200, 250, 560, 560, 400, 560, 800, 960, …

### Python 3 — 74 bytes

```python
m=5
while[print(sum(1<<j*j*m+m for j in range(-m,m))**5>>m*m&2**m-1)]:m+=1
```

**How it works**

- Signs and order count, so a(n) is the coefficient of qⁿ in θ(q)⁵ with
  θ(q) = Σ_{j∈ℤ} q^(j²).
- The program evaluates the series at q = 2^m, so every coefficient becomes
  an m-bit digit of one big integer. `1<<j*j*m+m` is 2^(m(j²+1)), so the
  sum is 2^m·θ(2^m), cut to |j| ≤ m. That keeps every j with j² ≤ n; larger
  |j| only adds to digits above n.
- After the fifth power the number is 2^(5m)·θ⁵, so a(k) sits in digit
  k + 5. `>>m*m&2**m-1` reads digit m, which is a(m − 5), and starting at
  m = 5 prints a(0) first.
- Reading digit m − 5 directly would need `>>m*(m-5)`, 4 bytes longer. The
  `+m` in the exponent moves everything up one digit for 2 bytes.

**Why the digits never carry**

All coefficients are ≥ 0, so digits at and below m are exact as long as each
is below 2^m. Digit d ≤ m holds a(d − 5), so it is enough that
a(k) < 2^(k+5) for every k:

- for k < 10 this is checked directly (a(9) = 250 < 2¹⁴);
- for k ≥ 10, each of the five numbers has |x| ≤ √k, so
  a(k) ≤ (2⌊√k⌋ + 1)⁵. This is below 2^(k+5) at k = 10, and
  5·log₂(2√k + 1) grows by less than 1 per step for k ≥ 4, so the bound
  holds from there on.

Digits above m (from the cut-off |j| ≤ m terms) can be anything; the mask
drops them and carries only move upward.

**Notes**

- The big integer has about m³ bits and its fifth power about 5m³, so the
  program prints 100 terms in about 15 s and 128 in a minute. The bar is
  100 terms in 60 s; the b-file has 10 001.
- J. C. P. Miller's recurrence for powers of a series gives
  n·a(n) = Σ_{j≥1, j²≤n} 2(6j² − n)·a(n − j²). As a program it prints the
  whole b-file in about 4 s, but it is 96 bytes:
  `a=[1];n=0` / `while[print(a[n])]:n+=1;a+=2*sum((6*j*j-n)*a[n-j*j]for j in range(1,n+1)if j*j<=n)//n,`

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000132), CC BY-SA 4.0.
