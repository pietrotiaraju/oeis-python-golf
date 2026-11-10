# A001525

> a(n) = (3n)!/(3!n!).
> — [OEIS A001525](https://oeis.org/A001525)

Offset 1: 1, 60, 10080, 3326400, 1816214400, 1482030950400, …

### Python 3 — 37 bytes

```python
a=n=1
while[print(a)]:n+=3;a*=n*-~n*3
```

**How it works**

- a(k + 1)/a(k) = (3k + 1)(3k + 2)(3k + 3)/(k + 1) = 3(3k + 1)(3k + 2), and
  a(1) = 3!/(3!·1!) = 1.
- `a=n=1` starts both at 1. After `n+=3` the counter is n = 3k + 1, where k is
  the index just printed, so `n*-~n*3` (`-~n` is n + 1) is 3(3k + 1)(3k + 2)
  and `a*=` turns a(k) into a(k + 1). Every factor is an integer, so the
  products stay exact.
- `print(a)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- Printing b(k) = (3k)!/k! = 6a(k) from b(0) = 1, `a=n=1` /
  `while 1:a*=n*-~n*3;print(a//6);n+=3`, is 3 bytes longer. With the
  library, (3k)!/k! is `math.perm(3*k,2*k)`, and `perm(3*n,2*n)//6` after
  `from math import*` with a plain counter is 58 bytes.
- a(n) first has more than 4300 digits at n = 690, where Python's int-to-str
  limit stops the program.
- The b-file has 100 terms (n = 1 to 100) and all of them print at once; the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001525), CC BY-SA 4.0.
