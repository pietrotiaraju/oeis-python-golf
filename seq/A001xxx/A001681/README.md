# A001681

> The partition function G(n,4).
> — [OEIS A001681](https://oeis.org/A001681)

Offset 0: 1, 1, 2, 5, 15, 51, 196, 827, 3795, 18755, 99146, 556711, …

### Python 3 — 68 bytes

```python
d=a=b=n=0;c=1
while[print(c)]:n+=1;c,b,a,d=c+b+a//2+d//6,n*c,n*b,n*a
```

**How it works**

- G(n, 4) counts the partitions of an n-set into blocks of size at most
  4 (entry comment, e.g.f. exp(x + x²/2 + x³/6 + x⁴/24)). Look at the
  block that holds the element n: it has 0, 1, 2 or 3 of the other n − 1
  elements, so
  **a(n) = a(n−1) + (n−1)·a(n−2) + C(n−1, 2)·a(n−3) + C(n−1, 3)·a(n−4)**
  (Kotesovec's recurrence in the entry, 6a(n) = 6a(n−1) + …, is the same
  one times 6).
- This is the [A001680](../A001680/) loop (G(n, 3)) with one more state.
  At the top of the pass that has just set n, `c` = a(n−1),
  `b` = (n−1)·a(n−2), `a` = (n−1)(n−2)·a(n−3) and
  `d` = (n−1)(n−2)(n−3)·a(n−4). Then a(n) = c + b + a/2 + d/6, and the
  next state is just b = n·c, a = n·b, d = n·a: no binomial coefficient
  is ever formed. `a` holds a product of two consecutive integers and `d`
  one of three, so `a//2` and `d//6` are exact.
- Zero seeds work: `c=1` is a(0), and b, a, d are multiplied by n = 1 in
  the first pass, so the missing a(−1), a(−2), a(−3) never matter.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (610 terms, up to a(609)) prints in about 0.1 s; the
  bar is the whole b-file in 60 s.
- a(2125) is the first term with more than 4300 digits, where Python's
  int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001681), CC BY-SA 4.0.
