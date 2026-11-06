# A000045

> Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
> — [OEIS A000045](https://oeis.org/A000045)

Offset 0: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, …

### Python 3 — 31 bytes

```python
a=b=1
while[print(a:=b-a)]:b+=a
```

**How it works**

- Before each print, `a` is F(n−1) and `b` is F(n+1); the walrus
  `a:=b-a` turns `a` into F(n+1) − F(n−1) = F(n) and prints it.
- The body `b+=a` then makes `b` = F(n+1) + F(n) = F(n+2), so the pair is
  (F(n), F(n+2)) and the next pass prints F(n+2) − F(n) = F(n+1).
- The start `a=b=1` is (F(−1), F(1)) = (1, 1), so the first print is
  F(0) = 0. Only one variable is updated per pass, so no tuple swap is needed.
- `print(…)` returns `None`, and `[None]` is a non-empty list, so the
  condition is always true (the [A000007](../A000007/) loop).

**Notes**

- The previous record, `a,b=0,1` + `while[print(a)]:a,b=b,a+b` (33 bytes),
  moves both terms at once with a tuple assignment; `while 1:print(a);a,b=b,a+b`
  is one byte longer still.
- `a=b=1` + `while[print(b-a)]:a,b=b,a+b` is also 33: it prints the
  difference but still swaps the pair. Keeping the difference in `a` is what
  drops the swap.
- The trick needs a(0) = 0 (it rests on F(−1) = F(1)), so it does not carry over
  directly to Lucas-type starts.
- Python ints are exact, so the only limit is the 4300-digit int-to-str limit
  of Python 3.11+: the program prints F(0) to F(20577) and then stops with a
  `ValueError` at F(20578), the first term with more than 4300 digits.
- The b-file has 2001 terms (up to F(2000), 418 digits) and all of them print
  in well under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 33 | first entry |
| 2026-11-06 | Python 3 | 31 | keep the difference: `a:=b-a`, `b+=a` (found while golfing A000301) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000045), CC BY-SA 4.0.
