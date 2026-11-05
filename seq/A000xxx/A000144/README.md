# A000144

> Number of ways of writing n as a sum of 10 squares.
> — [OEIS A000144](https://oeis.org/A000144)

Offset 0: 1, 20, 180, 960, 3380, 8424, 16320, 28800, 52020, 88660, 129064, 175680, 262080, 386920, 489600, 600960, …

### Python 3 — 76 bytes

```python
m=10
while[print(sum(1<<j*j*m+m for j in range(-m,m))**10>>m*m&2**m-1)]:m+=1
```

**How it works**

- Signs and order count, so a(n) is the coefficient of qⁿ in θ(q)¹⁰ with
  θ(q) = Σ_{j∈ℤ} q^(j²).
- The program evaluates the series at q = 2^m, so every coefficient becomes
  an m-bit digit of one big integer. `1<<j*j*m+m` is 2^(m(j²+1)), so the
  sum is 2^m·θ(2^m), cut to |j| ≤ m. That keeps every j with j² ≤ n; larger
  |j| only adds to digits above n.
- After the tenth power the number is 2^(10m)·θ¹⁰, so a(k) sits in digit
  k + 10. `>>m*m&2**m-1` reads digit m, which is a(m − 10), and starting at
  m = 10 prints a(0) first.
- This is the [A000132](../A000132/) program (five squares) with the power
  and the start changed from 5 to 10, which costs 2 bytes.

**Why the digits never carry**

All coefficients are ≥ 0, so digits at and below m are exact as long as each
is below 2^m. Digit d ≤ m holds a(d − 10), so it is enough that
a(k) < 2^(k+10) for every k:

- for k < 25 this is checked directly (the tightest case is
  a(5) = 8424 < 2¹⁵);
- for k ≥ 25, each of the ten numbers has |x| ≤ √k, so
  a(k) ≤ (2√k + 1)¹⁰. This is below 2^(k+10) at k = 25 (11¹⁰ < 2³⁵), and
  10·log₂(2√k + 1) grows by less than 1 per step for k ≥ 7, so the bound
  holds from there on.

Digits above m (from the cut-off |j| ≤ m terms) can be anything; the mask
drops them and carries only move upward.

**Notes**

- The big integer has about m³ bits and its tenth power about 10m³, so the
  program prints 95 terms in a minute and 100 in about 95 s. The bar is
  75 terms in 60 s; the b-file has 10 001.
- J. C. P. Miller's recurrence for powers of a series gives
  n·a(n) = Σ_{j≥1, j²≤n} 2(11j² − n)·a(n − j²). As a program it prints the
  whole b-file in about 7 s, but it is 97 bytes:
  `a=[1];n=0` / `while[print(a[n])]:n+=1;a+=2*sum((11*j*j-n)*a[n-j*j]for j in range(1,n+1)if j*j<=n)//n,`

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000144), CC BY-SA 4.0.
