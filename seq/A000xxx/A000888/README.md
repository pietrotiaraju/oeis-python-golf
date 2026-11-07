# A000888

> a(n) = (2*n)!^2 / ((n+1)!*n!^3).
> — [OEIS A000888](https://oeis.org/A000888)

Offset 0: 1, 2, 12, 100, 980, 10584, 121968, 1472328, 18404100, 236390440, …

### Python 3 — 44 bytes

```python
b=n=1
while[print(b*b//n)]:b=4*b-2*b//n;n+=1
```

**How it works**

- a(n) = C(2n,n)²/(n+1) (an OEIS formula): (2n)!²/(n!⁴) · n!/(n+1)!.
- The counter `n` is one more than the index k, and `b` is C(2k,k), so the
  print is `b*b//n`. The quotient is exact: it is C(2k,k)·C_k with C_k the
  Catalan number C(2k,k)/(k+1).
- Next binomial: C(2k+2,k+1) = C(2k,k)·(4k+2)/(k+1) = 4b − 2b/n, and 2b/n
  = 2C_k is an integer, so `b=4*b-2*b//n` is exact and 2 bytes shorter
  than `b=b*(4*n-2)//n`.
- At the start k = 0: b = C(0,0) = 1 and n = 1, so `b=n=1`.
- Carrying the Catalan number instead, a(k) = (k+1)·C_k², is
  `c=n=1` / `while[print(n*c*c)]:c=4*c-6*c//-~n;n+=1`, one byte longer.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 3578, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000888), CC BY-SA 4.0.
