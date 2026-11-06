# A000284

> a(n) = a(n-1)^3 + a(n-2) with a(0)=0, a(1)=1.
> — [OEIS A000284](https://oeis.org/A000284)

Offset 0: 0, 1, 1, 2, 9, 731, 390617900, 59601394712394173339000731, …

### Python 3 — 36 bytes

```python
a,b=0,1
while[print(a)]:a,b=b,b**3+a
```

**How it works**

- The pair (a, b) holds (a(n), a(n+1)), starting from a(0) = 0, a(1) = 1.
  Each pass prints a(n) and moves the window one step:
  a(n+2) = a(n+1)³ + a(n).
- `while[print(a)]:` prints at the top of every pass; `[None]` is a
  non-empty list, so the loop never stops on its own.

**Notes**

- The number of digits triples every step: a(11) has 2088 digits and a(12)
  about 6264, past CPython's 4300-digit int-to-str limit, so the program
  prints 12 terms (n = 0..11) and stops with a `ValueError`. The b-file has
  11 terms, so the bar is the whole b-file.
- The only equal pair is (a(1), a(2)) = (1, 1), but `a=b=1` starts one step
  late and printing a(0) back as `b-a**3` costs more than it saves (39).
  Going back gives a(−1) = 1, a(−2) = −1, a(−3) = 2, a(−4) = −9, …, never
  two equal values in a row.
- Same length: `a=1;b=0` with `print(b)`, or `a=0;b=1`. The walrus update
  `while 1:print(a);b=a+(a:=b)**3` is 38, and a queue that grows while it
  is read (`l=[0,1]` / `for x in l:print(x);l+=l[-1]**3+x,`) is 42.
- Same program shape as [A000280](../A000280/), a(n) = a(n−1) + a(n−2)³,
  with the cube moved to the newer term.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000284), CC BY-SA 4.0.
