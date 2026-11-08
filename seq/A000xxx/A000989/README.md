# A000989

> 3-adic valuation of binomial(2*n, n): largest k such that 3^k divides binomial(2*n, n).
> — [OEIS A000989](https://oeis.org/A000989)

Offset 0: 0, 0, 1, 0, 0, 2, 1, 1, 2, 0, 0, 1, 0, 0, 3, 2, 2, 3, 1, 1, …

### Python 3 — 54 bytes

```python
m=0
while[print(sum(m//3**k%2for k in range(m)))]:m+=2
```

**How it works**

- Legendre's formula gives a(n) = Σ_{k≥1} (⌊2n/3ᵏ⌋ − 2⌊n/3ᵏ⌋) (Cloitre's
  formula in the entry). Each term is ⌊2x⌋ − 2⌊x⌋ for x = n/3ᵏ, which is 0
  or 1 and equals ⌊2x⌋ mod 2. So a(n) = Σₖ (⌊2n/3ᵏ⌋ mod 2): the number of
  k with n mod 3ᵏ above 3ᵏ/2, which is also the number of carries in
  n + n in base 3 (Kummer).
- `m` = 2n runs over 0, 2, 4, …, and `m//3**k%2` is the k-th term. The
  term k = 0 is m mod 2 = 0, and every k with 3ᵏ > m adds 0, so `range(m)`
  covers all of them (m − 1 ≥ log₃ m for m ≥ 2; for m = 0 the sum is
  empty).

**Notes**

- Exact integer arithmetic; only Legendre's formula is used.
- The recursion `f=lambda m:m and m%2+f(m//3)` with `print(f(m))` is
  58 bytes.
- `range(m)` is far longer than needed, so the cost per term grows like
  n: 2881 terms in 60 s here, the whole b-file (2001 terms) in about 18 s.
  The bar is the whole b-file in 60 s.
- [A000999](../A000999/) is the same program with 5 in place of 3.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000989), CC BY-SA 4.0.
