# A000283

> a(n) = a(n-1)^2 + a(n-2)^2 for n >= 2 with a(0) = 0 and a(1) = 1.
> — [OEIS A000283](https://oeis.org/A000283)

Offset 0: 0, 1, 1, 2, 5, 29, 866, 750797, 563696885165, …

### Python 3 — 35 bytes

```python
a=b=-1
while 1:print(a:=b+(b:=a*a))
```

**How it works**

- Before a(n) is printed, `a` is a(n−1) and `b` is a(n−2)². In
  `b+(b:=a*a)` the left operand is read first, so the sum is
  a(n−2)² + a(n−1)² = a(n), and on the way `b` becomes a(n−1)². The outer
  walrus then stores a(n) in `a`, which leaves the state ready for n + 1.
  This is one byte under the tuple swap `a,b=b,a*a+b*b`.
- The seeds are the state for n = 0 read backwards: a(1) = a(0)² + a(−1)²
  gives a(−1)² = 1, and a(0) = a(−1)² + b gives b = −1. No real a(−2) has
  that square, but `b` is just a number here, so it can be −1, and choosing
  a(−1) = −1 makes both seeds equal: `a=b=-1` is a byte under `a,b=0,1`.
- The update happens inside the print, so the loop is a plain `while 1:`.

**Notes**

- Exact integer arithmetic, correct for every n. The digit count roughly
  doubles each step: a(14) has 753 digits and a(16) 3009, so the program
  prints a(0) to a(16) and then stops on Python's 4300-digit int-to-str
  limit at a(17) (about 6017 digits), a `ValueError` on stderr that the
  rules count as an interpreter limit. The b-file has a(0) to a(14), and the
  bar is all 15 terms in 60 s.
- With the print first, the state has to be (a(0), a(−1)²) = (0, 1):
  `a,b=0,1` / `while[print(a)]:a=b+(b:=a*a)` is 36 bytes, and the plain
  pair `a,b=0,1` / `while[print(a)]:a,b=b,a*a+b*b` is 37. Equal seeds would
  have to be a(0) = 0 there, and (0, 0) stays at 0. A recursive
  `def f(a,b):print(a);f(b,a*a+b*b)` / `f(0,1)` is 39.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000283), CC BY-SA 4.0.
