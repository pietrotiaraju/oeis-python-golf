# A001308

> Order of Chevalley group D_n (2).
> — [OEIS A001308](https://oeis.org/A001308)

Offset 1: 1, 36, 20160, 174182400, 23499295948800, 50027557148216524800, …

The entry gives a(n) = 2^(n(n−1)) · (2ⁿ − 1) · ∏_{i=1..n−1} (4ⁱ − 1), the
order formula q^(n(n−1)) (qⁿ − 1) ∏ (q^(2i) − 1) / gcd(4, qⁿ − 1) of
D_n(q) at q = 2, where the gcd is 1. For example a(2) = 36 = |S₃ × S₃|
and a(3) = 20160 = |A₈|.

### Python 3 — 45 bytes

```python
a=x=1
while[print(a)]:x*=2;a*=x*x*(2*x*x+x-1)
```

**How it works**

- From the formula, a(n+1)/a(n) = 2^(2n) · (2ⁿ⁺¹ − 1)/(2ⁿ − 1) · (4ⁿ − 1),
  and 4ⁿ − 1 = (2ⁿ − 1)(2ⁿ + 1), so the ratio is the integer
  2^(2n) (2ⁿ⁺¹ − 1)(2ⁿ + 1). With x = 2ⁿ that is x²(2x − 1)(x + 1)
  = x²(2x² + x − 1).
- `a` starts at a(1) = 1 and `x` at 1. Each step first doubles `x` to 2ⁿ
  and then multiplies `a` by x²(2x² + x − 1), turning a(n) into a(n+1):
  x = 2 gives 4 · 9 = 36, x = 4 gives 36 · 16 · 35 = 20160. All of it is
  exact integer arithmetic, so every term is right.
- `print(…)` runs in the loop condition: it returns `None`, and `[None]`
  is a non-empty list, so the loop never ends.

**Notes**

- `x*x*-~x*(x+x-1)` is the same length as `x*x*(2*x*x+x-1)`. Multiplying
  before doubling needs `a=1` and `x=2` set apart (+2 bytes). Printing
  the product as it is formed, with `(x|1)` standing for x + 1 so that the
  first factor is 1 at x = 1, is 48 bytes:
  `a=x=1` / `while 1:print(a:=a*x*x*(x|1)*(2*x-1));x*=2`.
- The terms grow like 2^(n(2n−1)): the program prints a(1) to a(84) (4223
  digits) and then stops with a `ValueError` at the interpreter's
  4300-digit int-to-str limit.
- The b-file has 20 terms (n = 1 to 20); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001308), CC BY-SA 4.0.
