# A000788

> Total number of 1's in binary expansions of 0, ..., n.
> — [OEIS A000788](https://oeis.org/A000788)

Offset 0: 0, 1, 2, 4, 5, 7, 9, 12, 13, 15, 17, 20, 22, 25, 28, 32, 33, 35, 37, 40, 42, 45, …

### Python 3 — 43 bytes

```python
a=n=0
while[print(a)]:n+=1;a+=n.bit_count()
```

**How it works**

- A running sum of the binary weights: `n.bit_count()` (Python 3.10+) is
  the number of 1's of n, and `a` adds it up from a(0) = 0.

**Notes**

- `bin(n).count('1')` is 4 bytes longer; putting the sum in the print,
  `while[print(a:=a+n.bit_count())]:n+=1`, ties at 43.
- The whole b-file (10001 terms) prints in a fraction of a second; it is
  the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000788), CC BY-SA 4.0.
