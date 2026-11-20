# A001911

> a(n) = Fibonacci(n+3) - 2.
> — [OEIS A001911](https://oeis.org/A001911)

Offset 0: 0, 1, 3, 6, 11, 19, 32, 53, 87, 142, 231, 375, 608, 985, 1595, 2582, 4179, …

### Python 3 — 34 bytes

```python
a=b=-1
while[print(a:=b-a)]:b+=a+2
```

**How it works**

- a(n) = F(n + 3) − 2 satisfies a(n + 1) = a(n) + a(n − 1) + 2, because
  F(n + 4) = F(n + 3) + F(n + 2) and −2 = −2 − 2 + 2.
- Call the printed values x₀, x₁, … and the value of `b` after pass n bₙ.
  The program sets xₙ₊₁ = bₙ − xₙ and bₙ = bₙ₋₁ + xₙ + 2. As
  xₙ = bₙ₋₁ − xₙ₋₁, this gives xₙ₊₁ = bₙ₋₁ + 2 = xₙ + xₙ₋₁ + 2: the same
  recurrence.
- The start `a=b=-1` gives x₀ = −1 − (−1) = 0 = F(3) − 2, b₀ = 1 and
  x₁ = 1 = F(4) − 2, so xₙ = a(n) for every n.

**Notes**

- The constant has to sit in `b`'s update (with `a:=b-a+c` the recurrence
  keeps whatever `b` adds); the pair update `a=0;b=1` /
  `a,b=b,a+b+2` is 35 bytes.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at about n = 20575.
- The b-file has 4784 terms (n = 0 to 4783); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001911), CC BY-SA 4.0.
