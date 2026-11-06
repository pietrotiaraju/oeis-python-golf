# A000523

> a(n) = floor(log_2(n)).
> — [OEIS A000523](https://oeis.org/A000523)

Offset 1: 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, …

### Python 3 — 36 bytes

```python
n=1
while[print(len(bin(n))-3)]:n+=1
```

**How it works**

- For n≥1, `bin(n)` is `0b` followed by floor(log₂(n))+1 bits.
  Subtracting 3 from its length removes the prefix and that extra bit.
- The result changes precisely at powers of 2, with no rounding error
  even for integers beyond floating point precision.
- The loop begins at n=1, whose binary expansion is `0b1` and whose
  output is 0.

**Notes**

- Binary conversion is exact and is exempt from Python's decimal
  integer conversion limit.
- The program has no input and continues for every positive n.
- The reference file contains 105 terms from the published OEIS entry; the verification
  bar is 105 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000523), CC BY-SA 4.0.
