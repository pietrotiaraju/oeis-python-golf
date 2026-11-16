# A001794

> Negated coefficients of Chebyshev T polynomials: [x^n](-T(n+6, x)), n >= 0.
> — [OEIS A001794](https://oeis.org/A001794)

Offset 0: 1, 7, 32, 120, 400, 1232, 3584, 9984, 26880, 70400, 180224, 452608, …

### Python 3 — 43 bytes

```python
m=1
while[print((m*-~m*(m+5)<<m)//24)]:m+=1
```

**How it works**

- The Chebyshev polynomials have the explicit form
  T(N, x) = (N/2)·Σₖ (−1)ᵏ (N − k − 1)!/(k!(N − 2k)!)·(2x)ᴺ⁻²ᵏ for N ≥ 1,
  k = 0, …, ⌊N/2⌋. For N = n + 6 the power xⁿ comes from k = 3, with
  coefficient −((n + 6)/2)·(n + 2)!/(3!·n!)·2ⁿ. Negated,
  a(n) = (n + 1)(n + 2)(n + 6)·2ⁿ/12, the formula
  2ⁿ⁻²(n + 1)(n + 2)(n + 6)/3 on the OEIS page.
- The loop runs over m = n + 1, from 1. Then
  a(n) = m(m + 1)(m + 5)·2ᵐ/24: `-~m` is m + 1, `<<m` multiplies by 2ᵐ and
  `//24` divides. a(n) is an integer (a coefficient of an integer
  polynomial), so the floor division is exact. The parentheses are needed
  because `//` binds tighter than `<<`.

**Notes**

- `m*-~m*(m+5)//3<<m>>3` and m = n + 2 with `(~-m*m*(m+4)<<m)//48` are
  the same length; in n itself the product costs 4 bytes more.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001794), CC BY-SA 4.0.
