# A000866

> 2^n written in base 5.
> — [OEIS A000866](https://oeis.org/A000866)

Offset 0: 1, 2, 4, 13, 31, 112, 224, 1003, 2011, 4022, 13044, 31143, 112341, 230232, …

### Python 3 — 59 bytes

```python
f=lambda m:m and f(m//5)*10+m%5
n=1
while[print(f(n))]:n*=2
```

**How it works**

- `f(m)` writes m in base 5 and reads the digits back in base 10: the last
  base-5 digit is m mod 5, the others are the digits of ⌊m/5⌋, so
  f(m) = 10·f(⌊m/5⌋) + (m mod 5), with f(0) = 0 from `m and …`. For
  m = 8 = 1·5 + 3 that gives 13.
- `n` holds 2ⁿ exactly and doubles at every step; `print(f(n))` in the loop
  condition returns `None`, and `[None]` is a non-empty list, so the loop
  never ends.

**Notes**

- Python has no base-5 format, so the digits have to be peeled off. A loop
  that builds the string, `m=n;s=''` / `while m:s=str(m%5)+s;m//=5`, makes
  the program 65 bytes.
- The recursion goes one level per base-5 digit, and Python's default limit
  of 1000 nested calls ends the program with a `RecursionError` at 2²³¹⁸,
  the first power with 999 base-5 digits, after printing a(0) to a(2317)
  in about 1.4 s. The limit is not counted as a failure.
- The b-file has 301 terms (up to a(300)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000866), CC BY-SA 4.0.
