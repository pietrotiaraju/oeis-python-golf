# A000910

> a(n) = 5*binomial(n, 6).
> — [OEIS A000910](https://oeis.org/A000910)

Offset 0: 0, 0, 0, 0, 0, 0, 5, 35, 140, 420, 1050, 2310, 4620, 8580, 15015, …

### Python 3 — 49 bytes

```python
n=0
while[print(5*(4**n+1)**n>>12*n&4**n-1)]:n+=1
```

**How it works**

- The binomial digit trick of [A000579](../A000579/), with the factor 5
  folded in: with B = 4ⁿ, 5·(B+1)ⁿ = Σₖ 5·C(n,k)·Bᵏ, and the program reads
  its base-B digit number 6 (`>>12*n` divides by B⁶, `&4**n-1` keeps one
  digit).
- That digit is exactly 5·C(n,6) for every n: the lower part
  5·Σ_{k<6} C(n,k)Bᵏ is below 5·2ⁿ·B⁵ < B⁶ once n ≥ 3, so nothing carries
  into digit 6 (for n = 1, 2 the whole number is below B⁶, and for n = 0
  the mask is 0), and
  5·C(n,6) < 5·2ⁿ < B fits in one digit.
- Base 2ⁿ as in [A000579](../A000579/) would need parentheses around the
  digit before multiplying by 5 (50 bytes); `import math` and
  `5*math.comb(n,6)` is 51.

**Notes**

- Exact integer arithmetic, correct for every n.
- (4ⁿ+1)ⁿ has 2n² bits, so the program slows down: about 1125 terms in
  60 s on the test PC (900 in 25 s, 1001 in 39 s). The b-file has 1001
  terms (up to a(1000)); the bar is 900 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000910), CC BY-SA 4.0.
