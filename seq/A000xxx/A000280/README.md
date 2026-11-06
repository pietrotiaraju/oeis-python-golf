# A000280

> a(n) = a(n-1) + a(n-2)^3.
> — [OEIS A000280](https://oeis.org/A000280)

Offset 0: 0, 1, 1, 2, 3, 11, 38, 1369, 56241, 2565782650, …

### Python 3 — 36 bytes

```python
a,b=0,1
while[print(a)]:a,b=b,b+a**3
```

**How it works**

- The pair (a, b) holds (a(n), a(n+1)), starting from a(0) = 0, a(1) = 1.
  Each pass prints a(n) and moves the window one step:
  a(n+2) = a(n+1) + a(n)³.
- `while[print(a)]:` prints at the top of every pass; `[None]` is a
  non-empty list, so the loop never stops on its own.

**Notes**

- The number of digits roughly triples every two steps: a(20) has 3463
  digits and a(21) about 6900, past CPython's 4300-digit int-to-str limit,
  so the program prints 21 terms (n = 0..20) and stops with a
  `ValueError`. The b-file has 18 terms, so the bar is the whole b-file.
- Starting one step early does not help: going back, a(−1) = 1 and
  a(−2) = −1, but a(−3)³ = 2 has no integer solution, and no earlier pair
  has two equal values that `a=b=…` could set.
- Same length: `a=1;b=0` with `print(b)`, or `a=0;b=1`. Updating in place
  (`b+=a**3;a=b-a**3`) is 4 bytes longer, and a queue that grows while it
  is read (`l=[0,1]` / `for x in l:print(x);l+=l[-1]+x**3,`) is 42.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000280), CC BY-SA 4.0.
