# A001932

> Sum of Fibonacci (A000045) and Pell (A000129) numbers.
> — [OEIS A001932](https://oeis.org/A001932)

Offset 0: 0, 2, 3, 7, 15, 34, 78, 182, 429, 1019, 2433, 5830, 14004, 33694, 81159, …

### Python 3 — 51 bytes

```python
a=c=0;b=d=1
while[print(a+c)]:a,b,c,d=b,a+b,d,c+2*d
```

**How it works**

- `a`, `b` run through consecutive Fibonacci numbers F(n), F(n + 1) and `c`,
  `d` through consecutive Pell numbers P(n), P(n + 1), with
  F(n + 2) = F(n + 1) + F(n) and P(n + 2) = 2P(n + 1) + P(n); each pass
  prints F(n) + P(n) and steps both pairs in one tuple assignment.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The sum satisfies a(n) = 3a(n − 1) − 3a(n − 3) − a(n − 4), since
  (1 − x − x²)(1 − 2x − x²) = 1 − 3x + 3x³ + x⁴, but the four starting terms
  cost more: 54 bytes. Two walrus pairs from `a=b=c=d=1`,
  `print((a:=b-a)+(c:=d-c))`, are 53.
- The b-file has 502 terms (n = 0 to 501); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001932), CC BY-SA 4.0.
