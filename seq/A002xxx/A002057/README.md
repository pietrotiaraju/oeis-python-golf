# A002057

> Fourth convolution of Catalan numbers: a(n) = 4*binomial(2*n+3,n)/(n+4).
> — [OEIS A002057](https://oeis.org/A002057)

Offset 0: 1, 4, 14, 48, 165, 572, 2002, 7072, 25194, 90440, 326876, 1188640, …

### Python 3 — 52 bytes

```python
a=p=1
while[print(a)]:a=a*-~p*(4*p+6)//p//(p+4);p+=1
```

**How it works**

- a(n) = 4·C(2n+3, n)/(n + 4) = 4·(2n + 3)!/(n!·(n + 4)!), so
  a(n)/a(n−1) = (2n + 3)(2n + 2)/(n(n + 4)), written `-~p*(4*p+6)` over
  p·(p + 4) with p = n.
- The whole product is formed before the two floor divisions, and
  ⌊⌊x/p⌋/(p + 4)⌋ = ⌊x/(p(p + 4))⌋, which is exact because a(n) is an
  integer. `a=p=1` starts at a(0) = 1 with p = 1 for the first step.

**Notes**

- `2*math.comb(2*m,m-2)//m` (m = n + 2) with an import is 58 bytes.
- Exact integer arithmetic, so the program is right for every n; a(n) is
  about 4ⁿ, so Python's 4300-digit int-to-str limit stops the output near
  n = 7140.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002057), CC BY-SA 4.0.
