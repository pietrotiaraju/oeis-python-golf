# A000211

> a(n) = a(n-1) + a(n-2) - 2, a(0) = 4, a(1) = 3.
> — [OEIS A000211](https://oeis.org/A000211)

Offset 0: 4, 3, 5, 6, 9, 13, 20, 31, 49, 78, …

### Python 3 — 35 bytes

```python
a,b=4,3
while[print(a)]:a,b=b,a+b-2
```

**How it works**

- The definition itself: `a, b` hold a(n), a(n+1), and each pass prints
  a(n) and steps the pair to a(n+1), a(n) + a(n+1) − 2.
- `while[print(…)]:` runs the print in the loop test: the list `[None]` is
  non-empty, hence true, and the body only steps the pair. One byte under
  `while 1:print(a);a,b=b,a+b-2`.

**Notes**

- Integer arithmetic only, so it is correct for every n. It prints the
  whole b-file (501 terms) at once; the bar is the whole b-file in 60 s.
- It stops at Python's 4300-digit limit for converting an int to a string:
  a(20575) is the last term printed (a(20576) has 4301 digits), about 3 s in.
- a(n) is the Lucas number L(n) + 2 ([A000032](https://oeis.org/A000032)),
  but `a,b=2,1` / `while[print(a+2)]:a,b=b,a+b` ties: the `-2` just moves
  into the print. A seed pair can't shrink to `a=b=…`, since no two
  consecutive terms are equal, even extended to negative n (…, 9, −2, 5, 1,
  4, 3, …).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000211), CC BY-SA 4.0.
