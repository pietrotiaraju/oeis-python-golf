# A000143

> Number of ways of writing n as a sum of 8 squares.
> — [OEIS A000143](https://oeis.org/A000143)

Offset 0: 1, 16, 112, 448, 1136, 2016, 3136, 5504, 9328, 12112, 14112, 21312, …

### Python 3 — 74 bytes

```python
m=8
while[print(sum(1<<j*j*m+m for j in range(-m,m))**8>>m*m&2**m-1)]:m+=1
```

**How it works**

- Signs and order count, so a(n) is the coefficient of qⁿ in θ(q)⁸ with
  θ(q) = Σ_{j∈ℤ} q^(j²). This is the program of
  [A000132](../A000132/) (5 squares) with the power and the start changed.
- The program evaluates the series at q = 2^m, so every coefficient becomes
  an m-bit digit of one big integer. `1<<j*j*m+m` is 2^(m(j²+1)), so the
  sum is 2^m·θ(2^m), cut to |j| ≤ m. That keeps every j with j² ≤ n; the
  missing terms only add to digits m² + 8 and up.
- After the eighth power the number is 2^(8m)·θ⁸, so a(k) sits in digit
  k + 8. `>>m*m&2**m-1` reads digit m, which is a(m − 8), and starting at
  m = 8 prints a(0) first.

**Why the digits never carry**

All coefficients are ≥ 0, so digits at and below m are exact as long as each
is below 2^m. Digit d ≤ m holds a(d − 8), so it is enough that
a(k) < 2^(k+8) for every k. Jacobi's formula
a(k) = 16 Σ_{d|k} (−1)^(k+d) d³ (k ≥ 1) gives

a(k) ≤ 16 σ₃(k) = 16 k³ Σ_{d|k} d⁻³ < 16 ζ(3) k³ < 19.3 k³,

and 19.3 k³ < 256·2^k because k³/2^k never exceeds 4 (its maximum, at
k = 4). Digits above m can be anything; the mask drops them and carries only
move upward.

**Notes**

- The big integer has about m³ bits and its eighth power about 8m³, so the
  program prints 80 terms in about 13 s and 108 in a minute. The bar is
  80 terms in 60 s; the b-file has 10 001.
- Jacobi's divisor sum as a program prints the whole b-file in seconds, but
  it is 80 bytes (`or 1` supplies a(0), since every a(n) with n ≥ 1 is
  positive): `n=0` /
  `while[print(16*sum((-1)**(n+d)*d**3for d in range(1,n+1)if n%d<1)or 1)]:n+=1`

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000143), CC BY-SA 4.0.
