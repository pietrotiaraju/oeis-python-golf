# A001296

> 4-dimensional pyramidal numbers: a(n) = (3*n+1)*binomial(n+2, 3)/4. Also Stirling2(n+2, n).
> — [OEIS A001296](https://oeis.org/A001296)

Offset 0: 0, 1, 7, 25, 65, 140, 266, 462, 750, 1155, …

### Python 3 — 39 bytes

```python
b=n=0
while[print(b)]:n+=1;b-=n*n*~n//2
```

**How it works**

- The Stirling recurrence S(m, k) = k·S(m−1, k) + S(m−1, k−1) with
  m = n + 2, k = n reads a(n) = n·S(n+1, n) + a(n−1), and
  S(n+1, n) = C(n+1, 2) = n(n+1)/2 (choose the one block of size 2). So
  a(n) = a(n−1) + n²(n+1)/2, with a(0) = S(2, 0) = 0: the OEIS formula
  a(n) = Sum_{j=0..n} j·A000217(j).
- `~n` is −n − 1, so `n*n*~n//2` is −n²(n+1)/2 and `b-=` adds n²(n+1)/2,
  a byte under `b+=n*n*-~n//2`. Either n or n + 1 is even, so n²(n+1) is
  even and the floor division is exact.
- `b` starts at a(0) = 0, and each pass steps n and adds the next
  difference.

**Notes**

- Keeping the triangular number in its own variable,
  `a=b=n=0` / `while[print(b)]:n+=1;a+=n;b+=n*a`, is 40 bytes. The
  closed form (3n+1)·n(n+1)(n+2)/24 is 43 bytes with m = n + 1,
  `(3*n-2)*(n**3-n)//24`, and 46 as `-n*~n*(n+2)*(3*n+1)//24`.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁴/8, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001296), CC BY-SA 4.0.
