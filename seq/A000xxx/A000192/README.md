# A000192

> Generalized Euler numbers c(6,n).
> — [OEIS A000192](https://oeis.org/A000192)

Offset 0: 2, 46, 7970, 3487246, 2849229890, 3741386059246, 7205584123783010, …

### Python 3 — 89 bytes

```python
r=[s:=2];p=1
while[print(s)]:
 for s in 0,(p:=p*-25)-1|2:r=[s:=s+6*x for x in[0]+r[::-1]]
```

**How it works**

- a(n) = (2n)!·[x^(2n)] sec(6x)·(cos x + cos 5x) (Luschny's e.g.f. in
  the OEIS entry; Chapoton's 2cos(3x)/(2cos(4x)−1) is the same function,
  since cos 6x = cos 2x·(2cos 4x − 1)).
- Same weighted Seidel–Entringer triangle as [A000187](../A000187/):
  T(m,0) = u_m and T(m,k) = T(m,k−1) + 6·T(m−1,m−k). Its diagonal
  T(m,m) has e.g.f. (sec 6x + tan 6x)·U(x), where U is the e.g.f. of u.
- Take U = cos x + cos 5x, so u_m = 0 for odd m and
  u_(2n) = (−1)ⁿ + (−25)ⁿ. U is even, so tan 6x·U only feeds the odd
  rows, and T(2n,2n) = a(n).
- `p` holds (−25)ⁿ, and u_(2n) = (p−1)|2: p − 1 is 0 (mod 8) for even n
  and 6 (mod 8) for odd n, so `|2` adds 2 in the first case (p + 1) and
  nothing in the second (p − 1). That is 2 B under `p+2-p%4`.
- Each pass of the `while` computes two rows: an odd row starting at 0,
  then an even row starting at u_(2n). `s` is the `for` target, so it
  already holds the row's first value; the `[0]` in front of the reversed
  row makes the first element s + 0, and the walrus carries the running
  sum. After the even row, `s` is a(n), which the next `while` header
  prints.

**Notes**

- Row m has m+1 entries, so a(n) costs about 2n² big-integer additions.
  The whole b-file (251 terms) prints in about 0.1 s; the bar is the
  whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(657).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000192), CC BY-SA 4.0.
