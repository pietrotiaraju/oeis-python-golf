# A001621

> a(n) = n*(n + 1)*(n^2 + n + 2)/4.
> — [OEIS A001621](https://oeis.org/A001621)

Offset 0: 0, 2, 12, 42, 110, 240, 462, 812, 1332, 2070, 3080, 4422, 6162, …

### Python 3 — 35 bytes

```python
t=k=0
while[print(t*t+t)]:k+=1;t+=k
```

**How it works**

- n(n+1) is even, so t = n(n+1)/2 is the n-th triangular number and
  n(n+1)(n²+n+2)/4 = (2t)(2t+2)/4 = t(t+1). The program prints `t*t+t`.
- `t` runs through the triangular numbers by adding 1, 2, 3, …: `k+=1`
  then `t+=k`, so t = 1 + 2 + … + n after the n-th pass. Both start at 0,
  which gives a(0) = 0.

**Notes**

- The entry is marked "changed"; its data and b-file agree with the name's
  formula, which is what the program follows.
- The direct `(x:=n*n+n)*(x+2)//4` with a counter is 42 bytes, and
  `n*~n*(n*~n-2)//4` is 39; the triangular-number walk saves the
  polynomial.
- Exact integer arithmetic, so the program is right for every n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001621), CC BY-SA 4.0.
