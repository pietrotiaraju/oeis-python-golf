# A001473

> Number of degree-n permutations of order exactly 4.
> — [OEIS A001473](https://oeis.org/A001473)

Offset 1: 0, 0, 0, 6, 30, 180, 840, 5460, 30996, 209160, 1290960, 9753480, 69618120, …

### Python 3 — 84 bytes

```python
a=b=c=d=e=f=n=1
while[print(d-e)]:a,b,c,d,e,f=b,c,d,d+n*(c+~-n*(n-2)*a),e+n*f,e;n+=1
```

**How it works**

- The divisors of 4 are 1, 2 and 4, so a permutation has order exactly 4
  when its order divides 4 but not 2:
  a(n) = [A001472](../A001472/)(n) − [A000085](../A000085/)(n).
- F(n) = A001472(n): cycles of length 1, 2, 4, so
  F(n+1) = F(n) + n·F(n−1) + n(n−1)(n−2)·F(n−3) (point n+1 fixed, in one
  of n 2-cycles or in one of n(n−1)(n−2) 4-cycles). I(n) = A000085(n):
  I(n+1) = I(n) + n·I(n−1).
- `a`, `b`, `c`, `d` hold F(n−3), …, F(n) and `e`, `f` hold I(n), I(n−1);
  `d+n*(c+~-n*(n-2)*a)` and `e+n*f` are the two right-hand sides. The
  print `d-e` comes first, at n = 1 (the offset).
- At n = 1 the true values are F(0) = F(1) = I(0) = I(1) = 1, and `a`,
  `b` (F(−2), F(−1)) are only multiplied by n(n−1)(n−2) = 0 at n = 1
  and 2, so the whole start is `a=b=c=d=e=f=n=1`.

**Notes**

- Exact integer arithmetic, so the program is right for every n; the
  4300-digit int-to-str limit stops it at about n = 1996.
- The b-file has 565 terms (n = 1 to 565); all of them print in well under
  a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001473), CC BY-SA 4.0.
