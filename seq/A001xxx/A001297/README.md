# A001297

> Stirling numbers of the second kind S(n+3, n).
> — [OEIS A001297](https://oeis.org/A001297)

Offset 0: 0, 1, 15, 90, 350, 1050, 2646, 5880, 11880, 22275, …

### Python 3 — 48 bytes

```python
n=0
while[print((n*~n)**2*(n+2)*(n+3)//48)]:n+=1
```

**How it works**

- a(n) = C(n+1, 2)·C(n+3, 4) = n²(n+1)²(n+2)(n+3)/48 (Shevelev's formula on
  the OEIS entry). It holds for every n: call the right side P(n). P(0) = 0
  = S(3, 0), and
  P(n) − P(n−1) = n²(n+1)(n+2)·((n+1)(n+3) − (n−1)²)/48
  = n²(n+1)(n+2)(3n+1)/24 = n·S(n+2, n), using S(n+2, n) =
  (3n+1)·n(n+1)(n+2)/24 ([A001296](../A001296/)). The Stirling recurrence
  S(n+3, n) = n·S(n+2, n) + S(n+2, n−1) gives a(n) the same first
  differences, so a(n) = P(n).
- `~n` is −n − 1, so `(n*~n)**2` is n²(n+1)², a byte under `(n*n+n)**2`.
  P(n) is an integer, so `//48` is exact.

**Notes**

- With `(n*n+n)**2` it is 49 bytes. The running sums of the Stirling
  recurrence with the step of [A001296](../A001296/), `b=c=n=0` /
  `while[print(c)]:n+=1;b-=n*n*~n//2;c+=n*b`, tie at 48; the plain chain
  `a=b=c=n=0` / `while[print(c)]:n+=1;a+=n;b+=n*a;c+=n*b` is 49.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁶/48, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001297), CC BY-SA 4.0.
