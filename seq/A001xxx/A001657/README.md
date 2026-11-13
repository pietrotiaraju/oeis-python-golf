# A001657

> Fibonomial coefficients: column 5 of A010048.
> — [OEIS A001657](https://oeis.org/A001657)

Offset 0: 1, 8, 104, 1092, 12376, 136136, 1514513, 16776144, 186135312, …

### Python 3 — 44 bytes

```python
a=1;b=2
while[print((b**5-b)//30)]:a,b=b,a+b
```

**How it works**

- a(n) = C(n+5, 5)_F = F(n+1)···F(n+5)/(1·1·2·3·5), the Fibonomial
  coefficient (column 5 of A010048).
- With m = n + 3, Catalan's identity F(m−r)F(m+r) = F(m)² − (−1)^(m−r)F(r)²
  gives F(m−1)F(m+1) = F(m)² + (−1)^m and F(m−2)F(m+2) = F(m)² − (−1)^m,
  so the four outer factors multiply to F(m)⁴ − 1 and the product of the
  five is F(m)⁵ − F(m) (Gary Detlefs's formula on the OEIS page).
- `b` is F(n+3) (the pair starts at F(2), F(3) = 1, 2); each pass prints
  (b⁵ − b)/30, exact since a(n) is an integer.

**Notes**

- Folding the Fibonacci step into the print (`((b:=a+b)**5-b)//30` then
  `a=b-a`) is 45 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001657), CC BY-SA 4.0.
