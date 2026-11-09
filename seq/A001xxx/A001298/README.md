# A001298

> Stirling numbers of the second kind S(n+4, n).
> — [OEIS A001298](https://oeis.org/A001298)

Offset 0: 0, 1, 31, 301, 1701, 6951, 22827, 63987, 159027, 359502, …

### Python 3 — 56 bytes

```python
d=n=0
while[print(d)]:n+=1;d+=n**3*~n*~n*(n+2)*(n+3)//48
```

**How it works**

- The Stirling recurrence S(m, k) = k·S(m−1, k) + S(m−1, k−1) with
  m = n + 4, k = n gives a(n) = a(n−1) + n·S(n+3, n), and a(0) = S(4, 0)
  = 0.
- S(n+3, n) = n²(n+1)²(n+2)(n+3)/48 for every n (proved on
  [A001297](../A001297/)), so the step is n³(n+1)²(n+2)(n+3)/48. `~n` is
  −n − 1, so `~n*~n` is (n+1)² and `n**3*~n*~n*(n+2)*(n+3)` is that
  product, 48·n·S(n+3, n): the floor division is exact.
- `d` starts at a(0) = 0; each pass steps n and adds the next term.

**Notes**

- The plain chain of running sums of the recurrence,
  `a=b=c=d=n=0` / `while[print(d)]:n+=1;a+=n;b+=n*a;c+=n*b;d+=n*c`, is
  58 bytes (57 with `b-=n*n*~n//2` in place of `a`), and the step written
  `n*(n*~n)**2*(n+2)*(n+3)//48` is 57. The
  closed form (15n³+30n²+5n−2)·C(n+4, 5)/48 is much longer.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁸/384, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001298), CC BY-SA 4.0.
