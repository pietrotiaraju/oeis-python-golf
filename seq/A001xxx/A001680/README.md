# A001680

> The partition function G(n,3).
> — [OEIS A001680](https://oeis.org/A001680)

Offset 0: 1, 1, 2, 5, 14, 46, 166, 652, 2780, 12644, 61136, 312676, …

### Python 3 — 55 bytes

```python
a=b=n=0;c=1
while[print(c)]:n+=1;c,b,a=c+b+a//2,n*c,n*b
```

**How it works**

- G(n, 3) counts the partitions of an n-set into blocks of size at most
  3 (entry comment, e.g.f. exp(x + x²/2 + x³/6)). Look at the block that
  holds the element n: alone, with one of the other n − 1, or with two of
  them, so
  **a(n) = a(n−1) + (n−1)·a(n−2) + C(n−1, 2)·a(n−3)**
  (the recurrence and proof in the entry).
- Instead of three plain terms the loop keeps scaled ones: at the top of
  the pass that has just set n, `c` = a(n−1), `b` = (n−1)·a(n−2) and
  `a` = (n−1)(n−2)·a(n−3). Then a(n) = c + b + a/2, and the next state is
  just b = n·a(n−1), a = n·b_old = n(n−1)·a(n−2): no binomial coefficient
  is ever formed. a is a product of two consecutive integers times an
  integer, so `a//2` is exact.
- Zero seeds work: `c=1` is a(0), and b, a are multiplied by n = 1 in the
  first pass, so the missing a(−1), a(−2) never matter.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (654 terms, up to a(653)) prints in about 0.1 s; the
  bar is the whole b-file in 60 s.
- a(2290) is the first term with more than 4300 digits, where Python's
  int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001680), CC BY-SA 4.0.
