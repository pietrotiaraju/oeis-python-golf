# A000806

> Bessel polynomial y_n(-1).
> — [OEIS A000806](https://oeis.org/A000806)

Offset 0: 1, 0, 1, −5, 36, −329, 3655, −47844, 721315, −12310199, 234615096, −4939227215, …

### Python 3 — 40 bytes

```python
a=b=k=1
while[print(b)]:a,b=b,a-k*b;k+=2
```

**How it works**

- The Bessel polynomials satisfy y_n(x) = (2n−1)·x·y_(n−1)(x) + y_(n−2)(x),
  with y_0 = 1 and y_1 = 1 + x. At x = −1 this is the recurrence in the
  OEIS entry: a(n) = a(n−2) − (2n−1)·a(n−1), a(0) = 1, a(1) = 0.
- Run one step backwards, it gives a(−1) = a(1) + a(0) = 1 (the entry's
  symmetry a(−1−n) = a(n)). So the state (a, b, k) = (a(n−1), a(n), 2n+1)
  starts as `a=b=k=1`, and each pass prints b, then moves on with
  a, b = b, a − k·b and k += 2.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (405 terms, up to a(404)) prints in a few hundredths of
  a second; the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1423).
- `b=a-k*(a:=b)` does the same swap but is 1 byte longer than
  `a,b=b,a-k*b`; starting from (a(0), a(1)) = (1, 0) needs k = 3 and costs
  4 bytes more than `a=b=k=1`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000806), CC BY-SA 4.0.
