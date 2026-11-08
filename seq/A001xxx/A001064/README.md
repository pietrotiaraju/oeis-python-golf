# A001064

> a(n) = a(n-1)*a(n-2) + a(n-3).
> — [OEIS A001064](https://oeis.org/A001064)

Offset 0: 1, 1, 0, 1, 1, 1, 2, 3, 7, 23, 164, 3779, 619779, 2342145005, …

### Python 3 — 41 bytes

```python
a=b=1;c=0
while[print(a)]:a,b,c=b,c,b*c+a
```

**How it works**

- `a`, `b`, `c` hold a(n), a(n+1), a(n+2), starting from the OEIS values
  a(0) = 1, a(1) = 1, a(2) = 0 (then a(3) = 0·1 + 1 = 1, a(4) = 1·0 + 1 = 1,
  a(5) = 1·1 + 0 = 1, a(6) = 2, …).
- `a,b,c=b,c,b*c+a` moves one step: the new triple ends with
  a(n+2)·a(n+1) + a(n) = a(n+3). Exact integer arithmetic.
- `print(a)` in the loop condition returns `None`, and `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- Printing the newest term with walruses doing the shift,
  `while 1:print(c:=a+(a:=b)*(b:=c))`, needs the start
  (a(−3), a(−2), a(−1)) = (3, 2, −1), so it is 46 bytes; printing the
  middle term needs (−1, 1, 1), no shorter than `a=b=1;c=0`.
- The terms grow like c^(φⁿ): a(22) has 713 digits, a(25) 3018 and a(26)
  4882. The program prints a(0) to a(25) and then stops on Python's
  4300-digit int-to-str limit (a `ValueError` on stderr), an interpreter
  limit, not a failure.
- The b-file has 23 terms (a(0) to a(22)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001064), CC BY-SA 4.0.
