# A000919

> a(n) = 4^n - C(4,3)*3^n + C(4,2)*2^n - C(4,1).
> — [OEIS A000919](https://oeis.org/A000919)

Offset 1: 0, 0, 0, 24, 240, 1560, 8400, 40824, 186480, 818520, 3498000, 14676024, …

### Python 3 — 42 bytes

```python
n=1
while[print(4**n+6*2**n+~3**n*4)]:n+=1
```

**How it works**

- The formula of the name, 4ⁿ − 4·3ⁿ + 6·2ⁿ − 4 (for n ≥ 1 it is
  24·S(n, 4), the number of maps of an n-set onto a 4-set).
- `~3**n*4` is (−3ⁿ − 1)·4 = −4·3ⁿ − 4: the complement absorbs the
  constant, one byte under `-4*3**n-4`. `**` binds tighter than the unary
  `~` on its left, so no parentheses are needed.

**Notes**

- Other versions: the plain formula `4**n-4*3**n+6*2**n-4` is 43 bytes.
  The staggered Stirling loop of [A000453](../A000453/) also works for
  24·S(n, 4) from n = 1 if the three diagonals are extended by their closed
  forms: with c = 3·2ⁿ − 24 and b = 4·3ⁿ⁻¹ − 6·2ⁿ + 12,
  `a=0;b=4;c=-18` / `while[print(a)]:c+=c+24;b=3*b+c;a=4*a+b` is 53 bytes.
- Exact integer arithmetic.
- The b-file has 201 terms; they print at once. The bar is the whole
  b-file in 60 s. a(7143) is the first term with more than 4300 digits, so
  printing stops there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000919), CC BY-SA 4.0.
