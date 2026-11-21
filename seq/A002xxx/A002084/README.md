# A002084

> Sinh(x) / cos(x) = Sum_{n>=0} a(n)*x^(2n+1)/(2n+1)!.
> — [OEIS A002084](https://oeis.org/A002084)

Offset 0: 1, 4, 36, 624, 18256, 814144, 51475776, 4381112064, 482962852096, …

### Python 3 — 72 bytes

```python
r=[1,s:=1]
while[print(s)]:
 for s in 0,1:r=[s:=s+x for x in[0]+r[::-1]]
```

**How it works**

- **Triangle.** The program runs Millar, Sloane and Young's boustrophedon (Seidel–Entringer) triangle:
  T(m, 0) = u_m and T(m, k) = T(m, k−1) + T(m−1, m−k), each row a running
  sum over the previous row read backwards; its diagonal B_m = T(m, m) has
  e.g.f. (sec x + tan x)·U(x), where U is the e.g.f. of u.
- **Start values.** Take U = sinh x, i.e. u_m = 0 for even m and 1 for odd
  m. sec x is even and sinh x odd, so tan x·sinh x is even and the odd
  part of (sec x + tan x)·sinh x is sec x·sinh x = sinh x/cos x, the
  e.g.f. of a(n). Hence a(n) = T(2n+1, 2n+1).
- **Loop.** `r` starts as row 1, [1, 1], with s = a(0) = 1. Each pass
  builds an even row from start value 0 and an odd row from 1: the `for`
  target `s` is the row's first value, the extra `[0]` in front of the
  reversed row makes the first element s + 0, and the walrus carries the
  running sum (as in [A000187](../A000187/)). After the odd row, `s` is
  a(n), which the `while` header prints.

**Notes**

- Row m has m + 1 entries, so the first n terms cost about 2n²
  additions. The b-file has 51 terms (n = 0 to 50), and the bar is the
  whole b-file in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 72 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002084), CC BY-SA 4.0.
