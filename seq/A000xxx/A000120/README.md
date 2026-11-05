# A000120

> Ones-counting sequence: number of 1's in binary expansion of n (or the
> binary weight of n).
> — [OEIS A000120](https://oeis.org/A000120)

Offset 0: 0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, …

### Python 3 — 36 bytes

```python
n=0
while[print(n.bit_count())]:n+=1
```

**How it works**

- `int.bit_count()` (Python 3.10+) returns the number of 1 bits in the
  binary expansion of `n`, which is a(n) by definition.
- The loop is the [A000027](../A000027/) one: `print` runs in the
  condition and returns `None`, `[None]` is a non-empty list and therefore
  always true, and the body steps `n` through 0, 1, 2, …

**Notes**

- `bin(n).count('1')` is the classic way to count bits and is 4 bytes
  longer than `n.bit_count()`.
- `n=0` + `while 1:print(n.bit_count());n+=1` is 1 byte longer.
- The recurrence a(2n) = a(n), a(2n+1) = a(n) + 1 can be streamed by
  walking a list while it grows, `print(0);l=[1]` +
  `for x in l:print(x);l+=x,x+1` (43 bytes); without the separate
  `print(0)` the list would start with a duplicate a(0).
- `for n in range(9**99)` (41 bytes with the print) would stop
  eventually, which the rules do not allow for an infinite sequence.
- The b-file has the 10 001 terms a(0)..a(10000), all printed in well
  under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000120), CC BY-SA 4.0.
