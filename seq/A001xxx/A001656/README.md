# A001656

> Fibonomial coefficients.
> — [OEIS A001656](https://oeis.org/A001656)

Offset 0: 1, 5, 40, 260, 1820, 12376, 85085, 582505, 3994320, 27372840, …

### Python 3 — 48 bytes

```python
a=1;b=2
while[print(a*b*(b*b-a*a)//6)]:a,b=b,a+b
```

**How it works**

- a(n) = C(n+4, 4)_F = F(n+1)F(n+2)F(n+3)F(n+4)/(1·1·2·3), the Fibonomial
  coefficient (column 4 of A010048, as the formula section says).
- `a`, `b` hold F(n+2), F(n+3). The outer factors are
  F(n+1) = b − a and F(n+4) = a + b, so F(n+1)F(n+4) = b² − a² and the
  product of the four is `a*b*(b*b-a*a)`, divided by 6.
- The division is exact because a(n) is an integer (the Fibonomial
  coefficients are integers; here, the product of four consecutive
  Fibonacci numbers always has the factor 6).

**Notes**

- A list window with one division per term (`a(n) = a(n−1)·F(n+4)/F(n)`)
  or the walrus window of [A001655](../A001655/) with
  `a*b*(b:=a+b)*(b+b-a)//6` are both longer (49 bytes and up).
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001656), CC BY-SA 4.0.
