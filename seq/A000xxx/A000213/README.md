# A000213

> Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) with a(0)=a(1)=a(2)=1.
> — [OEIS A000213](https://oeis.org/A000213)

Offset 0: 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, …

### Python 3 — 39 bytes

```python
a=b=c=1
while[print(a)]:a,b,c=b,c,a+b+c
```

**How it works**

- `a`, `b` and `c` hold three consecutive terms, a(n), a(n+1) and a(n+2),
  starting from a(0) = a(1) = a(2) = 1. All three start equal, so one
  chained `a=b=c=1` sets them, two bytes under the `a=b=0;c=1` of
  [A000073](../A000073/).
- `print(a)` runs in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends.
- `a,b,c=b,c,a+b+c` builds the right-hand tuple before assigning, so the
  triple moves one step: a(n+1), a(n+2), a(n) + a(n+1) + a(n+2) = a(n+3).
  Integers are exact, so every term is right.

**Notes**

- Running the recurrence backwards gives a(−1) = −1, a(−2) = 1, a(−3) = 1,
  so starting earlier only makes the start longer.
- In-place updates such as `a+=b;b+=c;c+=a` (14 bytes) would save a byte,
  but a search over every sequence of up to four `x+=y`, `x-=y`,
  `x+=y+z`-type statements of at most 16 bytes found none whose matrix has
  the characteristic polynomial x³ − x² − x − 1, so the tuple update stays.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  a(16250), the first term with 4301 digits, after printing a(0) to
  a(16249). The limit is not counted as a failure.
- The b-file has 3773 terms (n = 0 to 3772, the last one has 998 digits) and
  the whole of it prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000213), CC BY-SA 4.0.
