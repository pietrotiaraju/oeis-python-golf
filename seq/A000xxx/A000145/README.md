# A000145

> Number of ways of writing n as a sum of 12 squares.
> — [OEIS A000145](https://oeis.org/A000145)

Offset 0: 1, 24, 264, 1760, 7944, 25872, 64416, 133056, 253704, 472760, 825264, 1297056, 1938336, 2963664, 4437312, 6091584, …

### Python 3 — 76 bytes

```python
m=12
while[print(sum(1<<j*j*m+m for j in range(-m,m))**12>>m*m&2**m-1)]:m+=1
```

**How it works**

- Signs and order count, so a(n) is the coefficient of qⁿ in θ(q)¹² with
  θ(q) = Σ_{j∈ℤ} q^(j²).
- The program evaluates the series at q = 2^m, so every coefficient becomes
  an m-bit digit of one big integer. `1<<j*j*m+m` is 2^(m(j²+1)), so the
  sum is 2^m·θ(2^m), cut to −m ≤ j < m. That keeps every j with j² ≤ n;
  larger |j| only adds to digits above n.
- After the twelfth power the number is 2^(12m)·θ¹², so a(k) sits in digit
  k + 12. `>>m*m&2**m-1` reads digit m, which is a(m − 12), and starting at
  m = 12 prints a(0) first. The same trick as
  [A000132](../A000132/) (5 squares), where the offset happens to be 5.

**Why the digits never carry**

All coefficients are ≥ 0, so digits at and below m are exact as long as each
is below 2^m. Digit d ≤ m holds a(d − 12), so it is enough that
a(k) < 2^(k+12) for every k:

- for k < 32 this is checked directly (the tightest case is
  a(7) = 133056 < 2¹⁹);
- for k ≥ 32, each of the twelve numbers has |x| ≤ √k, so
  a(k) ≤ (2√k + 1)¹². This is below 2^(k+12) at k = 32, and
  12·log₂(2√k + 1) grows by less than 1 per step for k ≥ 8, so the bound
  holds from there on.

Digits above m (from the cut-off |j| ≤ m terms) can be anything; the mask
drops them and carries only move upward.

**Notes**

- The big integer has about m³ bits and its twelfth power about 12m³, so the
  program prints 70 terms in about 19 s and 88 in a minute. The bar is
  70 terms in 60 s; the b-file has 10 001.
- Reducing before the power, `pow(sum(…),12,1<<m*m+m)>>m*m`, keeps every
  product at m² + m bits and prints 208 terms in a minute, for 82 bytes.
- J. C. P. Miller's recurrence for powers of a series gives
  n·a(n) = Σ_{j≥1, j²≤n} 2(13j² − n)·a(n − j²). As a program it prints the
  whole b-file in about 9 s, but it is 97 bytes:
  `a=[1];n=0` / `while[print(a[n])]:n+=1;a+=2*sum((13*j*j-n)*a[n-j*j]for j in range(1,n+1)if j*j<=n)//n,`

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000145), CC BY-SA 4.0.
