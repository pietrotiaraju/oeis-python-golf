# A000891

> a(n) = (2*n)!*(2*n+1)! / (n! * (n+1)!)^2.
> — [OEIS A000891](https://oeis.org/A000891)

Offset 0: 1, 3, 20, 175, 1764, 19404, 226512, 2760615, 34763300, 449141836, …

### Python 3 — 45 bytes

```python
c=m=1
while[print(m*c*c)]:c=c*4*m//(m+3);m+=2
```

**How it works**

- Split the factorials: (2n)!/(n!(n+1)!) is the Catalan number C_n, and
  (2n+1)!/(n!(n+1)!) = (2n+1)·C_n, so a(n) = (2n+1)·C_n².
- `m` is 2n+1 and `c` is C_n, so the print is `m*c*c`.
- Next Catalan number: C_{n+1} = C_n·2(2n+1)/(n+2) = c·4m/(m+3), and since
  the quotient is the integer C_{n+1}, `c*4*m//(m+3)` is exact. Then `m+=2`.
- At n = 0 both are 1: `c=m=1`.
- The OEIS form a(n) = C(2n+2,n+1)·C_n/2, with the central binomial
  carried by `b=4*b-2*b//n`, is 48 bytes:
  `b=n=1` / `while[print(b*(b:=4*b-2*b//n)//n//2)]:n+=1`.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 3578, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000891), CC BY-SA 4.0.
