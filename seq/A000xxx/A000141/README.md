# A000141

> Number of ways of writing n as a sum of 6 squares.
> — [OEIS A000141](https://oeis.org/A000141)

Offset 0: 1, 12, 60, 160, 252, 312, 544, 960, 1020, 876, 1560, 2400, 2080, 2040, 3264, 4160, …

### Python 3 — 74 bytes

```python
m=6
while[print(sum(1<<j*j*m+m for j in range(-m,m))**6>>m*m&2**m-1)]:m+=1
```

**How it works**

- Signs and order count, so a(n) is the coefficient of qⁿ in θ(q)⁶ with
  θ(q) = Σ_{j∈ℤ} q^(j²).
- The program evaluates the series at q = 2^m, so every coefficient becomes
  an m-bit digit of one big integer. `1<<j*j*m+m` is 2^(m(j²+1)), so the
  sum is 2^m·θ(2^m), cut to |j| ≤ m. That keeps every j with j² ≤ n; larger
  |j| only adds to digits above n.
- After the sixth power the number is 2^(6m)·θ⁶, so a(k) sits in digit
  k + 6. `>>m*m&2**m-1` reads digit m, which is a(m − 6), and starting at
  m = 6 prints a(0) first.
- This is the [A000132](../A000132/) program (five squares) with both 5s
  turned into 6s.

**Why the digits never carry**

All coefficients are ≥ 0, so digits at and below m are exact as long as each
is below 2^m. Digit d ≤ m holds a(d − 6), so it is enough that
a(k) < 2^(k+6) for every k:

- for k < 12 this is checked directly (a(11) = 2400 < 2¹⁷);
- for k ≥ 12, each of the six numbers has |x| ≤ √k, so
  a(k) ≤ (2√k + 1)⁶. This is below 2^(k+6) at k = 12, and
  6·log₂(2√k + 1) grows by less than 1 per step for k ≥ 4, so the bound
  holds from there on.

Digits above m (from the cut-off |j| ≤ m terms) can be anything; the mask
drops them and carries only move upward.

**Notes**

- The big integer has about m³ bits and its sixth power about 6m³, so the
  program prints 100 terms in about 25 s and 119 in a minute. The bar is
  100 terms in 60 s; the b-file has 10 001.
- Jacobi's formula a(n) = Σ_{d|n} d²·(16χ(n/d) − 4χ(d)) for n ≥ 1, with χ
  the non-principal character mod 4, is fast but needs χ spelled out
  (`x%2*(2-x%4)`) twice and a special case for n = 0, so it is 102 bytes:
  `n=0` / `while[print(sum(d*d*4*(4*(n//d%2*(2-n//d%4))-d%2*(2-d%4))for d in range(1,n+1)if n%d<1)or 1)]:n+=1`

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000141), CC BY-SA 4.0.
