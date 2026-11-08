# A000999

> 5-adic valuation of binomial(2*n,n): largest k such that 5^k divides binomial(2*n, n).
> — [OEIS A000999](https://oeis.org/A000999)

Offset 0: 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 2, 2, 1, 1, 1, 2, 2, …

### Python 3 — 54 bytes

```python
m=0
while[print(sum(m//5**k%2for k in range(m)))]:m+=2
```

**How it works**

- Legendre's formula gives a(n) = Σ_{k≥1} (⌊2n/5ᵏ⌋ − 2⌊n/5ᵏ⌋). Each term is
  ⌊2x⌋ − 2⌊x⌋ for x = n/5ᵏ, which is 0 or 1 and equals ⌊2x⌋ mod 2. So
  a(n) = Σₖ (⌊2n/5ᵏ⌋ mod 2): the number of k with n mod 5ᵏ above 5ᵏ/2,
  also the number of carries in n + n in base 5 (Kummer).
- `m` = 2n runs over 0, 2, 4, …, and `m//5**k%2` is the k-th term. The
  term k = 0 is m mod 2 = 0, and every k with 5ᵏ > m adds 0, so
  `range(m)` covers all of them.

**Notes**

- Exact integer arithmetic; only Legendre's formula is used.
- Same program as [A000989](../A000989/) with 5 in place of 3; the
  recursion `f=lambda m:m and m%2+f(m//5)` with `print(f(m))` is 58 bytes.
- 2457 terms in 60 s here; the b-file has 1001 terms (about 2.5 s) and
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000999), CC BY-SA 4.0.
