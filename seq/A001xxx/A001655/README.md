# A001655

> Fibonomial coefficients: a(n) = F(n+1) * F(n+2) * F(n+3)/2, where F() = Fibonacci numbers A000045.
> — [OEIS A001655](https://oeis.org/A001655)

Offset 0: 1, 3, 15, 60, 260, 1092, 4641, 19635, 83215, 352440, 1493064, …

### Python 3 — 41 bytes

```python
a=b=1
while[print(a*b*(b:=a+b)//2)]:a=b-a
```

**How it works**

- `a`, `b` hold F(n+1), F(n+2). Inside the print, `(b:=a+b)` is the third
  factor F(n+3) and also stores it, so the product F(n+1)F(n+2)F(n+3) is
  printed halved (one of three consecutive Fibonacci numbers is even, so
  `//2` is exact).
- After the print, `b` is already F(n+3) and `a=b-a` gives
  F(n+3) − F(n+1) = F(n+2): the window has moved without a tuple swap.
- These are the Fibonomial coefficients C(n+3, 3)_F =
  F(n+1)F(n+2)F(n+3)/(F(1)F(2)F(3)).

**Notes**

- The plain `a,b=b,a+b` with `print(a*b*(a+b)//2)` is 42 bytes.
- For the next columns, [A001656](../A001656/), [A001657](../A001657/) and
  [A001658](../A001658/), Fibonacci product identities beat the walrus
  window.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001655), CC BY-SA 4.0.
