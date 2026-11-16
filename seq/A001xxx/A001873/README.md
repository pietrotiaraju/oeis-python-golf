# A001873

> Convolved Fibonacci numbers.
> — [OEIS A001873](https://oeis.org/A001873)

Offset 0: 1, 5, 20, 65, 190, 511, 1295, 3130, 7285, 16435, 36122, 77645, …

### Python 3 — 53 bytes

```python
a=n=0;b=1
while[print(b)]:n+=1;a,b=b,a+b+4*(2*a+b)//n
```

**How it works**

- The generating function is A = 1/(1 − x − x²)⁵ (the data start 1, 5, …,
  the coefficients from x⁰ on). Differentiating,
  A′ = 5(1 + 2x)·A/(1 − x − x²), so (1 − x − x²)A′ = 5(1 + 2x)A. The
  coefficient of xⁿ⁻¹ on both sides gives, for n ≥ 1 (with a(−1) = 0),
  n·a(n) = (n + 4)·a(n−1) + (n + 8)·a(n−2).
- Splitting off n(a(n−1) + a(n−2)) leaves
  a(n) = a(n−1) + a(n−2) + 4(2a(n−2) + a(n−1))/n, and that last quotient
  is an integer because everything else in the identity is: so `//n` is
  exact.
- `a`, `b` hold a(n−2), a(n−1); they start at a(−1) = 0, a(0) = 1. The
  same template, with the factor k − 1 for 1/(1 − x − x²)^k, gives
  [A001628](../A001628/) (k = 3) and A001872–A001875 (k = 4 … 7).

**Notes**

- Two variables and a counter beat the order-10 linear recurrence and the
  closed forms with Fibonacci numbers times a polynomial in n.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001873), CC BY-SA 4.0.
