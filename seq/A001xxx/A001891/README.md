# A001891

> Hit polynomials; convolution of natural numbers with Fibonacci numbers F(2), F(3), F(4), ....
> — [OEIS A001891](https://oeis.org/A001891)

Offset 0: 0, 1, 4, 10, 21, 40, 72, 125, 212, 354, 585, 960, 1568, 2553, …

### Python 3 — 42 bytes

```python
a=n=5;b=8
while[print(a-n)]:a,b=b,a+b;n+=2
```

**How it works**

- The generating function is x(1 + x)/((1 − x)²(1 − x − x²)), and
  x(1 + x)/(1 − x)² = Σ (2n − 1)·xⁿ (n ≥ 1), so
  a(n) = a(n−1) + a(n−2) + 2n − 1 for n ≥ 1, with a(−1) = a(0) = 0.
- b(n) = F(n + 5) − (2n + 5) satisfies the same recurrence,
  −(2n + 5) + (2n + 3) + (2n + 1) = 2n − 1, and b(−1) = 3 − 3 = 0,
  b(0) = 5 − 5 = 0. So a(n) = F(n + 5) − (2n + 5) (W. Lang's formula on the
  OEIS page).
- `a`, `b` step through F(n + 5), F(n + 6) from F(5) = 5, F(6) = 8, and `n`
  holds 2n + 5, which also starts at 5.

**Notes**

- The recurrence itself, `a,b=b,a+b+n+1` with `n+=2`, is 44 bytes, and so is
  the running sum of F(n + 3) − 2.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001891), CC BY-SA 4.0.
