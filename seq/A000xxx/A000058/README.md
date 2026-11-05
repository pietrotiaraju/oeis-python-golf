# A000058

> Sylvester's sequence: a(n+1) = a(n)^2 - a(n) + 1, with a(0) = 2.
> — [OEIS A000058](https://oeis.org/A000058)

Offset 0: 2, 3, 7, 43, 1807, 3263443, 10650056950807, …

### Python 3 — 28 bytes

```python
b=1
while[print(b+1)]:b*=b+1
```

**How it works**

- `b` is a(n) − 1. The recurrence gives a(n+1) − 1 = a(n)² − a(n) =
  a(n)·(a(n) − 1), so **b(n+1) = (b(n) + 1)·b(n)**, with b(0) = 1. In-place
  that is just `b*=b+1`, three bytes shorter than `a=a*a-a+1`, and paying
  `+1` in the print costs only two of them back.
- It is the same as the other classic form a(n) = 1 + a(0)·a(1)·…·a(n−1):
  `b` is the running product of the terms printed so far.
- `while[print(b+1)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true.

**Notes**

- The terms roughly double in length each step: a(12) has 834 digits,
  a(14) 3336 and a(15) 6672. The program prints a(0) to a(14) and then stops
  on Python's 4300-digit int-to-str limit (a `ValueError` on stderr), which
  the rules count as an interpreter limit, not a failure. The b-file has
  13 terms, a(0) to a(12), and the bar is all of them in 60 s.
- Tracking a(n) directly, `a=2` with `while[print(a)]:a=a*a-a+1`, is
  29 bytes (`a*~-a+1` is no shorter than `a*a-a+1`). `while 1:print(b+1);…`
  costs one byte more than the list condition, and a walrus
  `print(a:=b+1)` … `b*=a` saves nothing.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000058), CC BY-SA 4.0.
