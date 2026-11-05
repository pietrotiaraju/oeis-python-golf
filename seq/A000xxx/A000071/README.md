# A000071

> a(n) = Fibonacci(n) - 1.
> — [OEIS A000071](https://oeis.org/A000071)

Offset 1: 0, 0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609, 986, …

### Python 3 — 32 bytes

```python
a=b=0
while[print(a)]:a,b=b,a-~b
```

**How it works**

- Subtracting 1 from F(n) = F(n−1) + F(n−2) gives
  **a(n) = a(n−1) + a(n−2) + 1**, so the sequence is the
  [A000045](../A000045/) loop with a +1 in the step, started at
  a(1) = a(2) = 0.
- `a-~b` is a + b + 1, since `~b` is −b − 1. It is one byte shorter than
  `a+b+1`.
- `a` and `b` hold a(n) and a(n+1). `print(a)` runs in the loop condition
  and `[None]` is true, so the loop never ends (the [A000007](../A000007/)
  trick).

**Notes**

- Shifting the Fibonacci loop instead, `a=b=1` +
  `while[print(a-1)]:a,b=b,a+b`, is 33 bytes: the `-1` in the print costs
  two bytes and the plain `a+b` step saves only one.
- `b=a-~(a:=b)` for the step is also right (the left `a` is read before
  the walrus changes it) but one byte longer than `a,b=b,a-~b`.
- sympy's `fibonacci(n)-1` in an `n+=1` loop is 56 bytes, so there is no
  sympy entry.
- Python ints are exact, so the only limit is the 4300-digit int-to-str
  limit of Python 3.11+: the program prints a(1) to a(20577) and then stops
  with a `ValueError` at a(20578), the first term with more than 4300
  digits.
- The b-file has 500 terms (up to a(500), 105 digits) and all of them print
  at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000071), CC BY-SA 4.0.
