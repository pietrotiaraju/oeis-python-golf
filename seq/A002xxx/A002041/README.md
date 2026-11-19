# A002041

> Expansion of x/((1-x)(1-4x^2)(1-5x)).
> — [OEIS A002041](https://oeis.org/A002041)

Offset 1: 1, 6, 35, 180, 921, 4626, 23215, 116160, 581141, 2906046, …

### Python 3 — 43 bytes

```python
a=p=q=1
while[print(a)]:a=5*a+q;p,q=q,4*p+1
```

**How it works**

- Write the generating function as x·U(x)/(1 − 5x) with
  U(x) = 1/((1 − x)(1 − 4x²)) = 1 + x + 5x² + 5x³ + 21x⁴ + 21x⁵ + ….
  Then a(n) = 5a(n−1) + u(n−1), and U(x)(1 − 4x²) = 1/(1 − x) gives
  u(n) = 4u(n−2) + 1.
- When a(n) is printed, `p`, `q` hold u(n−1), u(n): the step is
  `a=5*a+q` and `p,q=q,4*p+1`. Everything starts at 1: a(1) = 1 and
  u(0) = u(1) = 1.

**Notes**

- The order-4 recurrence from the denominator,
  a(n) = 6a(n−1) − a(n−2) − 24a(n−3) + 20a(n−4), the order-3 one with a
  constant, and the closed form
  a(n) = (25·5ⁿ − 28·2ⁿ − 4·(−2)ⁿ + 7)/84 are all longer.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops the output near n = 6150.
- The b-file has 1000 terms (n = 1 to 1000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002041), CC BY-SA 4.0.
