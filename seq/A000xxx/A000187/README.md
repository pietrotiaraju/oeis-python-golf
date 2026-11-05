# A000187

> Generalized Euler numbers, c(5,n).
> — [OEIS A000187](https://oeis.org/A000187)

Offset 0: 2, 30, 3522, 1066590, 604935042, 551609685150, 737740947722562, …

### Python 3 — 93 bytes

```python
r=[s:=2];p=1
while[print(s)]:
 for s in 0,(p:=p*-4)+p*abs(p):r=[s:=s+5*x for x in[0]+r[::-1]]
```

**How it works**

- a(n) = (2n)!·[x^(2n)] sec(5x)·(cos 2x + cos 4x) (Luschny's e.g.f. in
  the OEIS entry, equivalent to Bala's
  (e^(ix)+e^(3ix)+e^(7ix)+e^(9ix))/(1+e^(10ix))).
- The program runs a weighted Seidel–Entringer (boustrophedon) triangle:
  T(m,0) = u_m and T(m,k) = T(m,k−1) + 5·T(m−1,m−k), so each row is a
  running sum over the previous row read backwards. With weight 1 this is
  the boustrophedon transform of Millar, Sloane and Young (1996), and
  B_m = T(m,m) has e.g.f. (sec x + tan x)·U(x), where U is the e.g.f. of
  u. With weight c, T(m,k) = c^m·T′(m,k) where T′ is the weight-1 triangle
  started from u_m/c^m, so the e.g.f. of B becomes
  (sec cx + tan cx)·U(x).
- Take U = cos 2x + cos 4x, so u_m = 0 for odd m and
  u_(2n) = (−4)ⁿ + (−16)ⁿ. U is even, so tan 5x·U is odd and only feeds the
  odd rows. The even part of the output is sec 5x·U, the e.g.f. of a(n),
  so T(2n,2n) = a(n).
- Each pass of the `while` computes two rows: an odd row starting at 0,
  then an even row starting at u_(2n). `p` holds (−4)ⁿ and
  (−16)ⁿ = p·|p|.
- `s` is the `for` target, so it already holds the row's first value when
  the comprehension starts. The extra `[0]` in front of the reversed row
  makes the first element s + 0, and the walrus carries the running sum
  (4 B under `r=[s:=u]+[s:=s+5*x for x in r[::-1]]`). After the even row,
  `s` is a(n), which the next `while` header prints.

**Notes**

- Row m has m+1 entries, so a(n) costs about 2n² big-integer additions.
  The whole b-file (251 terms) prints in about 0.1 s; the bar is the
  whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(672) (4299 digits); a(673) has 4307.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000187), CC BY-SA 4.0.
