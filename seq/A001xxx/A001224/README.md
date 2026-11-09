# A001224

> If F(n) is the n-th Fibonacci number, then a(2n) = (F(2n+1) + F(n+2))/2 and a(2n+1) = (F(2n+2) + F(n+1))/2.
> — [OEIS A001224](https://oeis.org/A001224)

Offset 1: 1, 2, 2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195, 322, 504, 826, 1309, 2135, 3410, 5545, 8900, 14445, 23256, …

### Python 3 — 58 bytes

```python
x=u=0;y=v=1
while[print(x:=x+y-u),print(y:=y+x)]:u,v=v,u+v
```

**How it works**

- The formula counts compositions of n into parts 1 and 2 up to reversal
  (Burnside): there are F(n+1) of them, and the palindromic ones number
  F(m+2) for n = 2m (any left half) and F(m+1) for n = 2m+1 (the middle
  part is 1). So a(n) = (F(n+1) + P(n))/2 with P(n) the palindromic count.
- Hence a(2m+1) = a(2m) + a(2m−1) − F(m): F(n+1) is Fibonacci, and the
  palindromic parts give F(m+1) − F(m+2) − F(m) = −2F(m). And
  a(2m+2) = a(2m+1) + a(2m), where they cancel: F(m+3) − F(m+1) − F(m+2)
  = 0.
- Each pass prints a(2m+1) into `x` and a(2m+2) into `y`, with `u,v` =
  F(m), F(m+1). The start `x=u=0;y=v=1` is a(−1) = 0, a(0) = 1, F(0),
  F(1).

**Notes**

- The whole b-file (500 terms) prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001224), CC BY-SA 4.0.
