# A001803

> Numerators in expansion of (1 - x)^(-3/2).
> — [OEIS A001803](https://oeis.org/A001803)

Offset 0: 1, 3, 15, 35, 315, 693, 3003, 6435, 109395, 230945, 969969, 2028117, …

### Python 3 — 47 bytes

```python
a=n=1
while[print(a)]:a=a*(n-~n)*(n&-n)//n;n+=1
```

**How it works**

- **The series.** (1 − x)^(−3/2) = Σ (2n + 1)·C(2n, n)/4ⁿ·xⁿ = Σ
  (2n + 1)!/(n!²·4ⁿ)·xⁿ. The denominator is a power of 2, so in lowest terms
  the numerator is the odd part of (2n + 1)!/n!². By Legendre's formula its
  2-adic valuation is (2n + 1 − s₂(2n + 1)) − 2(n − s₂(n)) = s₂(n) ≤ 2n
  (s₂ = binary digit sum), so the fraction really reduces to that odd part,
  as in the OEIS formula a(n) = (2n + 1)!/(n!²·2^A000120(n)).
- **A ratio instead of factorials.** (2n + 1)!/n!² grows by 2(2n + 1)/n from
  n − 1 to n, and dividing out 2^s₂(n) instead of 2^s₂(n − 1) multiplies
  that by 2^(s₂(n − 1) − s₂(n)) = 2^(v₂(n) − 1).
  So a(n) = a(n − 1)·(2n + 1)·2^v₂(n)/n = a(n − 1)·(2n + 1)·(n & −n)/n.
- **The program.** `n-~n` is 2n + 1 and `n&-n` the lowest set bit of n. The
  product comes before the floor division and the quotient is the integer
  a(n), so `//` is exact; `n` is advanced after each step, so `a=n=1` starts
  the first step at n = 1.

**Notes**

- Checked against the exact rational binomial series for n < 150, and against
  the b-file.
- Tracking (2n + 1)!/n!² and printing its odd part `c//(c&-c)` is 2 bytes
  longer; `math.comb` with `>>n.bit_count()` is longer still.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 7144.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001803), CC BY-SA 4.0.
