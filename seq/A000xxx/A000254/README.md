# A000254

> Unsigned Stirling numbers of first kind, s(n+1,2): a(n+1) = (n+1)*a(n) + n!.
> — [OEIS A000254](https://oeis.org/A000254)

Offset 0: 0, 1, 3, 11, 50, 274, 1764, 13068, 109584, 1026576, 10628640, …

### Python 3 — 43 bytes

```python
a=0;f=n=1
while[print(a)]:a=a*n+f;f*=n;n+=1
```

**How it works**

- The recurrence from the name, a(n) = n·a(n−1) + (n−1)!, needs two
  numbers besides the counter: `a` is the term and `f` the factorial that
  goes with it. At the top of each round `a` = a(n−1) and `f` = (n−1)!, so
  `a=a*n+f` gives a(n), `f*=n` gives n!, and `n+=1` moves on.
- Starting from a(0) = 0, 0! = 1, n = 1, the loop prints 0, 1, 3, 11, …
- `while[print(a)]:` is one byte under `while 1:print(a);`: `print`
  returns `None`, but the list `[None]` is not empty, so it is true.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (450 terms) prints at once; the program stops after a(1557), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.
- A tie at 43 bytes: `a=f=n=1` with `print(a-f)`. Adding any multiple of
  n! to a(n) keeps the recurrence, so a(n) + n! starts at 1 like the other
  two variables; the shorter start pays for the `-f` in the print.
- a(n) = n!·H_n, but summing `f//k` over k, or carrying H_n as a fraction,
  costs more than keeping the factorial alongside. A recurrence without the
  factorial, a(n) = (2n−1)·a(n−1) − (n−1)²·a(n−2), still needs two terms
  and the counter, and its update is longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000254), CC BY-SA 4.0.
