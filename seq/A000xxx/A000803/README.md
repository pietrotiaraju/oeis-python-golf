# A000803

> a(n+3) = a(n+2) + a(n+1) + a(n) - 4.
> — [OEIS A000803](https://oeis.org/A000803)

Offset 0: 0, 0, 8, 4, 8, 16, 24, 44, 80, 144, 264, 484, 888, 1632, 3000, 5516, 10144, …

### Python 3 — 43 bytes

```python
a=b=0;c=8
while[print(a)]:a,b,c=b,c,a+b+c-4
```

**How it works**

- `a`, `b` and `c` hold three consecutive terms a(n), a(n+1), a(n+2),
  starting from a(0) = a(1) = 0 and a(2) = 8 (the OEIS data).
- `print(a)` runs in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends.
- `a,b,c=b,c,a+b+c-4` builds the right-hand tuple before assigning, so the
  triple moves one step: a(n+1), a(n+2), a(n) + a(n+1) + a(n+2) − 4 = a(n+3).
  Integers are exact, so every term is right.

**Notes**

- The tribonacci update is the one of [A000213](../A000213/), where a search
  found no shorter chain of in-place updates; the `-4` just rides along.
- Writing a(n) = b(n) + 2 removes the constant (b is plain tribonacci with
  b(0), b(1), b(2) = −2, −2, 6), but `a=b=-2;c=6` and `print(a+2)` make it
  44 bytes. All terms are multiples of 4, and d(n) = a(n)/4 follows the same
  recurrence with −1, but `print(4*a)` makes that 45.
- Running the recurrence back gives a(−1) = 12, so starting earlier does not
  give a shorter start either.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  a(16249), the first term with 4301 digits, after printing a(0) to
  a(16248) in about 3 s. The limit is not counted as a failure.
- The b-file has 401 terms (up to a(400)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000803), CC BY-SA 4.0.
