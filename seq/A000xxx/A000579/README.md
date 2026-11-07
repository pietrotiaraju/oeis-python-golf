# A000579

> Figurate numbers or binomial coefficients C(n,6).
> — [OEIS A000579](https://oeis.org/A000579)

Offset 0: 0, 0, 0, 0, 0, 0, 1, 7, 28, 84, …

### Python 3 — 46 bytes

```python
n=0
while[print((2**n+1)**n>>6*n&2**n-1)]:n+=1
```

**How it works**

- **Binomials as digits.** With B = 2ⁿ, (B + 1)ⁿ = Σ_k C(n, k)·B^k. For
  n ≥ 1 every C(n, k) is below B, since the n + 1 coefficients are positive
  and add up to 2ⁿ. So there are no carries, and the base-B digits of
  (B + 1)ⁿ are exactly C(n, 0), …, C(n, n).
- **Reading digit 6.** `>>6*n` drops the digits for k < 6 and `&2**n-1`
  keeps the next one, C(n, 6). For n < 6 the power has no digit 6 and the
  result is 0, so the six leading zeros need no special case; at n = 0 the
  mask 2⁰ − 1 is 0 as well.
- Precedence does the grouping: `**` and `*` before `+`/`-`, then `>>`,
  then `&`, so this is ((B + 1)ⁿ >> 6n) & (B − 1).

**Notes**

- Other versions that print the same terms: `import math` with
  `math.comb(n,6)`: 49 bytes (50 with `from math import*`); the same digit
  read with a modular power, `pow(2**n+1,n,2**(7*n))>>6*n`: 50 bytes and
  50 times faster. The multiplicative step of [A000580](../A000580/) cannot
  start from the zeros.
- Exact integer arithmetic, so the program is right for every n.
- The n-th term builds an n²-bit power: the whole b-file takes about 25 s
  here. The b-file has 1001 terms (up to a(1000)); the bar is the whole
  b-file in 60 s.
- a(n) < n⁶, so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-07 | Python 3 | 46 | digit 6 of (2ⁿ + 1)ⁿ in base 2ⁿ, no import |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000579), CC BY-SA 4.0.
