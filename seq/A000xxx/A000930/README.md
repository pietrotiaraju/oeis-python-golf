# A000930

> Narayana's cows sequence: a(0) = a(1) = a(2) = 1; thereafter a(n) = a(n-1) + a(n-3).
> — [OEIS A000930](https://oeis.org/A000930)

Offset 0: 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, …

### Python 3 — 37 bytes

```python
a=b=c=1
while[print(a)]:a,b,c=b,c,a+c
```

**How it works**

- (a, b, c) holds three consecutive terms (a(t), a(t+1), a(t+2)); the
  tuple shift `a,b,c=b,c,a+c` appends a(t+3) = a(t+2) + a(t). The start
  1, 1, 1 is one chain `a=b=c=1`.

**Notes**

- A search over chains of three in-place statements (`x=…`, `x+=…`, `x-=…`
  with coefficients −1, 0, 1, and 2 on the variable itself) found 42 bytes
  at best, a walrus update inside the print plus a two-variable tuple 40,
  and three-variable tuples of other linear forms tie at 37.
- Exact integer arithmetic.
- The b-file has 5001 terms; they print in about 0.2 s here. The bar is
  the whole b-file in 60 s. a(25904) is the first term with more than 4300
  digits, so printing stops there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000930), CC BY-SA 4.0.
