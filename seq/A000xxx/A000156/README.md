# A000156

> Number of ways of writing n as a sum of 24 squares.
> — [OEIS A000156](https://oeis.org/A000156)

Offset 0: 1, 48, 1104, 16192, 170064, 1362336, 8662720, 44981376, 195082320, 721175536, 2319457632, 6631997376, …

### Python 3 — 76 bytes

```python
m=24
while[print(sum(1<<j*j*m+m for j in range(-m,m))**24>>m*m&2**m-1)]:m+=1
```

**How it works**

- Signs and order count, so a(n) is the coefficient of qⁿ in θ(q)²⁴ with
  θ(q) = Σ_{j∈ℤ} q^(j²).
- The program evaluates the series at q = 2^m, so every coefficient becomes
  an m-bit digit of one big integer. `1<<j*j*m+m` is 2^(m(j²+1)), so the
  sum is 2^m·θ(2^m), cut to |j| ≤ m. That keeps every j with j² ≤ n; larger
  |j| only adds to digits above n.
- After the 24th power the number is 2^(24m)·θ²⁴, so a(k) sits in digit
  k + 24. `>>m*m&2**m-1` reads digit m, which is a(m − 24), and starting at
  m = 24 prints a(0) first.
- This is the [A000132](../A000132/) program (five squares) with the power
  and the start changed from 5 to 24, the same 2 bytes as
  [A000144](../A000144/) (ten squares).

**Why the digits never carry**

All coefficients are ≥ 0, so digits at and below m are exact as long as each
is below 2^m. Digit d ≤ m holds a(d − 24), so it is enough that
a(k) < 2^(k+24) for every k:

- for k < 78 this is checked directly; it is tight but holds, the closest
  case being a(12) = 17231109824 < 2³⁵, one bit inside 2³⁶;
- for k ≥ 78, each of the 24 numbers has |x| ≤ √k, so
  a(k) ≤ (2√k + 1)²⁴. At k = 78 that is about 2^101.3 < 2^102, and
  24·log₂(2√k + 1) grows by less than 1 per step for k ≥ 16, so the bound
  holds from there on.

Digits above m (from the cut-off |j| ≤ m terms) can be anything; the mask
drops them and carries only move upward.

**Notes**

- The big integer has about m³ bits and its 24th power about 24m³, so the
  program prints 57 terms in a minute. The bar is 45 terms in 60 s; the
  b-file has 10 001.
- J. C. P. Miller's recurrence for powers of a series gives
  n·a(n) = Σ_{j≥1, j²≤n} 2(25j² − n)·a(n − j²). As a program it prints the
  whole b-file in about 6 s, but it is 97 bytes:
  `a=[1];n=0` / `while[print(a[n])]:n+=1;a+=2*sum((25*j*j-n)*a[n-j*j]for j in range(1,n+1)if j*j<=n)//n,`

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000156), CC BY-SA 4.0.
