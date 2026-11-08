# A001054

> a(n) = a(n-1)*a(n-2) - 1.
> — [OEIS A001054](https://oeis.org/A001054)

Offset 0: 0, 1, -1, -2, 1, -3, -4, 11, -45, -496, 22319, -11070225, …

### Python 3 — 35 bytes

```python
a,b=0,1
while[print(a)]:a,b=b,a*b-1
```

**How it works**

- `a` and `b` hold a(n) and a(n+1), starting from a(0) = 0 and a(1) = 1
  (the OEIS data: a(2) = 1·0 − 1 = −1, a(3) = (−1)·1 − 1 = −2, …).
- `a,b=b,a*b-1` moves one step: the new pair is a(n+1) and
  a(n+1)·a(n) − 1 = a(n+2). Negative terms print with a minus sign, as in
  the OEIS (keyword sign).
- `print(a)` in the loop condition returns `None`, and `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- No earlier start exists: a(1) = a(0)·a(−1) − 1 = −1 for any a(−1), not 1.
  For the same reason the walrus form `print(a:=b*(b:=a)-1)` (see
  [A001056](../A001056/)) has no valid start.
- |a(n)| grows like c^(φⁿ): a(21) has 867 digits, a(24) 3669 and a(25)
  5937. The program prints a(0) to a(24) and then stops on Python's
  4300-digit int-to-str limit (a `ValueError` on stderr), an interpreter
  limit, not a failure.
- The b-file has 22 terms (a(0) to a(21)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001054), CC BY-SA 4.0.
