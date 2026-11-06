# A000332

> Binomial coefficient binomial(n,4) = n*(n-1)*(n-2)*(n-3)/24.
> — [OEIS A000332](https://oeis.org/A000332)

Offset 0: 0, 0, 0, 0, 1, 5, 15, 35, 70, 126, 210, 330, 495, 715, 1001, …

### Python 3 — 38 bytes

```python
u=1
while[print((u*~u+1)**2//24)]:u-=1
```

**How it works**

- Pair the four factors from the outside in: n(n−3) = z − 2 and
  (n−1)(n−2) = z with z = (n−1)(n−2). So the product is z(z − 2) =
  (z − 1)² − 1, and binomial(n,4) = ((z − 1)² − 1)/24.
- z − 1 is odd (z is a product of two consecutive integers) and never a
  multiple of 3 (a product of two consecutive integers is 0 or 2 mod 3), so
  (z − 1)² ≡ 1 (mod 24). The floor `(z-1)**2//24` is therefore exactly
  ((z − 1)² − 1)/24, the term.
- z = (n−1)(n−2) is u(u+1) for u = 1 − n (and also for u = n − 2). `~u` is
  −(u+1), so `u*~u+1` is 1 − z, which has the same square. The counter starts
  at u = 1 for n = 0 and counts down.
- `while[print(…)]:` is a non-empty list, so it is always true.

**Notes**

- Exact integer arithmetic, so every term is right; the 4300-digit limit
  would only be reached near n = 10^1075.
- Centring at n = 3/2 instead, with m = 2n − 3, gives the same length:
  `m=3` + `while[print((m*m-5)**2//384)]:m-=2`, since
  (m² − 5)² = 384·a(n) + 16. Longer forms: `(n*n-3*n+1)**2//24` with a plain
  counter is 41 bytes; the Pascal chain `a=b=c=d=0` +
  `while[print(a)]:a+=b;b+=c;c+=d;d+=1` is 45; and `math.comb(n,4)` is 50
  with its import.
- The b-file has 1003 terms (n = 0 to 1002) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000332), CC BY-SA 4.0.
