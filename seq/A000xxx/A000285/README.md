# A000285

> a(0) = 1, a(1) = 4, and a(n) = a(n-1) + a(n-2) for n >= 2.
> — [OEIS A000285](https://oeis.org/A000285)

Offset 0: 1, 4, 5, 9, 14, 23, 37, 60, 97, 157, 254, 411, 665, 1076, …

### Python 3 — 33 bytes

```python
a,b=1,4
while[print(a)]:a,b=b,a+b
```

**How it works**

- The [A000045](../A000045/) loop with another start: `a` and `b` hold
  a(n) and a(n+1), starting from a(0) = 1 and a(1) = 4.
- `print(a)` runs in the loop condition; it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends.
- `a,b=b,a+b` builds the right-hand tuple first, so (a(n), a(n+1)) becomes
  (a(n+1), a(n) + a(n+1)) in one step.

**Notes**

- Running the pair the other way, (a(n), a(n−1)) from a(0) = 1 and
  a(−1) = a(1) − a(0) = 3, is also 33 bytes: `a,b=1,3` +
  `while[print(a)]:a,b=a+b,a`. No pair of consecutive terms is equal, so the
  `a=b=1` start of A000045's 33-byte tie has no counterpart here.
- a(n) = 2·F(n) + F(n+2), but any closed form needs the Fibonacci numbers
  first.
- Exact integers, so every term is right. Python's 4300-digit int-to-str
  limit stops the program at a(20574), the first term with more than 4300
  digits, after printing a(0) to a(20573).
- The b-file has 501 terms (up to a(500), 105 digits) and all of them print
  at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000285), CC BY-SA 4.0.
