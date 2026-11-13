# A001582

> Product of Fibonacci and Pell numbers.
> — [OEIS A001582](https://oeis.org/A001582)

Offset 0: 1, 2, 10, 36, 145, 560, 2197, 8568, 33490, 130790, 510949, 1995840, …

### Python 3 — 50 bytes

```python
a=b=c=d=1
while[print(a*c)]:a,b=b,a+b;d+=c+c;c=d-c
```

**How it works**

- a(n) = F(n+1)·P(n+1), with F the Fibonacci numbers and P the Pell numbers
  (P(0) = 0, P(1) = 1, P(n) = 2P(n−1) + P(n−2)): the data starts
  1·1, 1·2, 2·5, 3·12, 5·29, …
- `a,b=b,a+b` walks (a, b) = (F(n+1), F(n+2)) from (1, 1).
- For Pell, `c` = P(n+1) and `d` = P(n+1) + P(n) (the companion numbers
  [A001333](../A001333/)). Then `d+=c+c` gives
  P(n+1) + P(n) + 2P(n+1) = P(n+2) + P(n+1), and `c=d-c` leaves
  c = P(n+2). At n = 0 both are 1, so all four variables start at 1.
- The product `a*c` is printed.

**Notes**

- The entry's g.f. (1 − x²)/(1 − 2x − 7x² − 2x³ + x⁴) gives an order-4
  recurrence, but four seeds and four coefficients cost more. The plain
  tuples `a=b=c=1;d=2` / `a,b,c,d=b,a+b,d,c+2*d` are 51 bytes; the start
  with four equal values is what the in-place Pell step buys.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001582), CC BY-SA 4.0.
