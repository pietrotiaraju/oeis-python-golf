# A000431

> Expansion of 2*x^3/((1-2*x)^2*(1-4*x)).
> — [OEIS A000431](https://oeis.org/A000431)

Offset 0: 0, 0, 0, 2, 16, 88, 416, 1824, 7680, 31616, …

### Python 3 — 42 bytes

```python
n=0
while 1:print(2**n*(2**n-2*n)//8);n+=1
```

**How it works**

- Partial fractions of the rational generating function give
  a(n)=(4ⁿ−n·2^(n+1))/8 for n≥1. Factoring out 2ⁿ yields
  `2**n*(2**n-2*n)//8`.
- For n≥3, the factor 2ⁿ is itself divisible by 8. At n=1 and
  n=2 the other factor is zero, giving the two remaining initial zeros
  with an exact division.
- At n=0 the numerator is 1, so floor division gives 0 rather than
  1/8. This supplies the exceptional constant coefficient without a
  conditional or a separate print.
- The loop starts at n=0 and increments after printing. At n=3 the
  expression is 8·(8−6)/8=2, the first nonzero coefficient of a
  generating function with a factor x³.

**Notes**

- Integer powers and floor division are exact here. Only the n=0
  quotient is deliberately inexact as a rational number, and its
  integer result is the required initial zero.
- The direct expression needs no recurrence history or stored powers.
  Carrying 2ⁿ and 4ⁿ between iterations trades exponentiation for
  additional variables and updates.
- Growth is on the scale of 4ⁿ. Python 3.11+ eventually reaches its
  default 4300-digit integer-to-string limit, an interpreter limit
  rather than a failure of the coefficient formula.
- The b-file has 201 terms (indices 0 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000431), CC BY-SA 4.0.
